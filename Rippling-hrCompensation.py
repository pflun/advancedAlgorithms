# -*- coding: utf-8 -*-
# Rippling - HR Compensation System
# Temporal salary data: create/update/cancel future changes, query salary on any date.
# Dict 1 records:       employee_id -> sorted list of (effective_date, CompensationRecord)
# Dict 2 date_index:    (employee_id, effective_date) -> record_id  [O(1) conflict check]
# Dict 3 pending_index: record_id -> record  [only PENDING records can be mutated]
# Dict 4 audit_log:     employee_id -> list of AuditEvent

import bisect

# ── Data classes ──────────────────────────────────────────────

class CompensationRecord(object):
    def __init__(self, record_id, employee_id, amount, currency, pay_type, effective_date):
        self.record_id      = record_id
        self.employee_id    = employee_id
        self.amount         = amount         # in cents
        self.currency       = currency
        self.pay_type       = pay_type       # "annual" or "hourly"
        self.effective_date = effective_date # "YYYY-MM-DD"
        self.status         = "PENDING"      # PENDING -> ACTIVE once date passes

class AuditEvent(object):
    def __init__(self, actor, action, record_id, old_value=None, new_value=None):
        self.actor     = actor
        self.action    = action    # CREATE / UPDATE / CANCEL
        self.record_id = record_id
        self.old_value = old_value
        self.new_value = new_value

# ── System ────────────────────────────────────────────────────

class HRCompensationSystem(object):
    def __init__(self):
        self.records       = {}  # employee_id -> [(effective_date, CompensationRecord)]
        self.date_index    = set() # set of (employee_id, effective_date) [O(1) conflict check]
        self.pending_index = {}  # record_id -> CompensationRecord (PENDING only)
        self.audit_log     = {}  # employee_id -> [AuditEvent]
        self._next_id      = 1

    def _new_id(self):
        rid = "rec_%04d" % self._next_id
        self._next_id += 1
        return rid

    def _audit(self, employee_id, actor, action, record_id, old_value=None, new_value=None):
        self.audit_log.setdefault(employee_id, []).append(
            AuditEvent(actor, action, record_id, old_value, new_value))

    # ── Create ───────────────────────────────────────────────

    def create_change(self, employee_id, amount, currency, pay_type, effective_date, actor):
        # O(1) conflict check: same employee cannot have two records on same date
        if (employee_id, effective_date) in self.date_index:
            raise ValueError("Conflict: record already exists for %s on %s"
                             % (employee_id, effective_date))
        record = CompensationRecord(
            self._new_id(), employee_id, amount, currency, pay_type, effective_date)
        self.records.setdefault(employee_id, [])
        bisect.insort(self.records[employee_id], (effective_date, record))
        self.date_index.add((employee_id, effective_date))
        self.pending_index[record.record_id] = record
        self._audit(employee_id, actor, "CREATE", record.record_id, new_value=amount)
        return record.record_id

    # ── Update ───────────────────────────────────────────────

    def update_change(self, record_id, new_amount, actor):
        if record_id not in self.pending_index:
            raise ValueError("Cannot update: %s is not PENDING" % record_id)
        record = self.pending_index[record_id]
        old_amount = record.amount
        record.amount = new_amount
        self._audit(record.employee_id, actor, "UPDATE", record_id, old_amount, new_amount)

    # ── Cancel ───────────────────────────────────────────────

    def cancel_change(self, record_id, actor):
        if record_id not in self.pending_index:
            raise ValueError("Cannot cancel: %s is not PENDING" % record_id)
        record = self.pending_index.pop(record_id)
        self.records[record.employee_id].remove((record.effective_date, record))
        self.date_index.remove((record.employee_id, record.effective_date))
        self._audit(record.employee_id, actor, "CANCEL", record_id)

    # ── Query ────────────────────────────────────────────────

    def get_salary_on_date(self, employee_id, query_date):
        """Bisect: find last record with effective_date <= query_date. O(log N)."""
        timeline = self.records.get(employee_id, [])
        dates = [entry[0] for entry in timeline]
        idx = bisect.bisect_right(dates, query_date) - 1
        return timeline[idx][1] if idx >= 0 else None

    def get_history(self, employee_id):
        return [entry[1] for entry in self.records.get(employee_id, [])]


# ── Test ──────────────────────────────────────────────────────

sys = HRCompensationSystem()

# Baseline salary active from 2024-01-01
r1 = sys.create_change("emp_123", 10000000, "USD", "annual", "2024-01-01", "admin")
sys.pending_index[r1].status = "ACTIVE"  # simulate record already in effect

# Schedule future raise for 2025-07-01
r2 = sys.create_change("emp_123", 12000000, "USD", "annual", "2025-07-01", "admin")

rec = sys.get_salary_on_date("emp_123", "2025-06-30")
print "2025-06-30:", rec.amount  # 10000000

rec = sys.get_salary_on_date("emp_123", "2025-07-01")
print "2025-07-01:", rec.amount  # 12000000

sys.update_change(r2, 13000000, "admin")
print "After update:", sys.get_salary_on_date("emp_123", "2025-07-01").amount  # 13000000

sys.cancel_change(r2, "admin")
print "After cancel:", sys.get_salary_on_date("emp_123", "2025-07-01").amount  # 10000000

try:
    sys.create_change("emp_123", 99999, "USD", "annual", "2024-01-01", "admin")
except ValueError as e:
    print e

for event in sys.audit_log.get("emp_123", []):
    print "[%s] %s %s old=%s new=%s" % (
        event.actor, event.action, event.record_id, event.old_value, event.new_value)

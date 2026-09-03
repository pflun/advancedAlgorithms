# -*- coding: utf-8 -*-
# Rippling - Building an Expense Rules Engine
# Data-driven rules: Field + Operator + Value 三元组模型

import collections

class Operator(object):
    EQUALS       = "=="
    NOT_EQUALS   = "!="
    GREATER_THAN = ">"
    LESS_THAN    = "<"

class Condition(object):
    def __init__(self, field, operator, value):
        self.field    = field
        self.operator = operator
        self.value    = value

    def matches(self, expense):
        v = expense.get(self.field)
        if v is None:
            return False
        # 数值比较时统一 float
        if self.operator in (Operator.GREATER_THAN, Operator.LESS_THAN):
            v, target = float(v), float(self.value)
        else:
            target = self.value
        if self.operator == Operator.EQUALS:       return v == target
        if self.operator == Operator.NOT_EQUALS:   return v != target
        if self.operator == Operator.GREATER_THAN: return v > target
        if self.operator == Operator.LESS_THAN:    return v < target
        return False

class Rule(object):
    def __init__(self, rule_id, description, conditions):
        self.rule_id     = rule_id
        self.description = description
        self.conditions  = conditions  # AND 逻辑

    def is_violated_by(self, expense):
        return all(c.matches(expense) for c in self.conditions)

class Violation(object):
    def __init__(self, expense_id, rule_id, rule_description):
        self.expense_id       = expense_id
        self.rule_id          = rule_id
        self.rule_description = rule_description

def evaluate_rules(rules, expenses):
    # Per-transaction pass: each expense x each rule -> Violation if violated
    violations = []
    for expense in expenses:
        for rule in rules:
            if rule.is_violated_by(expense):
                violations.append(Violation(
                    expense.get("expense_id"), rule.rule_id, rule.description))
    return violations

# ── Group Rules ───────────────────────────────────────────────

class GroupRule(object):
    def __init__(self, rule_id, description, group_by, aggregate_field, threshold, filter_condition=None):
        self.rule_id          = rule_id
        self.description      = description
        self.group_by         = group_by          # 分组字段，如 "trip_id"
        self.aggregate_field  = aggregate_field   # 求和字段，如 "amount_usd"
        self.threshold        = threshold
        self.filter_condition = filter_condition  # 复用 Condition 做过滤

class GroupViolation(object):
    def __init__(self, group_id, rule_id, rule_description, actual_value, threshold, expense_ids):
        self.group_id         = group_id
        self.rule_id          = rule_id
        self.rule_description = rule_description
        self.actual_value     = actual_value
        self.threshold        = threshold
        self.expense_ids      = expense_ids

def evaluate_group_rules(group_rules, expenses):
    # Per-trip pass: group -> filter -> sum -> emit GroupViolation if over threshold
    violations = []
    for rule in group_rules:
        groups = collections.defaultdict(list)
        for e in expenses:
            groups[e.get(rule.group_by)].append(e)

        for group_id, group in groups.items():
            filtered = [e for e in group if rule.filter_condition.matches(e)] \
                       if rule.filter_condition else group
            total = sum(float(e.get(rule.aggregate_field, 0)) for e in filtered)
            if total > rule.threshold:
                violations.append(GroupViolation(
                    group_id, rule.rule_id, rule.description,
                    total, rule.threshold,
                    [e.get("expense_id") for e in filtered]))
    return violations

# ── Rules ─────────────────────────────────────────────────────

rules = [
    Rule("R001", "Restaurant expense cannot exceed $75", [
        Condition("vendor_type", Operator.EQUALS, "restaurant"),
        Condition("amount_usd", Operator.GREATER_THAN, 75)
    ]),
    Rule("R002", "No airfare expenses", [
        Condition("expense_type", Operator.EQUALS, "airfare")
    ]),
    Rule("R003", "No entertainment expenses", [
        Condition("expense_type", Operator.EQUALS, "entertainment")
    ]),
    Rule("R004", "No expense can exceed $250", [
        Condition("amount_usd", Operator.GREATER_THAN, 250)
    ]),
]

group_rules = [
    GroupRule("G001", "Trip total cannot exceed $2000",
              group_by="trip_id", aggregate_field="amount_usd", threshold=2000.0),
    GroupRule("G002", "Total meal expenses cannot exceed $200 per trip",
              group_by="trip_id", aggregate_field="amount_usd", threshold=200.0,
              filter_condition=Condition("expense_type", Operator.EQUALS, "meals")),
]

# ── Test ──────────────────────────────────────────────────────

expenses = [
    {"expense_id": "001", "trip_id": "001", "amount_usd": "49.99",  "expense_type": "supplies",     "vendor_type": "restaurant"},
    {"expense_id": "002", "trip_id": "001", "amount_usd": "125.00", "expense_type": "supplies",     "vendor_type": "retailer"},
    {"expense_id": "003", "trip_id": "002", "amount_usd": "153.00", "expense_type": "meals",        "vendor_type": "restaurant"},
    {"expense_id": "004", "trip_id": "002", "amount_usd": "1996.00","expense_type": "airfare",      "vendor_type": "transportation"},
    {"expense_id": "005", "trip_id": "002", "amount_usd": "34.68",  "expense_type": "meals",        "vendor_type": "restaurant"},
    {"expense_id": "006", "trip_id": "002", "amount_usd": "22.40",  "expense_type": "meals",        "vendor_type": "restaurant"},
    {"expense_id": "007", "trip_id": "003", "amount_usd": "59.50",  "expense_type": "entertainment","vendor_type": "theater"},
]

for v in evaluate_rules(rules, expenses):
    print "Expense %s: %s" % (v.expense_id, v.rule_description)

print "---"

for v in evaluate_group_rules(group_rules, expenses):
    print "Trip %s: %s (actual=%.2f)" % (v.group_id, v.rule_description, v.actual_value)

# -*- coding: utf-8 -*-
# Rippling - Logger OOD
# Pipeline: message -> handlers (in order) -> print if all return should_print=True
# Strategy pattern: each handler is an independent strategy object



# ── Base ──────────────────────────────────────────────────────

class LogHandler(object):
    def handle(self, message):
        # Returns (new_message, should_print)
        raise NotImplementedError

class Logger(object):
    def __init__(self, handlers):
        self.handlers = handlers  # ordered list of LogHandler

    def log(self, message):
        should_print = True
        for handler in self.handlers:
            message, ok = handler.handle(message)
            if not ok:
                should_print = False
        if should_print:
            print message
            return message
        return None

# ── Handlers ──────────────────────────────────────────────────

class RemoveStringHandler(LogHandler):
    def __init__(self, target):
        self.target = target

    def handle(self, message):
        return message.replace(self.target, ""), True

class TruncateHandler(LogHandler):
    def __init__(self, max_chars):
        if max_chars < 0:
            raise ValueError("max_chars cannot be negative")
        self.max_chars = max_chars

    def handle(self, message):
        return message[:self.max_chars], True

class CapitalizeHandler(LogHandler):
    def handle(self, message):
        return message.upper(), True  # upper()，不是 capitalize()！

class StoreHandler(LogHandler):
    def __init__(self):
        self.store = []  # 存储完整消息列表，不打印

    def handle(self, message):
        self.store.append(message)
        return message, False

    # Follow-up: search stored messages for keywords, return in original order without duplicates
    def search(self, keywords):
        result = []
        seen = set()
        for i, msg in enumerate(self.store):
            msg_lower = msg.lower()
            for kw in keywords:
                if kw.lower() in msg_lower and i not in seen:
                    seen.add(i)
                    result.append(msg)
                    break
        return result


# ── Tests ─────────────────────────────────────────────────────

# Example 1: Remove -> Truncate -> Capitalize -> print
logger1 = Logger([
    RemoveStringHandler("debug "),
    TruncateHandler(12),
    CapitalizeHandler(),
])
logger1.log("debug hello world from rippling")
# Remove:   "hello world from rippling"
# Truncate: "hello world "
# Upper:    "HELLO WORLD "

print "---"

# Example 2: Remove -> Capitalize -> Store (no print)
store = StoreHandler()
logger2 = Logger([
    RemoveStringHandler("[internal] "),
    CapitalizeHandler(),
    store,
])
logger2.log("[internal] payroll sync failed")
logger2.log("[internal] employee import completed")

print store.store
# ['PAYROLL SYNC FAILED', 'EMPLOYEE IMPORT COMPLETED']

print store.search(["payroll", "import"])
# ['PAYROLL SYNC FAILED', 'EMPLOYEE IMPORT COMPLETED']

print store.search(["payroll"])
# ['PAYROLL SYNC FAILED']

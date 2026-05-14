# -*- coding: utf-8 -*-
# implement一个session manager class，有start_session(session_id: str) -> None, get_allocation() -> Dict(str, set(str))两个function
# 例子是如果有三个server [s1, s2, s3], 再往里面分配session的时候要让他们保持balance，如 [8, 8, 8] 或者 [8, 8, 7]
# 任何一个server的session数和其他server的gap不能超过1
# min heap存(num_of_session, server_id) 这样就每次start新session的时候就可以把最少session的server拿出来加进去。
import heapq

class SessionManager:
    def __init__(self, server_ids):
        self.used = set()
        # {server_id => set(session_ids)}
        self.dic = {}
        # (num_of_session, server_id)
        self.heap = []
        heapq.heapify(self.heap)
        for server_id in server_ids:
            self.dic[server_id] = set()
            heapq.heappush(self.heap, (0, server_id))

    def startSession(self, session_id):
        if session_id in self.used:
            return False
        curr_num_of_session, curr_server_id = heapq.heappop(self.heap)
        self.dic[curr_server_id].add(session_id)
        heapq.heappush(self.heap, (curr_num_of_session + 1, curr_server_id))
        return None

    def getAllocation(self):
        return self.dic

test = SessionManager(['s1', 's2', 's3'])
print test.startSession(1)
print test.startSession(2)
print test.startSession(3)
print test.startSession(4)
print test.startSession(5)
print test.startSession(6)
print test.startSession(7)
print test.startSession(8)
print test.startSession(9)
print test.startSession(10)
print test.startSession(11)
print test.getAllocation()
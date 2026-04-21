# -*- coding: utf-8 -*-
# https://www.hack2hire.com/companies/pinterest/coding-questions/681bc4c3a73bd75b806cb98f/practice
# Problem
# You're managing a real-time leaderboard for an escape room game with n sequential rooms. Support registering participants,
# advancing them through rooms, counting how many are in each room, and retrieving the top k participants who have
# progressed the furthest (breaking ties by earliest arrival).
# Example
# Input:
# ["EscapeRoom", "registerParticipant", "registerParticipant", "registerParticipant", "registerParticipant",
#  "increment", "increment", "increment", "increment", "increment",
#  "countParticipantsInRoom", "countParticipantsInRoom", "countParticipantsInRoom", "countParticipantsInRoom", "getTopParticipants"]
# [[4, 4], ["P0"], ["P1"], ["P2"], ["P3"], ["P2"], ["P2"], ["P2"], ["P0"], ["P3"], [0], [1], [2], [3], [2]]
# Output:
# [null, null, null, null, null, true, true, true, true, true, 1, 2, 0, 1, ["P2", "P0"]]
# Explanation:
# After registration, all four players start in room P0.
# “P2” advances three times (to room P3). “P0” and “P3” each advance once (to room P1). “P1” stays in room P0.
# countParticipantsInRoom(0) → 1 (only “P1”).
# countParticipantsInRoom(1) → 2 (“P0” and “P3”).
# countParticipantsInRoom(2) → 0.
# countParticipantsInRoom(3) → 1 (only “P2”).
# getTopParticipants(2) → ["P2", "P0"]: “P2” is in room P3 (farthest), then “P0” and “P3” tie in room P1 but “P0” arrived earlier.
import heapq

class EscapeRoom(object):
    def __init__(self, numRooms, maxParticipants):
        self.numRooms = numRooms
        self.capacity = maxParticipants
        self.roomCount = [0] * numRooms
        self.timestamp = 0
        # {participantId => [room, timestamp]}
        self.state = {}
        # (-room, timestamp, participantId)
        self.heap = []

    def registerParticipant(self, participantId):
        if len(self.state) >= self.capacity or participantId in self.state:
            return
        ts = self.timestamp
        self.timestamp += 1
        self.state[participantId] = [0, ts]
        heapq.heappush(self.heap, (0, ts, participantId))
        self.roomCount[0] += 1

    def increment(self, participantId):
        curr_room, curr_ts = self.state.get(participantId)
        # Player at the end room
        if curr_room == self.numRooms - 1:
            return False
        self.roomCount[curr_room] -= 1
        new_room = curr_room + 1
        new_ts = self.timestamp
        self.timestamp += 1
        self.state[participantId] = [new_room, new_ts]
        self.roomCount[new_room] += 1
        heapq.heappush(self.heap,(-new_room, new_ts, participantId))
        return True

    def countParticipantsInRoom(self, room):
        return self.roomCount[room]

    def getTopParticipants(self, k):
        res = []
        tmp = []
        cnt = 0
        while self.heap and cnt < min(k, len(self.state)):
            curr = heapq.heappop(self.heap)
            player = self.state[curr[2]]
            # real updated record because same as player state
            # state存正的room, heap存负的room
            if player[0] == -curr[0] and player[1] == curr[1]:
                res.append(curr[2]) # participantId
                cnt += 1
                tmp.append(curr)
        for t in tmp:
            heapq.heappush(self.heap, t) # after use, push them back
        return res

test = EscapeRoom(4, 4)
print test.registerParticipant("P0")
print test.registerParticipant("P1")
print test.registerParticipant("P2")
print test.registerParticipant("P3")
print test.increment("P2")
print test.increment("P2")
print test.increment("P2")
print test.increment("P0")
print test.increment("P3")
print test.countParticipantsInRoom(0)
print test.countParticipantsInRoom(1)
print test.countParticipantsInRoom(2)
print test.countParticipantsInRoom(3)
print test.getTopParticipants(2)
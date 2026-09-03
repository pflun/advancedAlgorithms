# -*- coding: utf-8 -*-
# https://www.1point3acres.com/interview/problems/company/rippling/delivery-billing-system
import heapq

class DeliveryCost:
    def __init__(self):
        self.drivers = {}
        self.total_recorded = 0
        self.total_paid = 0
        self.unpaid_heap = []
        # for maxSimultaneousDriverInPast24Hours()
        self.all_deliveries = []

    def addDriver(self, driverId, hourlyRate):
        self.drivers[driverId] = hourlyRate

    def recordDelivery(self, driverId, startTime, endTime):
        rate = self.drivers[driverId]
        duration_hours = (endTime - startTime) / 3600.0
        cost = duration_hours * rate
        heapq.heappush(self.unpaid_heap, (endTime, cost))
        self.total_recorded += cost
        # maxSimultaneousDriverInPast24Hours()
        self.all_deliveries.append((startTime, endTime, driverId))

    def getTotalCost(self):
        return self.total_paid

    def pay_up_to(self, endTime):
        while self.unpaid_heap and self.unpaid_heap[0][0] <= endTime:
            _, cost = heapq.heappop(self.unpaid_heap)
            self.total_paid += cost

    # minMeetingRooms.py 扫描线
    def maxSimultaneousDriverInPast24Hours(self, now):
        window_start = now - 86400
        starts = []
        ends = []
        for start, end, driverId in self.all_deliveries:
            if end < window_start or start > now:
                continue
            starts.append(max(start, window_start))
            ends.append(min(end, now))

        if not starts:
            return 0

        starts.sort()
        ends.sort()

        i = 0
        j = 0
        curr = 0
        res = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                curr += 1
                res = max(res, curr)
                i += 1
            elif starts[i] > ends[j]:
                curr -= 1
                j += 1
            else:
                i += 1
                j += 1

        return res
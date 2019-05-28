class Solution(object):
    def canVisitAllRooms(self, rooms):
        self.visit = set()

        def helper(key, rooms):
            if key in self.visit:
                return
            else:
                self.visit.add(key)
                for k in rooms[key]:
                    helper(k, rooms)

        helper(0, rooms)

        return True if len(rooms) == len(self.visit) else False

test = Solution()
print test.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
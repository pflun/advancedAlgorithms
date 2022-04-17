# given 2 list of free times
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])

        i = 0
        j = 0
        while i < len(slots1) and j < len(slots2):
            intersectStart = max(slots1[i][0], slots2[j][0])
            intersectEnd = min(slots1[i][1], slots2[j][1])

            if intersectStart + duration <= intersectEnd:
                return [intersectStart, intersectStart + duration]
            elif slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
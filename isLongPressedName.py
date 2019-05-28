class Solution(object):
    def isLongPressedName(self, name, typed):
        if len(name) > len(typed):
            return False
        elif len(name) == len(typed):
            return True

        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i] != typed[j] and name[i - 1] == typed[j]:
                j += 1
            else:
                return False

        # Edge case, long press happen at the very last
        if i == len(name) and j < len(typed):
            while j < len(typed):
                if name[i - 1] == typed[j]:
                    j += 1
                else:
                    return False

        if i == len(name) and j == len(typed):
            return True
        else:
            return False

test = Solution()
print test.isLongPressedName("vtkgn","vttkgnn")
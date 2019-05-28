"""
# Employee info
"""
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        if len(employees) == 0 or id == None:
            return False

        self.importance = 0
        queue = []

        def bfs(id):
            queue.append((id))

            while queue:
                curr = queue.pop(0)
                self.importance += employees[curr - 1][1]
                for i in employees[curr - 1][2]:
                    queue.append(i)

        bfs(id)
        return self.importance

# Employee is an object not array!
class Solution2(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        sons = []
        if not employees:
            return 0
        for employee in employees:
            if employee.id == id or employee.id in sons:
                res += employee.importance
                sons += employee.subordinates
        return res

test = Solution()
print test.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
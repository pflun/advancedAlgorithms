class Solution(object):
    def fewestConnections(self, targetOrigin, targetDestination, flights):
        graph = {}
        for origin, destination in flights:
            if origin not in graph:
                graph[origin] = []
            graph[origin].append(destination)
        queue = [[targetOrigin, [targetOrigin]]]
        visited = set()
        while queue:
            curr = queue.pop(0)
            currCity = curr[0]
            currPath = curr[1]
            if currCity == targetDestination:
                return currPath
            visited.add(currCity)
            for nextCity in graph[currCity]:
                if nextCity not in visited:
                    currPath.append(nextCity)
                    queue.append([nextCity, currPath[:]])
                    currPath.pop()
        return False

test = Solution()
print test.fewestConnections('SZ', 'LA', [['SZ', 'NY'], ['NY', 'LA'], ['SZ', 'DC'], ['DC', 'WA'], ['WA', 'LA']])
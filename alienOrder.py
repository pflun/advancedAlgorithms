# BFS Topological sort
# https://www.youtube.com/watch?v=hWnvHiaXTsw
class Solution(object):
    def alienOrder2(self, words):
        # dic => set()
        self.graph = {}
        self.indegree = {}
        self.buildGraph(words)
        return self.bfs()

    def buildGraph(self, words):
        # build empty graph
        for w in words:
            for c in w:
                if c not in self.graph:
                    self.graph[c] = set()
                if c not in self.indegree:
                    self.indegree[c] = 0
        # fill graph, and add in indegree
        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]
            j = 0
            while j < len(first) and j < len(second):
                if first[j] != second[j]:
                    if second[j] not in self.graph[first[j]]:
                        self.graph[first[j]].add(second[j])
                        self.indegree[second[j]] = self.indegree.get(second[j], 0) + 1
                    break
                j += 1

    def bfs(self):
        res = ''
        queue = []
        for k, v in self.indegree.items():
            if v == 0:
                res += k
                queue.append(k)

        while queue:
            curr = queue.pop(0)
            for next in self.graph[curr]:
                self.indegree[next] -= 1
                if self.indegree[next] == 0:
                    queue.append(next)
                    res += next
        # any(indegree)
        for v in self.indegree.values():
            if v != 0:
                return ''
        return res

    def alienOrder(self, words):
        result, zero_in_degree_queue, in_degree, out_degree = [], [], {}, {}
        nodes = set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in xrange(1, len(words)):
            if len(words[i - 1]) > len(words[i]) and \
                    words[i - 1][:len(words[i])] == words[i]:
                return ""
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)

        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.pop(0)
            result.append(precedence)

            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)

                del out_degree[precedence]

        if out_degree:
            return ""

        return "".join(result)

        # Construct the graph.

    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in xrange(str_len):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = set()
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break


test = Solution()
print test.alienOrder2([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])
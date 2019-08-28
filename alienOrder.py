# BFS Topological sort
class Solution(object):
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
print test.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])
# -*- coding: utf-8 -*-
# Positional Inverted Index
# 文档 1: "apple banana apple"
# 文档 2: "banana apple"
# 建立出来的 Positional Index：
# * "apple" -> { doc1: [0, 2], doc2: [1] }
# * "banana" -> { doc1: [1], doc2: [0] }
# search(query)
# * 将 query 按空格拆分成目标单词数组，例如 ["key", "words", "here"]。
# * 短路优化：如果其中有任何一个词不在倒排索引的 Key 里，直接返回空列表（因为连单个词都没有，更不可能有整个短语）。
# * 找交集文档：先拿到所有包含第一个词的文档 ID 集合。
# * 位置对齐（核心逻辑）：
# * 遍历这些候选的文档 ID。
# * 针对一个特定的文档，我们拿出每个目标词在这个文档里的位置列表。
# * 我们需要找是否存在一个起始位置 p，使得：
# * 第一个词在位置 p
# * 第二个词在位置 p+1
# * 第三个词在位置 p+2... 以此类推。
# * 如果能找到哪怕一个匹配的起始位置，这个文档 ID 就是合格的。
# * 收集所有合格的文档 ID，排序后返回
from collections import defaultdict

class DocumentSearch:
    def __init__(self, documents):
        # 核心数据结构: word -> { doc_id : [position1, position2, ...] }
        # 在 Python 中可以用 defaultdict(lambda: defaultdict(list))
        self.index = defaultdict(lambda: defaultdict(list))
        
        for doc in documents:
            doc_id = doc['id']
            content = doc['content']
            
            # 按空格切分单词
            words = content.split()
            for pos, word in enumerate(words):
                # 记录单词在这个文档里的位置
                self.index[word][doc_id].append(pos)

    def search(self, query):
        query_words = query.split()
        if not query_words:
            return []
            
        first_word = query_words[0]
        # 如果第一个词都没出现过，直接返回空
        if first_word not in self.index:
            return []
            
        result_doc_ids = []
        
        # 候选文档 ID，也就是包含了查询中第一个词的所有文档
        candidate_doc_ids = self.index[first_word].keys()
        
        for doc_id in candidate_doc_ids:
            # 拿到第一个词在这个文档里所有的出现位置
            positions_of_first_word = self.index[first_word][doc_id]
            
            # 检查这些位置中，是否有一个能够串起后面的所有词
            found_match = False
            for p in positions_of_first_word:
                match_this_pos = True
                # 往后逐个检查剩下的词
                for i in range(1, len(query_words)):
                    next_word = query_words[i]
                    # 如果后续的词根本没在这个文档里，或者没出现在 p+i 的位置上
                    # 为了查询效率更高，可以将 self.index[next_word][doc_id] 转为 set, 
                    # 但在原文档较短时用 in 判断也是可行的。
                    if doc_id not in self.index[next_word] or (p + i) not in self.index[next_word][doc_id]:
                        match_this_pos = False
                        break
                
                # 如果顺着位置 p，把所有词都对上了！
                if match_this_pos:
                    found_match = True
                    break # 只要找到一次，这个文档就符合要求了，不用继续找其他位置了
            
            if found_match:
                result_doc_ids.append(doc_id)
                
        # 题目要求升序排列
        return sorted(result_doc_ids)

# --- 本地测试用例 ---
docs = [
    {"id": 3, "content": "apple banana orange apple"},
    {"id": 1, "content": "hello world this is a key words test"},
    {"id": 2, "content": "key is not words but apple is"},
    {"id": 4, "content": "apple key words are here"}
]

ds = DocumentSearch(docs)
print(ds.search("apple"))      # 期待输出: [2, 3, 4]
print(ds.search("key words"))  # 期待输出: [1, 4]
print(ds.search("words key"))  # 期待输出: []
print ds.index

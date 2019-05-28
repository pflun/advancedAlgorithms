# -*- coding: utf-8 -*-
# 给你一个字符序列, 最小分割这个序列使每个分割出来的子序列里的所有字符不在别的分割序列里出现，输出所有子序列的长度。
# [ababcbacadefegdehijhklij] 输出[9, 7, 8]。也就是这样分割[ababcbaca/defegde/hijhklij]

def segment(s):
    for i in range(1, len(s) - 1):
        front = s[:1]
        end = s[i:]
        if len(set(front).intersection(set(end))) == 0:
            return segment(front) + segment(end)
    return [s]

def seg_length(s):
    return [len(x) for x in segment(s)]

print seg_length('ababcbacadefegdehijhklij')
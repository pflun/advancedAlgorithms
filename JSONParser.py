# -*- coding: utf-8 -*-
class JSONParser:
    def __init__(self, s):
        self.s = s
        self.i = 0  # global pointer

    def parse(self):
        # 总控阀门：看当前字符是什么，就丢给对应的函数处理
        if self.i >= len(self.s):
            return None
            
        char = self.s[self.i]
        if char == '"':
            return self.parse_string()
        elif char == '{':
            return self.parse_object()
        elif char == '[':
            return self.parse_array()

    def parse_string(self):
        self.i += 1  # 跳过开头的双引号 '"'
        start = self.i
        while self.s[self.i] != '"':
            self.i += 1
        res = self.s[start:self.i]
        self.i += 1  # 跳过结尾的双引号 '"'
        return res

    def parse_object(self):
        self.i += 1  # 跳过 '{'
        obj = {}
        
        # 处理空对象 "{}"
        if self.s[self.i] == '}':
            self.i += 1
            return obj
            
        while True:
            # 1. 提取 Key (必定是字符串)
            key = self.parse_string()
            
            # 2. 跳过冒号 ':'
            self.i += 1 
            
            # 3. 提取 Value (可能是 string/object/array，直接递归丢给 parse!)
            val = self.parse()
            obj[key] = val
            
            # 4. 判断接下来是逗号还是结束符
            if self.s[self.i] == ',':
                self.i += 1
                continue
            # exit after reached '}'
            elif self.s[self.i] == '}':
                self.i += 1
                return obj

    def parse_array(self):
        self.i += 1  # 跳过 '['
        arr = []
        
        # 处理空数组 "[]"
        if self.s[self.i] == ']':
            self.i += 1
            return arr
            
        while True:
            # 直接提取元素，类型未知，丢给 parse
            val = self.parse()
            arr.append(val)
            
            # 判断接下来是逗号还是结束符
            if self.s[self.i] == ',':
                self.i += 1
                continue
            # exit after reached ']'
            elif self.s[self.i] == ']':
                self.i += 1
                return arr

if __name__ == '__main__':
    s = '{"a":"hi","b":{"c":"Hello","d":["x","y",{"e":"Hi"}]}}'
    parser = JSONParser(s)
    print parser.parse()

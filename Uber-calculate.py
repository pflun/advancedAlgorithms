# -*- coding: utf-8 -*-
# "add(1,2)" -> 3
# "sub(3,1)" -> 2
# "add(1, sub(3,1))" -> 3
# "add(add(1,1), 2)" -> 4
class Solution(object):
    def calculate(self, s):
        stack = []
        for c in s:
            if c == " ":
                continue
                
            if c == ")":
                # 1. Pop everything until the matching '(' to get the arguments
                curr = ""
                while stack and stack[-1] != "(":
                    curr = stack.pop() + curr
                
                # Pop the '('
                stack.pop()
                
                # 2. Pop the function name ('add' or 'sub')
                func = ""
                # isalpha() ensures we only pop the letters of the function name
                while stack and stack[-1].isalpha():
                    func = stack.pop() + func
                
                # 3. Parse arguments and evaluate the sub-expression
                # `curr` will look like "1,2" or "1,-2"
                args = curr.split(",")
                val1 = int(args[0])
                val2 = int(args[1])
                
                if func == "add":
                    res = val1 + val2
                elif func == "sub":
                    res = val1 - val2
                    
                # 4. Push the evaluated result back to the stack as a string
                stack.append(str(res))
            else:
                # Push numbers, letters, commas, and '(' to the stack
                stack.append(c)
                
        # After processing all `)`, the stack will either have the final result 
        # as a single string, or a sequence of characters representing the number.
        ans = ""
        while stack:
            ans = stack.pop() + ans
            
        return int(ans)

test = Solution()
print test.calculate("add(1,2)")               # Output: 3
print test.calculate("sub(3,1)")               # Output: 2
print test.calculate("add(1, sub(3,1))")       # Output: 3
print test.calculate("add(add(1,1), 2)")       # Output: 4

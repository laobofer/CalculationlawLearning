# https://leetcode.cn/problems/valid-parentheses

class Solution:
    def is_right_pair(self, stack):
        if len(stack) < 2:
            return False
        
        left, right = stack[-1 -1], stack[-1]
        if (left, right) == ('(', ')'):
            return True
        elif (left, right) == ('{', '}'):
            return True
        elif (left, right) == ('[', ']'):
            return True
        
        return False

    def isValid(self, s: str) -> bool:
        stack = []

        for chr in s:
            stack.append(chr)
            if self.is_right_pair(stack):
                stack.pop()
                stack.pop()

        return not stack

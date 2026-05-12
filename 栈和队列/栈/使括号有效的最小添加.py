# https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for chr in s:
            if chr == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(chr)
            else:
                stack.append(chr)

        return len(stack)

print(Solution().minAddToMakeValid("()))"))
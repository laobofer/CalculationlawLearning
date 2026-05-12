# https://leetcode.cn/problems/evaluate-reverse-polish-notation

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from operator import add, sub, mul, truediv

        operator = {"+": add, "-": sub, "*": mul, "/": truediv}
        stack = []

        for token in tokens:
            if token in operator:
                nums2, nums1 = stack.pop(), stack.pop()
                stack.append(int(operator[token](int(nums1), int(nums2))))
            else:
                stack.append(int(token))

        return stack[0]
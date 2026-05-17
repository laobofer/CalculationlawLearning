# https://leetcode.cn/problems/lexicographical-numbers

from typing import List

class Solution:
    def __init__(self):
        self.res = []

    def traverse(self, i, n):
        if i > n:
            return

        self.res.append(i)

        for ii in range(0, 10):
            num = i * 10 + ii
            self.traverse(num, n)

    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1, 10):
            self.traverse(i, n)

        return self.res
    

print(Solution().lexicalOrder(13))
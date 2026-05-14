# https://leetcode.cn/problems/unique-binary-search-trees

class Solution:
    def __init__(self):
        self.memory = {}

    def numTrees(self, n: int) -> int:
        if n == 0:
            self.memory[0] = 1
            return 1

        num = 0
        for i in range(0, n):
            left = i
            right = n - i - 1
            left_num, right_num = -1, -1

            left_num = self.memory[left] if left in self.memory else self.numTrees(left)
            right_num = (
                self.memory[right] if right in self.memory else self.numTrees(right)
            )
            num += left_num * right_num

        self.memory[n] = num

        return num

# https://leetcode.cn/problems/path-in-zigzag-labelled-binary-tree

from typing import List

# 可以用数学方法优化

class Solution:
    def __init__(self):
        self.path = []
        self.res = []
        self.finded = False

    def traverse(self, root, depth, label):
        if root > label or self.finded:
            return

        self.path.append(root)
        if root == label:
            self.res = self.path.copy()
            self.finded = True

        # 当前层的范围
        start = 2 ** (depth - 1)
        end = 2**depth - 1
        # 下一层的范围
        next_start = 2**depth
        next_end = 2 ** (depth + 1) - 1

        if depth % 2 == 1:  # 奇数层：从左到右递增
            index = root - start
            left_idx = index * 2
            right_idx = index * 2 + 1
            left_child = next_end - left_idx
            right_child = next_end - right_idx
            self.traverse(right_child, depth + 1, label)
            self.traverse(left_child, depth + 1, label)
        else:  # 偶数层：从右向左递减
            index = end - root
            left_idx = index * 2
            right_idx = index * 2 + 1
            left_child = next_start + left_idx
            right_child = next_start + right_idx
            self.traverse(left_child, depth + 1, label)
            self.traverse(right_child, depth + 1, label)

        self.path.pop()

    def pathInZigZagTree(self, label: int) -> List[int]:
        self.traverse(1, 1, label)
        return self.res
    

print(Solution().pathInZigZagTree(26))
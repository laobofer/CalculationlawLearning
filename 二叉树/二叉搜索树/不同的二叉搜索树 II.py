# https://leetcode.cn/problems/unique-binary-search-trees-ii

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _generateTrees(self, lst):
        """使用递增的 lst 来建立一个 BST 并返回头结点列表"""
        if not lst:
            return [None]

        res = []

        for i in range(len(lst)):
            lefts = self._generateTrees(lst[0:i])
            rights = self._generateTrees(lst[i + 1 :])

            if not lefts and not rights:
                root = TreeNode(lst[i])
                root.left = None
                root.right = None
                res.append(root)
            elif not lefts and rights:
                for right in rights:
                    root = TreeNode(lst[i])
                    root.left = None
                    root.right = right
                    res.append(root)
            elif lefts and not rights:
                for left in lefts:
                    root = TreeNode(lst[i])
                    root.left = left
                    root.right = None
                    res.append(root)
            elif lefts and rights:
                for left in lefts:
                    for right in rights:
                        root = TreeNode(lst[i])
                        root.left = left
                        root.right = right
                        res.append(root)

        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self._generateTrees(list(range(1, n + 1)))


# 记忆化版本
class Solution2:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}  # 备忘录

        def generate(left, right):
            if left > right:
                return [None]

            # 如果已经计算过这个区间，直接返回结果
            if (left, right) in memo:
                return memo[(left, right)]

            res = []
            for i in range(left, right + 1):
                # 递归生成左右子树
                left_trees = generate(left, i - 1)
                right_trees = generate(i + 1, right)

                # 组合左右子树
                for left in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = r
                        res.append(root)

            memo[(left, right)] = res
            return res

        return generate(1, n)
# https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        from collections import defaultdict

        self.dict = defaultdict(list)

    def traverse(self, root, row, col):
        if root is None:
            return

        self.dict[(row, col)].append(root.val)

        self.traverse(root.left, row + 1, col - 1)
        self.traverse(root.right, row + 1, col + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict

        self.traverse(root, 0, 0)

        lst = [[key[0], key[1], vals] for key, vals in self.dict.items()]
        res_dict = defaultdict(list)
        res = []

        for row, col, vals in lst:
            for val in vals:
                res_dict[col].append([row, val])

        cols = list(sorted(res_dict.keys()))
        for col in cols:
            res_dict[col].sort(key=lambda x: x[1])
            res_dict[col].sort(key=lambda x: x[0])
            res.append([val for row, val in res_dict[col]])

        return res

        


# 优化顺序        
class Solution2:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        # 直接按列分组，每组存 (row, val) 元组
        col_map = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return
            # 每个节点直接放入对应列的列表中
            col_map[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        # 按列从小到大处理
        for col in sorted(col_map.keys()):
            # 对当前列的所有节点排序：先按行，行相同再按值
            col_map[col].sort(key=lambda x: (x[0], x[1]))
            # 提取排序后的值
            result.append([val for _, val in col_map[col]])

        return result
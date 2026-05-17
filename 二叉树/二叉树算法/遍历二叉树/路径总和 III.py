# https://leetcode.cn/problems/path-sum-iii

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 此题可以用前缀和优化, 这里也是区间内的和 == target
class Solution:
    def __init__(self):
        self.path = []
        self.count = 0

    def traverse(self, root, targetSum):
        if root is None:
            return
        
        self.path.append(root.val)

        for i in range(len(self.path) - 1, -1, -1):
            if sum(self.path[i: len(self.path)]) == targetSum:
                self.count += 1

        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)

        self.path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.traverse(root, targetSum)

        return self.count
    


class Solution2:
    def __init__(self):
        self.prefix = {0: 1}  # 前缀和 -> 出现次数
        self.count = 0

    def traverse(
        self, root: Optional[TreeNode], targetSum: int, cur_sum: int = 0
    ) -> None:
        if root is None:
            return

        # 当前路径和
        cur_sum += root.val

        # 如果 cur_sum - targetSum 在哈希表中，说明存在以当前节点结尾的有效路径
        self.count += self.prefix.get(cur_sum - targetSum, 0)

        # 将当前前缀和加入哈希表
        self.prefix[cur_sum] = self.prefix.get(cur_sum, 0) + 1

        # 递归左右子树
        self.traverse(root.left, targetSum, cur_sum)
        self.traverse(root.right, targetSum, cur_sum)

        # 回溯：离开当前节点时撤销前缀和计数
        self.prefix[cur_sum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.traverse(root, targetSum, 0)
        return self.count
    
class Solution3:
    def __init__(self):
        from collections import defaultdict

        self.dict = defaultdict(int)
        self.dict[0] = 1
        self.cur_sum = 0
        self.res = 0

    def traverse(self, root, targetSum):
        if root is None:
            return

        self.cur_sum += root.val
        if self.dict[self.cur_sum - targetSum] >= 1:
            self.res += 1

        self.dict[self.cur_sum] += 1

        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)

        self.dict[self.cur_sum] -= 1
        self.cur_sum -= root.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.traverse(root, targetSum)
        return self.res

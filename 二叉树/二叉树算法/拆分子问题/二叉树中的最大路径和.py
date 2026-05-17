# https://leetcode.cn/problems/binary-tree-maximum-path-sum

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            """
            l_max
            r_max
            a_max
            """
            if root is None:
                return -float("inf"), -float("inf"), -float('inf')
            
            ll_max, lr_max, la_max = helper(root.left)
            rl_max, rr_max, ra_max = helper(root.right)

            cur_a_max = max(
                root.val + ll_max,
                root.val + lr_max,
                root.val + rl_max,
                root.val + rr_max,
                la_max,
                ra_max,
                root.val + ll_max + rl_max,
                root.val + lr_max + rl_max,
                root.val + ll_max + rr_max,
                root.val + lr_max + rr_max,
                root.val,
            )
            cur_l_max = max(root.val + ll_max, root.val + lr_max, root.val)
            cur_r_max = max(root.val + rl_max, root.val + rr_max, root.val)

            return cur_l_max, cur_r_max, cur_a_max
        
        return max(helper(root))
    
# 这种方法涉嫌多次遍历, 但是思路好想
class Solution2:
    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 计算单边路径和时顺便计算最大路径和
        self.oneSideMax(root)
        return self.res

    # 定义：计算从根节点 root 为起点的最大单边路径和
    def oneSideMax(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_max_sum = max(0, self.oneSideMax(root.left))
        right_max_sum = max(0, self.oneSideMax(root.right))
        # 后序遍历位置，顺便更新最大路径和
        path_max_sum = root.val + left_max_sum + right_max_sum
        self.res = max(self.res, path_max_sum)
        # 实现函数定义，左右子树的最大单边路径和加上根节点的值
        # 就是从根节点 root 为起点的最大单边路径和
        return max(left_max_sum, right_max_sum) + root.val
    
# 第一种解法的优化
class Solution3:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                # 空树没有任何有效路径
                return float("-inf"), float("-inf")

            left_down, left_max = helper(node.left)
            right_down, right_max = helper(node.right)

            # 以当前节点为起点的最大向下路径和（选左、选右、或只选自己）
            current_down = max(node.val, node.val + left_down, node.val + right_down)

            # 以当前节点为最高点的路径和（连接左右向下路径）
            cross_sum = node.val
            if left_down != float("-inf"):
                cross_sum += left_down
            if right_down != float("-inf"):
                cross_sum += right_down

            # ✅ 修正：加入current_down，覆盖"只向一个方向延伸"的路径
            current_max = max(left_max, right_max, cross_sum, current_down)

            return current_down, current_max

        return helper(root)[1]
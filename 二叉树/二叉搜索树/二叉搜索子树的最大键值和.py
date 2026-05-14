# https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            """
            返回:
            所求的以 root 为根的二叉树的二叉搜索子树的最大键值和,
            以 root 为根的树是不是合法的 BST,
            当前子树的最大值
            当前子树的最小值
            当前子树的和
            """
            if root is None:
                return 0, True, -float("inf"), float("inf"), 0

            left_sum, left_vaild, max_l, min_l, cur_sum_l = helper(root.left)
            right_sum, right_vaild, max_r, min_r, cur_sum_r = helper(root.right)

            is_vaild = left_vaild and right_vaild and max_l < root.val < min_r

            root_sum = 0

            if is_vaild:
                root_sum = max(
                    left_sum,
                    right_sum,
                    cur_sum_l,
                    cur_sum_r,
                    cur_sum_l + cur_sum_r + root.val,
                )
            else:
                root_sum = max(left_sum, right_sum)

            return (
                root_sum,
                is_vaild,
                max(max_l, max_r, root.val),
                min(min_l, min_r, root.val),
                cur_sum_l + cur_sum_r + root.val,
            )

        res, _, _, _, _ = helper(root)
        return res
    



# 精简返回值：从 5 个减少到 4 个，移除了 "当前子树最大和" 的传递
# 全局最大值维护：仅在合法 BST 时更新，避免每个节点的max()计算
# 提前返回：不合法子树直接返回占位值，跳过 min/max 计算
# 消除函数调用：利用 BST 性质直接计算 min/max，替代min()/max()函数
# 局部常量：将无穷大定义为局部变量，减少重复创建开销
class Solution2:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        INF = float("inf")
        NINF = -INF
        max_sum = 0  # 初始化为0，天然处理全负数情况

        def post_order(node):
            nonlocal max_sum
            if not node:
                # 空节点：合法BST，最小值无穷大，最大值无穷小，和为0
                return (True, INF, NINF, 0)

            # 后序遍历：先处理左右子树
            left_valid, left_min, left_max, left_sum = post_order(node.left)
            right_valid, right_min, right_max, right_sum = post_order(node.right)

            # 只有左右都合法且满足BST性质时，当前子树才合法
            if left_valid and right_valid and left_max < node.val < right_min:
                current_sum = left_sum + right_sum + node.val
                # 仅在合法时更新全局最大值
                if current_sum > max_sum:
                    max_sum = current_sum
                # 利用BST性质直接计算min/max，避免函数调用
                current_min = left_min if node.left else node.val
                current_max = right_max if node.right else node.val
                return (True, current_min, current_max, current_sum)
            else:
                # 不合法子树返回占位值，父节点不会使用
                return (False, 0, 0, 0)

        post_order(root)
        return max_sum
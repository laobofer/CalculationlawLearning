# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        def helper(preorder, postorder):
            from collections import defaultdict

            if len(preorder) == 0:
                return None

            root_val = preorder[0]

            dict_pre = defaultdict(int)
            dict_post = defaultdict(int)

            index = 0

            for i in range(0, len(postorder) - 1):
                dict_pre[preorder[i + 1]] += 1
                dict_post[postorder[i]] += 1
                index += 1
                if all(dict_post[key] == val for key, val in dict_pre.items()):
                    break

            left = helper(preorder[1 : index + 1], postorder[0:index])
            right = helper(preorder[index + 1 :], postorder[index : len(postorder) - 1])

            root = TreeNode(root_val, left, right)

            return root

        return helper(preorder, postorder)

# 这种方法更好, 可以用哈希表直接得到分界的位置

# class Solution:
#     def constructFromPrePost(
#         self, preorder: List[int], postorder: List[int]
#     ) -> Optional[TreeNode]:
#         post_index = {val: idx for idx, val in enumerate(postorder)}
#         n = len(preorder)

#         def helper(
#             pre_start: int, pre_end: int, post_start: int, post_end: int
#         ) -> Optional[TreeNode]:
#             if pre_start > pre_end:
#                 return None

#             root_val = preorder[pre_start]
#             root = TreeNode(root_val)

#             if pre_start == pre_end:
#                 return root

#             left_root_val = preorder[pre_start + 1]
#             left_root_post_idx = post_index[left_root_val]

#             left_size = left_root_post_idx - post_start + 1

#             root.left = helper(
#                 pre_start + 1, pre_start + left_size, post_start, left_root_post_idx
#             )
#             root.right = helper(
#                 pre_start + left_size + 1, pre_end, left_root_post_idx + 1, post_end - 1
#             )

#             return root

#         return helper(0, n - 1, 0, n - 1)


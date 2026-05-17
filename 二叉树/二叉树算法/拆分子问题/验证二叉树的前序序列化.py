# https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")

        def helper(preorder):
            # 返回是否合规
            if not preorder:
                return False

            root_val = preorder.pop(0)

            if root_val == "#":
                return True

            left = helper(preorder)
            right = helper(preorder)

            return left and right

        return helper(preorder) and len(preorder) == 0

        
        
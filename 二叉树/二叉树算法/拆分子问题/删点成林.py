# https://leetcode.cn/problems/delete-nodes-and-return-forest

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete_set = set(to_delete)

        def helper(root, to_delete_set):
            """返回以root为根的子树中，所有无父节点的森林根节点列表（第一个元素是当前节点本身，若未被删除）"""
            if root is None:
                return []

            left_forest = helper(root.left, to_delete_set)
            right_forest = helper(root.right, to_delete_set)

            if root.val in to_delete_set:
                return left_forest + right_forest
            else:
                ret = []
                if root.left:
                    if root.left.val in to_delete_set:
                        root.left = None
                        ret += left_forest
                    else:
                        ret += left_forest[
                            1:
                        ] 
                if root.right:
                    if root.right.val in to_delete_set:
                        root.right = None
                        ret += right_forest
                    else:
                        ret += right_forest[
                            1:
                        ]
                return [root] + ret

        return helper(root, to_delete_set)
    

class Solution2:
    def __init__(self):
        self.delSet = set()
        # 记录森林的根节点
        self.res = []

    def delNodes(self, root, to_delete):
        if root is None:
            return []
        for d in to_delete:
            self.delSet.add(d)
        self.doDelete(root, False)
        return self.res

    # 定义：输入一棵二叉树，删除 delSet 中的节点，返回删除完成后的根节点
    def doDelete(self, root, hasParent):
        if root is None:
            return None
        # 判断是否需要被删除
        deleted = root.val in self.delSet
        if not deleted and not hasParent:
            # 没有父节点且不需要被删除，就是一个新的根节点
            self.res.append(root)
        # 去左右子树进行删除
        root.left = self.doDelete(root.left, not deleted)
        root.right = self.doDelete(root.right, not deleted)
        # 如果需要被删除，返回 null 给父节点
        return None if deleted else root
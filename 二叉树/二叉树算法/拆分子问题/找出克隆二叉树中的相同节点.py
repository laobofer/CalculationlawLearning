# https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = None
        self.found = False

    def traverse(self, root1, root2, target):
        if root1 is None or self.found:
            return
        
        if root1 is target:
            self.res = root2
            self.found = True
            return
        
        self.traverse(root1.left, root2.left, target)
        self.traverse(root1.right, root2.right, target)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.traverse(original, cloned, target)

        return self.res

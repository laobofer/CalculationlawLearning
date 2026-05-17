# https://leetcode.cn/problems/complete-binary-tree-inserter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: TreeNode):
        from collections import deque
        self.q = deque()
        self.root = root
        temp = deque()
        temp.append(root)
        while not temp:
            cur = temp.popleft()
            if cur.left is not None:
                temp.append(cur.left)
            if cur.right is not None:
                temp.append(cur.right)
            if cur.right is None or cur.left is None:
                self.q.append(cur)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        cur = self.q.queue[0]
        if cur.left is None:
            cur.left = node
        else:
            cur.right = node
            self.q.popleft()
        self.q.append(node)
        return cur.val

    def get_root(self) -> TreeNode:
        return self.root

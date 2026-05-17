# https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree

from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # 先构建邻接表
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def helper(root, parent):
            """返回: 从当前节点为根的子树上有没有苹果, 拿到所有苹果需要多少步数"""
            has = hasApple[root]
            _sum = 0

            for child in adj[root]:
                if child == parent:
                    continue
                child_has, child_sum = helper(child, root)
                if child_has:
                    has = True
                    _sum += child_sum + 2

            return has, _sum

        _, res = helper(0, -1)
        return res
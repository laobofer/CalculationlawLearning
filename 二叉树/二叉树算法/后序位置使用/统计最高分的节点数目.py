# https://leetcode.cn/problems/count-nodes-with-the-highest-score

from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        from collections import defaultdict

        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            parent = parents[i]
            children[parent].append(i)

        max_product = defaultdict(int)

        def helper(root):
            """返回以root为根的子树大小, 同时计算当前节点的分数"""
            child_list = children[root]
            subtree_sizes = []

            for child in child_list:
                subtree_sizes.append(helper(child))

            score = 1
            for size in subtree_sizes:
                score *= size
            parent_part = n - 1 - sum(subtree_sizes)
            if parent_part > 0:
                score *= parent_part

            max_product[score] += 1

            return 1 + sum(subtree_sizes)

        helper(0)

        max_score = max(max_product.keys())
        return max_product[max_score]
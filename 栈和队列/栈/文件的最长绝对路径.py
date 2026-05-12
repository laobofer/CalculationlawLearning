# https://leetcode.cn/problems/longest-absolute-file-path

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_len = 0
        for line in input.split("\n"):
            depth = 0
            while depth < len(line) and line[depth] == "\t":
                depth += 1
            name = line[depth:]
            while len(stack) > depth:
                stack.pop()
            parent_len = stack[-1] if stack else 0
            cur_len = parent_len + (1 if parent_len > 0 else 0) + len(name)
            if "." in name:
                max_len = max(max_len, cur_len)
            else:
                stack.append(cur_len)
        return max_len
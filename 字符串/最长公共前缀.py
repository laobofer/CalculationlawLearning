# https://leetcode.cn/problems/longest-common-prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = []

        j = 0
        min_ = min(strs, key=len)
        min_len = len(min_)

        if min_ == "":
            return ""

        val = min_[0]

        for _ in range(min_len):
            for i in range(len(strs)):
                if strs[i][j] != val:
                    return "".join(ret)

                if i == len(strs) - 1:
                    j = j + 1
                    ret.append(val)
                    if j >= min_len:
                        break
                    val = strs[0][j]

        return "".join(ret)
# https://leetcode.cn/problems/number-of-matching-subsequences

from typing import List

class Solution:
    def bi_search(self, indexs, index_target):
        left, right = 0, len(indexs) - 1

        while left <= right:
            mid = left + (right - left) // 2
            index = indexs[mid]

            if index < index_target:
                left = mid + 1
            elif index == index_target:
                right = mid - 1
            elif index > index_target:
                right = mid - 1
        
        return left if left != len(indexs) else -1

    def match_one_word(self, word, chr_dict):
        index = 0
        for chr in word:
            if not chr_dict[chr]:
                return False
            
            pos = self.bi_search(chr_dict[chr], index)
            if pos == -1:
                return False
            
            index = chr_dict[chr][pos] + 1
            
        return True


    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        chr_dict = defaultdict(list)

        for index, chr in enumerate(s):
            chr_dict[chr].append(index)
        
        res = 0
        for word in words:
            res += 1 if self.match_one_word(word, chr_dict) else 0

        return res


        



print(Solution().numMatchingSubseq("abcde", ["bb"]))
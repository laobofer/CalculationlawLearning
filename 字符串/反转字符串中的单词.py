# https://leetcode.cn/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        lst = s.split()
        lst.reverse()
        return ' '.join(lst)

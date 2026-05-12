# https://leetcode.cn/problems/valid-palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_ = list(s.lower())
        new_s = [chr for chr in str_ if chr.isalnum()]
        left, right = 0, len(new_s) - 1

        while left <= right:
            if new_s[left] != new_s[right]:
                return False

            left += 1
            right -= 1

        return True

# https://leetcode.cn/problems/remove-k-digits


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for chr in num:
            while stack and k > 0 and stack[-1] > chr:
                stack.pop()
                k -= 1

            stack.append(chr)

        res = stack

        if k != 0:
            res = stack[:-k]

        res = ''.join(res).lstrip('0')

        if not res:
            res = '0'

        return res
        



# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         stack = []
#         index_to_remove = set()
#         k_copy = k

#         for i, digit_char in enumerate(num):
#             digit_int = int(digit_char)
#             while stack and k_copy > 0 and stack[-1][0] > digit_int:
#                 index_to_remove.add(stack.pop()[1])
#                 k_copy -= 1
#             stack.append((digit_int, i))

#         while k_copy > 0:
#             if stack:
#                 index_to_remove.add(stack.pop()[1])
#                 k_copy -= 1

#         res = []
#         for i, ch in enumerate(num):
#             if i in index_to_remove:
#                 continue
#             if not res and ch == "0":
#                 continue
#             res.append(ch)

#         return "".join(res) if res else "0"

print(Solution().removeKdigits("9", 1))

# https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string

class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        res = 0

        i = 0
        while i < len(s):
            chr = s[i]

            if chr == "(":
                stack.append(chr)
                i += 1
            elif chr == ")":
                if i + 1 < len(s) and s[i + 1] == ")":
                    if stack:
                        stack.pop()
                    else:
                        res += 1

                    i += 2
                else:
                    if stack:
                        stack.pop()
                        res += 1
                    else:
                        res += 2

                    i += 1

        return res + 2 * len(stack)
    
# class Solution:
#     def minInsertions(self, s: str) -> int:
#         need = 0   # 还需要多少个右括号
#         ans = 0    # 已经插入的括号数

#         for ch in s:
#             if ch == '(':
#                 # 遇到左括号，需求增加 2
#                 # 但如果当前 need 是奇数，说明有单独的 ')' 需要补 '('
#                 if need % 2 == 1:
#                     ans += 1      # 插入一个 '('
#                     need -= 1     # 消耗掉一个右括号需求
#                 need += 2
#             else:  # ch == ')'
#                 need -= 1
#                 if need < 0:
#                     # 右括号过多，插入一个 '('
#                     ans += 1
#                     need = 1      # 新插入的 '(' 还需 1 个 ')'
        
#         return ans + need


print(Solution().minInsertions("((())))"))
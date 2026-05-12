# https://leetcode.cn/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for chr in s:
            if chr == ']':
                index = len(stack) - 1
                while stack[index] != '[':
                    index -= 1

                i = index - 1
                print(1, i, index, stack[index])
                k = 0
                while i > 0 and stack[i].isnumeric():
                    k += int(stack[i]) * 10 ** (index - i - 1)
                    i -= 1

                stack[i:] = stack[index + 1:] * int(k)
            else:
                stack.append(chr)

        return ''.join(stack)
    
print(Solution().decodeString('3[a]2[bc]'))
# https://leetcode.cn/problems/simplify-path


class Solution:
    def simplifyPath(self, path: str) -> str:
        filepaths = path.split('/')
        stack = []
        res = []

        for filepath in filepaths:
            if filepath == '..':
                if stack:
                    stack.pop()
            elif filepath == '.' or filepath == '':
                continue
            else:
                stack.append(filepath)
        
        for e in stack:
            res.append('/')
            res.extend(e)

        if not res:
            res.append('/')

        return ''.join(res)


# 效率低
# class Solution:
#     def is_one_dot(self, stack):
#         if len(stack) == 1 and stack[0] == '.':
#             return True
#         return False
    
#     def is_two_dot(self, stack):
#         if len(stack) == 2 and stack[0] == '.' and stack[1] == '.':
#             return True
#         return False

#     def simplifyPath(self, path: str) -> str:
#         # 这里先默认: 第一个字符都是 /
#         stack = []
#         filepaths = []
#         res = []

#         for chr in path:
#             if chr == '/':
#                 if self.is_one_dot(stack):
#                     stack.clear()
#                     continue
#                 elif self.is_two_dot(stack) and filepaths:
#                     filepaths.pop()
#                     stack.clear()
#                 elif self.is_two_dot(stack):
#                     stack.clear()
#                 elif stack:
#                     filepaths.append(''.join(stack))
#                     stack.clear()
#             else:
#                 stack.append(chr)

#         if stack:
#             if self.is_one_dot(stack):
#                 stack.clear()
#             elif self.is_two_dot(stack) and filepaths:
#                 filepaths.pop()
#             elif self.is_two_dot(stack):
#                 stack.clear()
#             else:
#                 filepaths.append("".join(stack))
#                 stack.clear()

#         for filepath in filepaths:
#             res.append('/')
#             res.extend(list(filepath))

#         if not res:
#             res.append('/')

#         return ''.join(res)


print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
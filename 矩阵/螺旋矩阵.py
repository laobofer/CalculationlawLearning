# https://leetcode.cn/problems/spiral-matrix

from typing import List

class Solution:
    def move(self, i, j, direction, limit):
        if j == limit[1] and direction == [0, 1]:
            direction[:] = [1, 0]
            limit[1] -= 1
            # 向右
        elif i == limit[0] and direction == [-1, 0]:
            direction[:] = [0, 1]
            limit[0] += 1
            # 向上
        elif i == limit[2] and direction == [1, 0]:
            direction[:] = [0, -1]
            limit[2] -= 1
            # 向下
        elif j == limit[3] and direction == [0, -1]:
            direction[:] = [-1, 0]
            limit[3] += 1
            # 向左
        
        i += direction[0]
        j += direction[1]


        return i, j

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, right, down, left = 1, len(matrix[0]) - 1, len(matrix) - 1, 0
        limit = [up, right, down, left]
        ret = []
        
        i, j = 0, -1
        direction = [0, 1]
        for _ in range(len(matrix[0])*len(matrix)):
            i, j = self.move(i, j, direction, limit)
            ret.append(matrix[i][j])

        return ret
    
s = Solution()
s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []
#         res = []
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1

#         while True:
#             # 右
#             for j in range(left, right + 1):
#                 res.append(matrix[top][j])
#             top += 1
#             if top > bottom:
#                 break

#             # 下
#             for i in range(top, bottom + 1):
#                 res.append(matrix[i][right])
#             right -= 1
#             if left > right:
#                 break

#             # 左
#             for j in range(right, left - 1, -1):
#                 res.append(matrix[bottom][j])
#             bottom -= 1
#             if top > bottom:
#                 break

#             # 上
#             for i in range(bottom, top - 1, -1):
#                 res.append(matrix[i][left])
#             left += 1
#             if left > right:
#                 break

#         return res
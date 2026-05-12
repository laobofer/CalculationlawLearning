# https://leetcode.cn/problems/rotate-image

from typing import List

class Solution:
    def get_v(self, i, j, mid):
        return i - mid, j - mid
    
    def rotate_v(self, x, y):
        return y, -x
    
    def get_index(self, x, y, mid):
        return int(x + mid), int(y + mid)
    
    def rotate_(self, matrix, i1_0, i1_1, i2_0, i2_1, i3_0, i3_1, i4_0, i4_1):
        (
            matrix[i1_0][i1_1],
            matrix[i2_0][i2_1],
            matrix[i3_0][i3_1],
            matrix[i4_0][i4_1],
        ) = (
            matrix[i4_0][i4_1],
            matrix[i1_0][i1_1],
            matrix[i2_0][i2_1],
            matrix[i3_0][i3_1],
        )
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mid = len(matrix[0]) // 2
        real_mid = (len(matrix[0]) - 1) / 2
        for i in range(mid):
            for j in range(mid):
                v1_0, v1_1 = self.get_v(i, j, real_mid)
                v2_0, v2_1 = self.rotate_v(v1_0, v1_1)
                v3_0, v3_1 = self.rotate_v(v2_0, v2_1)
                v4_0, v4_1 = self.rotate_v(v3_0, v3_1)
                i1_0, i1_1 = self.get_index(v1_0, v1_1, real_mid)
                i2_0, i2_1 = self.get_index(v2_0, v2_1, real_mid)
                i3_0, i3_1 = self.get_index(v3_0, v3_1, real_mid)
                i4_0, i4_1 = self.get_index(v4_0, v4_1, real_mid)
                self.rotate_(matrix, i1_0, i1_1, i2_0, i2_1, i3_0, i3_1, i4_0, i4_1)

        if len(matrix[0]) % 2 != 0:
            i = mid
            for j in range(mid):
                v1_0, v1_1 = self.get_v(i, j, real_mid)
                v2_0, v2_1 = self.rotate_v(v1_0, v1_1)
                v3_0, v3_1 = self.rotate_v(v2_0, v2_1)
                v4_0, v4_1 = self.rotate_v(v3_0, v3_1)
                i1_0, i1_1 = self.get_index(v1_0, v1_1, real_mid)
                i2_0, i2_1 = self.get_index(v2_0, v2_1, real_mid)
                i3_0, i3_1 = self.get_index(v3_0, v3_1, real_mid)
                i4_0, i4_1 = self.get_index(v4_0, v4_1, real_mid)
                self.rotate_(matrix, i1_0, i1_1, i2_0, i2_1, i3_0, i3_1, i4_0, i4_1)                

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)

#         # 只遍历左上角 1/4 区域，一圈一圈旋转
#         for i in range(n // 2):
#             for j in range((n + 1) // 2):
#                 # 四个点坐标（纯整数！完全不用浮点数）
#                 a = i, j
#                 b = j, n - 1 - i
#                 c = n - 1 - i, n - 1 - j
#                 d = n - 1 - j, i

#                 # 原地交换
#                 (
#                     matrix[a[0]][a[1]],
#                     matrix[b[0]][b[1]],
#                     matrix[c[0]][c[1]],
#                     matrix[d[0]][d[1]],
#                 ) = (
#                     matrix[d[0]][d[1]],
#                     matrix[a[0]][a[1]],
#                     matrix[b[0]][b[1]],
#                     matrix[c[0]][c[1]],
#                 )

                

                
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2], [3, 4]]
s = Solution()
s.rotate(matrix)
s.rotate(matrix2)
print(matrix)
print(matrix2)
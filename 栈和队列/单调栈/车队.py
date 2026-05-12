# https://leetcode.cn/problems/car-fleet

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zip_lst = list(zip(position, speed))
        zip_lst.sort(key=lambda x: x[0])
        times = [(target - position) // speed for position, speed in zip_lst]

        stack = []
        n = len(times)

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= times[i]:
                stack.pop()

            stack.append(times[i])

        return len(stack)

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         zip_lst = list(zip(position, speed))
#         zip_lst.sort(key=lambda x: x[0])
#         times = [(target - position) // speed for position, speed in zip_lst]

#         stack = []

#         for time in times:
#             while stack and time >= stack[-1]:
#                 stack.pop()
#             stack.append(time)
#         return len(stack)
    

print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
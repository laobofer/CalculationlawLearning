# 双指针算法

## 适用场景

双指针是处理 **有序数组 / 链表** 问题的高效技巧，能将许多 O(n²) 暴力解优化到 O(n)。当你遇到以下特征时应当考虑双指针：

- **N 数之和问题**：在有序数组中查找两个/三个/四个数满足某个和——排序后用左右指针向中间收窄
- **有序数组的去重与原地修改**：删除重复项、移除指定元素、移动零——用快慢指针维护「已处理区」和「待探索区」
- **两个有序序列的归并**：合并两个有序数组、找两个有序数组的中位数——用归并指针
- **数组平方后排序**：有序数组可能含负数，平方后最大值在两端——左右指针从两端向中间扫描
- **分割/分类问题**：如荷兰国旗（颜色分类），需要将数组按值分成多个区域——三指针
- **隐式链表判环**：如寻找重复数，用快慢指针在索引映射的隐式链表上做 Floyd 判圈

> **选型速查**：需要两边找 → 左右指针；需要原地修改维护顺序 → 快慢指针；需要合并已排序数据 → 归并指针；需要数组三分 → 三指针。

## 核心模式

双指针主要分为三种形态：

| 形态 | 指针位置 | 典型场景 |
|------|---------|---------|
| 左右指针 | 两端向中间收窄 | N 数之和、有序数组平方、回文检测 |
| 快慢指针 | 同向不同速 | 原地去重、移除元素、移动零、判环、寻找重复数 |
| 归并指针 | 双序列从后向前 | 合并两个有序数组 |

---

## 目录
- [两数之和](#两数之和)
- [三数之和](#三数之和)
- [四数之和](#四数之和)
- [删除有序数组中的重复项](#删除有序数组中的重复项)
- [删除有序数组中的重复项 II](#删除有序数组中的重复项-ii)
- [合并两个有序数组](#合并两个有序数组)
- [有序数组的平方](#有序数组的平方)
- [移动零](#移动零)
- [移除元素](#移除元素)
- [颜色分类](#颜色分类)
- [寻找重复数](#寻找重复数)

---

## 两数之和

**LeetCode 1** | 难度：简单

### 题目描述

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案，且同一个元素不能使用两遍。可以按任意顺序返回答案。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [2,7,11,15], target = 9` | `[0,1]` | 2 + 7 = 9 |
| `nums = [3,2,4], target = 6` | `[1,2]` | 2 + 4 = 6 |
| `nums = [3,3], target = 6` | `[0,1]` | 两个 3 各用一次 |

### 思路

经典解是用哈希表 O(n)。但如果要求用双指针：先排序并记录原始下标，然后左右指针向中间收窄。和 > target 则右指针左移，和 < target 则左指针右移。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 哈希表 | 低 | O(n) | 首选 |
| 排序 + 双指针 | 低 | O(n log n) | 保留原下标麻烦 |
| 暴力 | 极低 | O(n²) | 不推荐 |

### Python 实现

```python
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表法（推荐）
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []
```

> 双指针法版本在代码文件中。考试中两数之和优先用哈希表——不仅仅是 O(n) 的问题，更是因为不用处理「保留原始下标」的麻烦。

---

## 三数之和

**LeetCode 15** | 难度：中等

### 题目描述

给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i、j、k 互不相同且 nums[i] + nums[j] + nums[k] == 0。请你返回所有和为 0 且不重复的三元组。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [-1,0,1,2,-1,-4]` | `[[-1,-1,2],[-1,0,1]]` | 去重后有两组解 |
| `nums = [0,1,1]` | `[]` | 不存在和为 0 的三元组 |
| `nums = [0,0,0]` | `[[0,0,0]]` | 只有一组解 |

### 思路

先排序，固定第一个数，然后在右侧用双指针找两数之和等于 `-nums[i]`。关键是**去重**：对固定的第一个数跳过重复值，双指针找到解后也要跳过重复的左右值。

整体是递归思想：N 数之和通过固定一个数，降级为 N-1 数之和。`nSumTarget` 的递归模板可以统一处理 2Sum、3Sum、4Sum 乃至更高的 N 数之和。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 排序 + 外层循环 + 内层双指针 | 中 | O(n²) | 首选 |
| 排序 + nSum 递归模板 | 中 | O(n^(N-1)) | 推荐，统一代码 |
| 哈希表 + 去重 | 高 | O(n²) | 去重逻辑复杂 |

### Python 实现

```python
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                cur_sum = nums[left] + nums[right]

                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的左右值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
```

> 更通用的方案是 `n_sum_target(nums, n, start, target)` 递归，可覆盖任意 N 数之和。代码文件中已有实现。

---

## 四数之和

**LeetCode 18** | 难度：中等

### 题目描述

给你一个由 n 个整数组成的数组 nums 和一个目标值 target，找出所有不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]，满足四个元素之和等于 target。要求 a、b、c、d 互不相同，返回所有不重复的四元组。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,0,-1,0,-2,2], target = 0` | `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]` | 三组不重复的解 |
| `nums = [2,2,2,2,2], target = 8` | `[[2,2,2,2]]` | 全部元素相等 |

### 思路

和三数之和完全相同的套路：排序后外层固定一个数，内层递归调用三数之和。去重的处理方式和三数之和一致——每层跳过相同的已处理值。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 递归 nSum 模板 | 中 | O(n³) | 首选，写一次覆盖所有 N-Sum |
| 双层循环 + 双指针 | 中 | O(n³) | 也可以 |
| 哈希表 | 高 | O(n²) 平均 | 代码复杂 |

### Python 实现

```python
from typing import List


class Solution:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self._n_sum_target(nums, 4, 0, target)

    def _n_sum_target(
        self, nums: List[int], n: int, start: int, target: int
    ) -> List[List[int]]:
        result = []
        length = len(nums)

        if n < 2 or length < n:
            return result

        if n == 2:
            # 两数之和双指针
            left, right = start, length - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        else:
            for i in range(start, length):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub_results = self._n_sum_target(
                    nums, n - 1, i + 1, target - nums[i]
                )
                for sub in sub_results:
                    sub.append(nums[i])
                    result.append(sub)

        return result
```

> 掌握 `_n_sum_target` 递归模板一劳永逸。考试中也可以只写到 4Sum，代码量差别不大。

---

## 删除有序数组中的重复项

**LeetCode 26** | 难度：简单

### 题目描述

给你一个非严格递增排列的数组 nums，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。要求原地修改输入数组，不得使用额外的数组空间，仅使用 O(1) 额外空间。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,1,2]` | `2, nums = [1,2,_]` | 前两个元素被修改为 1, 2 |
| `nums = [0,0,1,1,1,2,2,3,3,4]` | `5, nums = [0,1,2,3,4,_,_,_,_,_]` | 保留 5 个不重复元素 |

### 思路

快慢指针：`slow` 指向下一个不重复元素应该放的位置，`fast` 在前面探路。当 `nums[fast] != nums[fast - 1]`（遇到新元素）时，复制到 `slow` 位置。

### Python 实现

```python
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
```

> 与 `移除元素` 的模板完全一致，只是判断条件从 `nums[fast] != val` 变为 `nums[fast] != nums[fast-1]`。

---

## 删除有序数组中的重复项 II

**LeetCode 80** | 难度：中等

### 题目描述

给定一个有序数组 nums，原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。必须在原地修改输入数组，并只使用 O(1) 额外空间。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,1,1,2,2,3]` | `5, nums = [1,1,2,2,3,_]` | 保留 5 个元素，每个最多两次 |
| `nums = [0,0,1,1,1,1,2,3,3]` | `7, nums = [0,0,1,1,2,3,3,_,_]` | 保留 7 个元素 |

### 思路

与上一题类似，但允许每个元素最多出现两次。快慢指针 + 计数器：维护 `count` 记录当前元素出现了几次。`count < 2` 时可以保留。

更简洁的写法：由于数组有序，直接判断 `nums[fast] != nums[slow - 2]`，只要当前元素不等于 slow 前两格的值，就可以放入。

### Python 实现

```python
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
```

> `nums[fast] != nums[slow - 2]` 是关键：因为有序，只要当前值和两格前的保留值不同，说明它最多只出现了两次。

---

## 合并两个有序数组

**LeetCode 88** | 难度：简单

### 题目描述

给你两个按非递减顺序排列的整数数组 nums1 和 nums2，以及它们的有效元素个数 m 和 n。请将 nums2 合并到 nums1 中，使合并后的数组同样按非递减顺序排列。nums1 的长度为 m + n，前 m 个元素是有效元素，后 n 个元素为 0 占位。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3` | `[1,2,2,3,5,6]` | 合并两个有序数组 |
| `nums1 = [1], m = 1, nums2 = [], n = 0` | `[1]` | nums2 为空，nums1 不变 |
| `nums1 = [0], m = 0, nums2 = [1], n = 1` | `[1]` | nums1 为空，直接填入 nums2 |

### 思路

**从后向前归并**。`nums1` 末尾有空位，从大往小填入避免覆盖未处理的元素。三指针：`p1` 指向 nums1 有效元素末尾，`p2` 指向 nums2 末尾，`p` 指向合并后位置。

### Python 实现

```python
from typing import List


class Solution:
    def merge(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        p1, p2 = m - 1, n - 1
        tail = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
```

> 关键：从后向前填。如果从前向后，需要额外空间或大量移动元素。

---

## 有序数组的平方

**LeetCode 977** | 难度：简单

### 题目描述

给你一个按非递减顺序排序的整数数组 nums，返回每个数字的平方组成的新数组，也要求按非递减顺序排序。数组中可能包含负数，平方后原有顺序会被打破，需要重新排序。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [-4,-1,0,3,10]` | `[0,1,9,16,100]` | 平方后升序排列 |
| `nums = [-7,-3,2,3,11]` | `[4,9,9,49,121]` | 含重复平方值 |

### 思路

左右指针：原数组有序可能包含负数，平方后最大值一定在两端（最左的负数平方或最右的正数平方）。用两个指针从两端向中间扫描，较大的平方值从结果数组末尾向前填充。

### Python 实现

```python
from typing import List


class Solution:
    def sorted_squares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq >= right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1

        return result
```

---

## 移动零

**LeetCode 283** | 难度：简单

### 题目描述

给定一个数组 nums，编写函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。必须原地操作，不能复制数组，尽量减少操作次数。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [0,1,0,3,12]` | `[1,3,12,0,0]` | 非零元素保持原有顺序 |
| `nums = [0]` | `[0]` | 单元素无需操作 |

### 思路

快慢指针：`fast` 遍历数组，遇到非零元素就和 `slow` 交换，`slow` 始终指向「已处理好的非零段」的下一个位置。

效果等价于将所有非零元素「挤」到前面，零自动被交换到后面。

### Python 实现

```python
from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
```

> 交换而非覆盖：使用交换可以一次性将零移到后面，`slow` 前面的元素都保持相对顺序。

---

## 移除元素

**LeetCode 27** | 难度：简单

### 题目描述

给你一个数组 nums 和一个值 val，需要原地移除所有数值等于 val 的元素，并返回移除后数组的新长度。元素的顺序可以改变，不需要考虑数组中超出新长度后面的元素。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [3,2,2,3], val = 3` | `2, nums = [2,2,_,_]` | 移除两个 3 |
| `nums = [0,1,2,2,3,0,4,2], val = 2` | `5, nums = [0,1,3,0,4,_,_,_]` | 移除三个 2 |

### 思路

快慢指针模板：`fast` 遍历，遇到不等于 `val` 的元素就复制到 `slow` 并右移 `slow`。`slow` 同时表示新数组的长度。

### Python 实现

```python
from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow
```

> 这是「原地移除」系列的最基本模板，几乎所有同类题（去重、移动零）都源于此。

---

## 颜色分类

**LeetCode 75** | 难度：中等

### 题目描述

给定一个包含红色、白色和蓝色的数组 nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色(0)、白色(1)、蓝色(2)的顺序排列。要求不使用库排序函数，且只使用常数空间的一次扫描完成。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [2,0,2,1,1,0]` | `[0,0,1,1,2,2]` | 红色(0)、白色(1)、蓝色(2) |
| `nums = [2,0,1]` | `[0,1,2]` | 三种颜色各一个 |

### 思路

荷兰国旗问题。三指针：`left` 左侧全是 0，`right` 右侧全是 2，`cur` 扫描当前元素。
- 遇 0：与 `left` 交换，`left++`，`cur++`
- 遇 1：`cur++`
- 遇 2：与 `right` 交换，`right--`（不移动 `cur`，因为换过来的元素未检查）

原代码用计数排序（两遍扫描）也能 AC，但三指针一次扫描是面试标准答案。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 三指针荷兰国旗 | 中 | O(n) 时间 O(1) 空间，一遍扫描 | 首选 |
| 计数排序 | 低 | O(n) 时间 O(1) 空间，两遍扫描 | 可 AC 但不是最优 |

### Python 实现

```python
from typing import List


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        cur = 0

        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
                # cur 不移动，因为换过来的值还需检查
            else:
                cur += 1
```

> 三指针的核心是 `cur <= right` 作为循环条件，以及遇到 2 时 `cur` 不动——这是最容易写错的地方。

---

## 寻找重复数

**LeetCode 287** | 难度：中等

### 题目描述

给定一个包含 n + 1 个整数的数组 nums，其数字都在 [1, n] 范围内。数组中有且只有一个重复的整数，返回这个重复的数。要求不修改数组 nums 且只使用常数级 O(1) 的额外空间。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,3,4,2,2]` | `2` | 2 是重复数 |
| `nums = [3,1,3,4,2]` | `3` | 3 是重复数 |
| `nums = [3,3,3,3,3]` | `3` | 重复多次仍返回 3 |

### 思路

数组长度 n+1，元素范围 [1, n]，只有一个重复数。可以将数组视为隐式链表：`i → nums[i]`。因为范围在 [1, n] 且有一个重复数，必然形成环（重复数是环的入口）。

应用 Floyd 判圈算法（同环形链表 II）：快慢指针在「链表」上走，相遇后 slow 归零，两者同步走，再次相遇即环入口 = 重复数。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| Floyd 快慢指针 | 中 | O(n) 时间 O(1) 空间 | 首选，满足题目的严格约束 |
| 哈希表 | 低 | O(n) 时间 O(n) 空间 | 简单但不满足 O(1) 空间要求 |
| 修改原数组（标记负数） | 低 | O(n) 时间 O(1) 空间 | 题目禁止修改数组 |

### Python 实现

```python
from typing import List


class Solution:
    def find_duplicate(self, nums: List[int]) -> int:
        # 将数组视为隐式链表：i → nums[i]
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

> 这是一个巧妙的建模：数组本身不是链表，但通过 `i → nums[i]` 的映射将其**视为**链表，从而复用 Floyd 判圈。这是考试中展示抽象建模能力的好题。

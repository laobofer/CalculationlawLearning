# 前缀和算法

## 适用场景

前缀和是处理 **「频繁查询区间和 / 子数组求和条件判断」** 的最核心技巧，适用于以下问题：

- **静态数组的区间和查询**：数组不变，多次查询 `sum[i..j]`，O(n) 预处理 + O(1) 查询
- **和为 K 的子数组**：通过 `pre_sum[j] - pre_sum[i] == k` 转化为两数之差问题，用哈希表边遍历边统计
- **和可被 K 整除的子数组**：同余定理——`(pre_sum[j] - pre_sum[i]) % k == 0` 等价于 `pre_sum[j] % k == pre_sum[i] % k`
- **最长满足条件的子数组**：哈希表记录每个前缀和首次出现的位置，求最大间距
- **前后缀分离**：如「除自身以外数组的乘积」，分别计算前缀积和后缀积
- **二维区域和**：二维前缀和快速计算矩形区域内的元素和

> **核心模式**：前缀和 + 哈希表 = O(n) 解决子数组条件问题。哈希表通常存储 `前缀和值 → 出现次数/首次出现位置`。关键初始化：`{0: 1}` 或 `{0: -1}` 处理从头开始的子数组。

## 核心思想

前缀和的核心公式：

- **一维**：`pre_sum[i]` 表示 `nums[0..i-1]` 的和，`sum[i..j] = pre_sum[j+1] - pre_sum[i]`
- **二维**：`pre_sum[i][j]` 表示 `matrix[0..i-1][0..j-1]` 的和，区域和 = `pre_sum[r2+1][c2+1] - pre_sum[r1][c2+1] - pre_sum[r2+1][c1] + pre_sum[r1][c1]`

---

## 目录
- [区域和检索 - 数组不可变](#区域和检索---数组不可变)
- [二维区域和检索 - 矩阵不可变](#二维区域和检索---矩阵不可变)
- [和为 K 的子数组](#和为k的子数组)
- [和可被 K 整除的子数组](#和可被k整除的子数组)
- [寻找数组的中心下标](#寻找数组的中心下标)
- [最后 K 个数的乘积](#最后k个数的乘积)
- [矩阵区域和](#矩阵区域和)
- [表现良好的时间段](#表现良好的时间段)
- [连续数组](#连续数组)
- [连续的子数组和](#连续的子数组和)
- [除自身以外数组的乘积](#除自身以外数组的乘积)

---

## 区域和检索 - 数组不可变

**LeetCode 303** | 难度：简单

### 题目描述

设计一个 NumArray 类，初始化时接收一个整数数组 nums。该类支持 `sumRange(left, right)` 查询，返回数组中下标 left 到 right（包含两端）的元素之和。数组不可变，且查询操作会被多次调用。要求预处理 O(n)，每次查询 O(1)。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [-2, 0, 3, -5, 2, -1]; sumRange(0, 2)` | `1` | -2 + 0 + 3 = 1 |
| `nums = [-2, 0, 3, -5, 2, -1]; sumRange(2, 5)` | `-1` | 3 + (-5) + 2 + (-1) = -1 |
| `nums = [-2, 0, 3, -5, 2, -1]; sumRange(0, 5)` | `-3` | 整个数组求和 = -3 |

### 思路

前缀和模板题。初始化时构建 `pre_sum` 数组（长度 n+1），查询时 O(1) 返回差值。前缀和数组多开一位的目的是统一 `sumRange(0, j)` 这种从头开始的计算。

### Python 实现

```python
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            self.pre_sum[i] = self.pre_sum[i - 1] + nums[i - 1]

    def sum_range(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]
```

---

## 二维区域和检索 - 矩阵不可变

**LeetCode 304** | 难度：中等

### 题目描述

给定一个二维矩阵 matrix，设计 NumMatrix 类支持 `sumRegion(row1, col1, row2, col2)` 查询，返回以 (row1, col1) 为左上角、(row2, col2) 为右下角的矩形区域内所有元素之和。矩阵不可变，查询次数远大于初始化次数。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `sumRegion(2, 1, 4, 3)` | `8` | 区域 `(2,1)` 到 `(4,3)`：2+0+1+1+0+1+0+3 = 8 |
| `sumRegion(1, 1, 2, 2)` | `11` | 区域 `(1,1)` 到 `(2,2)`：6+3+2+0 = 11 |
| `sumRegion(1, 2, 2, 4)` | `12` | 区域 `(1,2)` 到 `(2,4)`：3+2+1+0+1+5 = 12 |

> 给定矩阵：`[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]`

### 思路

一维前缀和的二维推广。`pre_sum[i][j]` = 以 `(0,0)` 为左上角、`(i-1, j-1)` 为右下角的矩形和。构建公式：

```
pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1] + matrix[i-1][j-1]
```

查询 `(r1,c1)` 到 `(r2,c2)`：大面积减去两个长条再加回重复减掉的小角。

### Python 实现

```python
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = (
                    self.pre_sum[i - 1][j]
                    + self.pre_sum[i][j - 1]
                    - self.pre_sum[i - 1][j - 1]
                    + matrix[i - 1][j - 1]
                )

    def sum_region(
        self, row1: int, col1: int, row2: int, col2: int
    ) -> int:
        return (
            self.pre_sum[row2 + 1][col2 + 1]
            - self.pre_sum[row1][col2 + 1]
            - self.pre_sum[row2 + 1][col1]
            + self.pre_sum[row1][col1]
        )
```

---

## 和为 K 的子数组

**LeetCode 560** | 难度：中等

### 题目描述

给定一个整数数组 nums 和一个整数 k，统计该数组中和为 k 的连续子数组的个数。子数组是数组中元素的连续非空序列。数组中可能包含负数。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1, 1, 1], k = 2` | `2` | 两个子数组 `[1,1]`（下标 0..1 和 1..2） |
| `nums = [1, 2, 3], k = 3` | `2` | 子数组 `[1,2]` 和 `[3]` |
| `nums = [1, -1, 0], k = 0` | `3` | `[1,-1]`, `[0]`, `[1,-1,0]` |

### 思路

核心转化：`sum[i..j] == k` 等价于 `pre_sum[j+1] - pre_sum[i] == k`，即 `pre_sum[i] == pre_sum[j+1] - k`。

**最优解法**：边遍历边用哈希表统计前缀和出现的次数。遍历到位置 j 时，查找 `pre_sum[j+1] - k` 在前面出现了多少次——这就是以 j 为右端点的满足条件的子数组个数。

原代码先构建完整哈希表再二分查找的方式虽然正确，但多了 O(n log n) 的二分开销和额外的存储。边遍历边计数的 O(n) 哈希法更简洁。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 哈希表边遍历边计数 | 中 | O(n) | 首选 |
| 前缀和 + 哈希表 + 二分 | 中 | O(n log n) | 可接受 |
| 暴力枚举 | 低 | O(n²) | 不推荐，会超时 |

### Python 实现

```python
from typing import List


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        # count[前缀和] = 出现次数
        count = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            need = prefix_sum - k
            if need in count:
                result += count[need]
            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return result
```

> 关键：初始化 `count = {0: 1}` 表示空前缀和为 0 出现一次，处理子数组从头开始的情况。

---

## 和可被 K 整除的子数组

**LeetCode 974** | 难度：中等

### 题目描述

给定一个整数数组 nums 和一个整数 k，返回其中元素之和可被 k 整除的（连续、非空）子数组的数目。子数组是数组中连续的一部分。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [4, 5, 0, -2, -3, 1], k = 5` | `7` | 共有 7 个子数组的和能被 5 整除 |
| `nums = [5], k = 9` | `0` | 9 不能整除 5，无符合条件的子数组 |
| `nums = [0, 0, 0], k = 3` | `6` | 所有子数组的和均为 0，0 能被 3 整除 |

### 思路

与「和为 K 的子数组」类似，但条件是 `(pre_sum[j] - pre_sum[i]) % k == 0`，即 `pre_sum[j] % k == pre_sum[i] % k`。

同余原理：如果两个前缀和对 k 取余相同，它们之间的子数组之和就能被 k 整除。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 哈希表 + 同余定理边遍历 | 中 | O(n) | 首选 |
| 前缀和 + 哈希表预存 + 二分 | 中 | O(n log n) | 不推荐 |

### Python 实现

```python
from typing import List


class Solution:
    def subarrays_div_by_k(self, nums: List[int], k: int) -> int:
        # count[余数] = 出现次数
        count = {0: 1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            # Python 的 % 自动返回非负余数，无需额外处理
            if mod in count:
                result += count[mod]
            count[mod] = count.get(mod, 0) + 1

        return result
```

> Python 的取余 `%` 对负数自动返回 `[0, k)` 范围内的结果，这是相对于 Java / C++ 的巨大优势。

---

## 寻找数组的中心下标

**LeetCode 724** | 难度：简单

### 题目描述

给定一个整数数组 nums，计算数组的「中心下标」。中心下标是数组的一个下标，其左侧所有元素之和等于右侧所有元素之和。如果不存在中心下标，返回 -1；如果有多个，返回最靠近左边的那个。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1, 7, 3, 6, 5, 6]` | `3` | 左侧和 = 1+7+3 = 11，右侧和 = 5+6 = 11 |
| `nums = [1, 2, 3]` | `-1` | 不存在满足条件的中心下标 |
| `nums = [2, 1, -1]` | `0` | 左侧和 = 0（下标 0 左边无元素），右侧和 = 1+(-1) = 0 |

### 思路

中心下标 i 满足 `sum[0..i-1] == sum[i+1..n-1]`。用前缀和：`left_sum = pre_sum[i]`，`right_sum = pre_sum[n] - pre_sum[i+1]`。

也可以不用完整前缀和数组：先算总和 `total`，然后从左到右遍历。维护 `left_sum`，对于每个位置 `i`，`right_sum = total - left_sum - nums[i]`。

### Python 实现

```python
from typing import List


class Solution:
    def pivot_index(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # right_sum = total - left_sum - num
            if left_sum == total - left_sum - num:
                return i
            left_sum += num

        return -1
```

> 使用运行中的 `left_sum` 替代完整前缀和数组，节省 O(n) 空间。

---

## 最后 K 个数的乘积

**LeetCode 1352** | 难度：中等

### 题目描述

设计一个类 ProductOfNumbers，支持两种操作：(1) `add(num)` 将数字 num 添加到当前数字流末尾；(2) `getProduct(k)` 返回当前数字流中最后 k 个数的乘积。数组长度会不断增长，需要高效处理 0 的情况。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `add(3); add(0); add(2); add(5); add(4); getProduct(2)` | `20` | 最后两个数 5 × 4 = 20 |
| `接着 getProduct(3)` | `40` | 最后三个数 2 × 5 × 4 = 40 |
| `接着 getProduct(4)` | `0` | 最后四个数中含 0，结果为 0 |

### 思路

前缀积的变体。关键是处理 0：一旦遇到 0，之前的前缀积全部失效（任何含有 0 的子数组乘积都是 0），因此将前缀积重置为 `[1]`。

查询时：如果 k 超过了当前前缀积数组的长度（说明最近 k 个数中包含 0），直接返回 0；否则用末尾前缀积除以对应位置的前缀积。

### Python 实现

```python
class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # 遇零重置
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def get_product(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]
```

---

## 矩阵区域和

**LeetCode 1314** | 难度：中等

### 题目描述

给定一个 m x n 的矩阵 mat 和一个整数 k，返回一个相同大小的矩阵 answer，其中 answer[i][j] 等于 mat 中以 (i, j) 为中心、边长为 2k+1 的正方形区域内所有元素之和（区域边界会被矩阵边界裁剪）。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1` | `[[12,21,16],[27,45,33],[24,39,28]]` | 对每个位置计算 3x3 区域和 |
| `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 0` | `[[1,2,3],[4,5,6],[7,8,9]]` | k=0 时每个位置只包含自身 |
| `mat = [[1]], k = 5` | `[[1]]` | 单元素矩阵，区域被边界裁剪 |

### 思路

二维前缀和的直接应用。先构建二维前缀和，然后对每个 `(i, j)`，计算以它为中心、半径为 k 的矩形区域和。注意边界裁剪：`r1 = max(i-k, 0)`，`c1 = max(j-k, 0)` 等。

本质和「二维区域和检索」相同的公式，只是把查询嵌入到遍历中。

### Python 实现

```python
from typing import List


class Solution:
    def matrix_block_sum(
        self, mat: List[List[int]], k: int
    ) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # 构建二维前缀和
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = (
                    pre_sum[i - 1][j]
                    + pre_sum[i][j - 1]
                    - pre_sum[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(i - k, 0), max(j - k, 0)
                r2, c2 = min(i + k, m - 1), min(j + k, n - 1)
                result[i][j] = (
                    pre_sum[r2 + 1][c2 + 1]
                    - pre_sum[r1][c2 + 1]
                    - pre_sum[r2 + 1][c1]
                    + pre_sum[r1][c1]
                )

        return result
```

---

## 表现良好的时间段

**LeetCode 1124** | 难度：中等

### 题目描述

给定一个数组 hours，记录员工每天的工作小时数。每天工作时长大于 8 小时视为「劳累的一天」。称一个时间段为「表现良好的时间段」，如果该时间段内劳累的天数严格大于不劳累的天数。返回表现良好时间段的最长长度。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `hours = [9, 9, 6, 0, 6, 6, 9]` | `3` | 最长的表现良好时间段是 `[9, 9, 6]`（下标 0..2），劳累天数 2 > 不劳累天数 1 |
| `hours = [6, 6, 6]` | `0` | 没有劳累天数，任何时间段都不满足条件 |
| `hours = [9, 9, 9]` | `3` | 整个数组是表现良好时间段，劳累天数 3 > 0 |

### 思路

将问题转化为前缀和：工作时间 > 8 小时记为 +1，否则记为 -1。问题变为「找最长的子数组使 sum > 0」，即 `pre_sum[j] > pre_sum[i]`。

关键技巧：维护一个单调递减栈记录前缀和的下坡位置，然后从右向左查找每个位置能延伸到的最远起点。或者用哈希表记录每个前缀和首次出现的位置，然后对每个 i 查找 `pre_sum[i] - 1` 的位置。

### Python 实现

```python
from typing import List


class Solution:
    def longest_wpi(self, hours: List[int]) -> int:
        n = len(hours)
        pre_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + (1 if hours[i - 1] > 8 else -1)

        # 哈希表记录每个前缀和首次出现的位置
        first_pos = {}
        result = 0

        for i in range(n + 1):
            if pre_sum[i] not in first_pos:
                first_pos[pre_sum[i]] = i
            # 前面有比当前前缀和小的，说明中间区间 > 0
            if pre_sum[i] - 1 in first_pos:
                result = max(result, i - first_pos[pre_sum[i] - 1])

        return result
```

---

## 连续数组

**LeetCode 525** | 难度：中等

### 题目描述

给定一个二进制数组 nums，找出含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [0, 1]` | `2` | 整个数组 `[0, 1]` 中含 1 个 0 和 1 个 1 |
| `nums = [0, 1, 0]` | `2` | 子数组 `[0, 1]` 或 `[1, 0]`，长度均为 2 |
| `nums = [0, 0, 1, 0, 0, 0, 1, 1]` | `6` | 子数组 `[0, 0, 1, 0, 0, 0, 1, 1]` 下标 2..7 中含 3 个 0 和 3 个 1 |

### 思路

将 0 视为 -1，1 视为 +1，问题转化为「和为 0 的最长子数组」。用哈希表记录每个前缀和首次出现的索引。当相同前缀和再次出现时，中间这段的和就是 0。

### Python 实现

```python
from typing import List


class Solution:
    def find_max_length(self, nums: List[int]) -> int:
        # 0 转 -1
        transformed = [num if num == 1 else -1 for num in nums]
        n = len(transformed)

        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + transformed[i - 1]

        # 记录每个前缀和首次出现的位置
        first_pos = {}
        result = 0

        for i in range(n + 1):
            if pre_sum[i] not in first_pos:
                first_pos[pre_sum[i]] = i
            else:
                result = max(result, i - first_pos[pre_sum[i]])

        return result
```

> 也可以边遍历边构建，省略 pre_sum 数组：维护 `cur_sum`，当 `nums[i] == 0` 时减一，否则加一。

---

## 连续的子数组和

**LeetCode 523** | 难度：中等

### 题目描述

给定一个整数数组 nums 和一个整数 k，判断是否存在长度至少为 2 的连续子数组，其元素之和为 k 的倍数。如果 k 的倍数包括 0，即子数组和为 0 也满足条件。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [23, 2, 4, 6, 7], k = 6` | `true` | 子数组 `[2, 4]` 和为 6，是 6 的倍数 |
| `nums = [23, 2, 6, 4, 7], k = 6` | `true` | 子数组 `[23, 2, 6, 4, 7]` 和为 42，是 6 的倍数 |
| `nums = [23, 2, 6, 4, 7], k = 13` | `false` | 不存在任何长度 >= 2 的子数组和为 13 的倍数 |

### 思路

寻找长度至少为 2 且和为 k 的倍数的子数组。和「和可被 K 整除的子数组」类似，但多了长度限制。

关键：哈希表存储余数**首次出现**的索引。当相同余数再次出现时，检查间距是否 >= 2。

### Python 实现

```python
from typing import List


class Solution:
    def check_subarray_sum(self, nums: List[int], k: int) -> bool:
        # 余数 -> 首次出现的索引
        mod_pos = {0: -1}
        pre_sum = 0

        for i, num in enumerate(nums):
            pre_sum += num
            mod = pre_sum % k

            if mod not in mod_pos:
                mod_pos[mod] = i
            elif i - mod_pos[mod] >= 2:
                return True

        return False
```

> `mod_pos[0] = -1` 的初始化处理了从头开始的子数组满足条件的情况。

---

## 除自身以外数组的乘积

**LeetCode 238** | 难度：中等

### 题目描述

给定一个整数数组 nums，返回一个数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。要求：不能使用除法，时间复杂度 O(n)，且是否使用额外空间为进阶要求（输出数组不计入额外空间）。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1, 2, 3, 4]` | `[24, 12, 8, 6]` | answer[0]=2×3×4=24, answer[1]=1×3×4=12, ... |
| `nums = [-1, 1, 0, -3, 3]` | `[0, 0, 9, 0, 0]` | 除 0 位置的元素外，其他位置乘积均含 0，故为 0 |
| `nums = [2, 3]` | `[3, 2]` | 最小输入情况，answer[0]=3, answer[1]=2 |

### 思路

本质是前缀积 + 后缀积。`answer[i] = prefix[i-1] * suffix[i+1]`。可以分成两个数组分别计算前缀积和后缀积，也可以在单个结果数组上两遍扫描。

最优 O(1) 额外空间（不计输出数组）：第一遍从左到右在 `answer[i]` 中保存 `prefix[i-1]`，第二遍从右到左维护一个 `suffix` 变量与 `answer[i]` 相乘。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 两遍扫描 O(1) 额外空间 | 中 | O(n) | 首选，展示空间优化 |
| 前缀积 + 后缀积数组 | 低 | O(n) 时间 O(n) 空间 | 简单直接 |

### Python 实现

```python
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # 第一遍：answer[i] = 左边所有元素的乘积
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # 第二遍：乘上右边所有元素的乘积
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```

> O(1) 额外空间（answer 不计入），两遍扫描，这是面试的标准答案。

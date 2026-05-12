# 差分数组算法

## 适用场景

差分数组专门处理 **「多次区间更新，最后统一查询」** 的问题。当你面对以下特征时，应当优先考虑差分数组：

- **批量区间增减**：对数组的多个连续子区间进行加法/减法操作，最终需要知道每个位置的值
- **线下处理（离线算法）**：所有更新操作提前给出，不需要在更新过程中实时查询结果
- **区间操作频繁但查询次数少**：有 m 次区间更新和 1 次最终查询，差分数组将 O(mn) 降为 O(m+n)
- **典型问题**：航班预订统计、拼车（上下客模拟）、区间加法、数组区间修改

> **核心对比**：前缀和是「频繁查询区间和，数组不变」；差分数组是「频繁修改区间值，最后统一查询」。两者互为逆运算。

---

## 核心思想

差分数组 `diff[i]` 定义为原数组相邻元素的差值：`diff[i] = nums[i] - nums[i-1]`（约定 `nums[-1] = 0`）。

**区间更新**：要想把 `nums[start..end]` 每个元素加 `inc`，只需：
```
diff[start] += inc
diff[end + 1] -= inc
```

**还原原数组**：对差分数组求前缀和即可还原出原数组：
```
nums[i] = diff[0] + diff[1] + ... + diff[i]
```

这就是差分数组的精髓——两次 O(1) 操作完成一次区间更新。

---

## 目录
- [区间加法](#区间加法)
- [拼车](#拼车)
- [航班预订统计](#航班预订统计)

---

## 区间加法

**LeetCode 370（VIP）** | 难度：中等

### 题目描述

假设你有一个长度为 `length` 的整数数组，初始所有元素均为 0。给你一个更新操作数组 `updates`，每个操作 `updates[i] = [start, end, inc]` 表示将子数组 `[start, end]`（包含两端）中的每个元素都加上 `inc`。请你返回所有更新操作完成后得到的最终数组。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]` | `[-2,0,3,5,3]` | 初始 `[0,0,0,0,0]`，三次更新后得到最终结果 |
| `length = 3, updates = [[0,1,5],[1,2,10]]` | `[5,15,10]` | 第一次更新后 `[5,5,0]`，第二次后 `[5,15,10]` |
| `length = 4, updates = [[0,3,3],[1,2,-1]]` | `[3,2,2,3]` | 先全部加 3，再对 [1,2] 减 1 |

### 思路

差分数组的模板题。`updates` 中每个 `[start, end, inc]` 表示将 `[start, end]` 范围内的元素加 `inc`。直接应用差分数组：`diff[start] += inc`，`diff[end+1] -= inc`，最后前缀和还原。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 差分数组 | 低 | O(length + updates) | 首选 |
| 暴力的每次循环累加 | 极低 | O(length * updates) | 超时 |

### Python 实现

```python
from typing import List


class Solution:
    def get_modified_array(
        self, length: int, updates: List[List[int]]
    ) -> List[int]:
        diff = [0] * length

        for start, end, inc in updates:
            diff[start] += inc
            if end + 1 < length:
                diff[end + 1] -= inc

        # 前缀和还原
        result = [diff[0]]
        for i in range(1, length):
            result.append(result[-1] + diff[i])

        return result
```

> `diff[end+1] -= inc` 需要有边界检查，因为 `end` 可能指向数组最后一个元素。

---

## 拼车

**LeetCode 1094** | 难度：中等

### 题目描述

车上最初有 `capacity` 个空座位，车辆只能向东行驶（不允许掉头）。给定一个行程数组 `trips`，其中 `trips[i] = [numPassengers, from, to]` 表示有 `numPassengers` 名乘客从 `from` 站上车，在 `to` 站下车。请你判断是否可以一次性接载所有乘客——即在任何一站，车上的乘客人数都不超过 `capacity`。如果可以返回 `true`，否则返回 `false`。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `trips = [[2,1,5],[3,3,7]], capacity = 4` | `false` | 第 3 站时车上 5 人（2+3），超出容量 4 |
| `trips = [[2,1,5],[3,3,7]], capacity = 5` | `true` | 最多同时 5 人，刚好等于容量 |
| `trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11` | `true` | 第 3~7 站最多 11 人，未超容量 |

### 思路

将行程视为区间更新：`trips[i] = [numPassengers, from, to]`。对每个行程，在 `from` 站增加 `numPassengers`，在 `to` 站减少 `numPassengers`（乘客在 `to` 站已下车，不计入）。

对所有行程应用差分数组后，求前缀和得到每站的车上人数。如果任何一站人数超过 `capacity`，返回 `False`。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 差分数组 | 低 | O(trips + stations) | 首选 |
| 逐站模拟 | 高 | 复杂且易错 | 不推荐 |

### Python 实现

```python
from typing import List


class Solution:
    def car_pooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001  # 题目给定最多 1000 站

        for num, start, end in trips:
            diff[start] += num
            if end < len(diff):
                diff[end] -= num  # 乘客在 end 站已下，不计入

        # 前缀和还原并检查
        cur = 0
        for d in diff:
            cur += d
            if cur > capacity:
                return False

        return True
```

> 核心转化：把「上下车」建模为「区间加减」——上车站 +num，下车站 -num。差分数组天然适配这种场景。

---

## 航班预订统计

**LeetCode 1109** | 难度：中等

### 题目描述

这里有 `n` 个航班，按 1 到 `n` 编号。给定一个预订数组 `bookings`，其中 `bookings[i] = [first, last, seats]` 表示从航班 `first` 到航班 `last`（包含两端）的每个航班预订了 `seats` 个座位。请你返回一个长度为 `n` 的数组 `answer`，其中 `answer[i]` 表示第 `i+1` 个航班的总预订座位数。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5` | `[10,55,45,25,25]` | 第 2 个航班累计 10+20+25=55 |
| `bookings = [[1,2,10],[2,2,15]], n = 2` | `[10,25]` | 第 2 个航班 10+15=25 |
| `bookings = [[1,5,5],[2,3,3],[4,5,2]], n = 5` | `[5,8,8,7,7]` | 多区间叠加后的结果 |

### 思路

每个 `[first, last, seats]` 表示从航班 `first` 到 `last` 每班预订 `seats` 个座位，这些是 1-indexed。转为 0-indexed 后直接套用差分数组模板。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 差分数组 | 低 | O(bookings + n) | 首选 |
| 暴力更新 | 低 | O(bookings * n) | 超时 |

### Python 实现

```python
from typing import List


class Solution:
    def corp_flight_bookings(
        self, bookings: List[List[int]], n: int
    ) -> List[int]:
        diff = [0] * n

        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats

        # 前缀和还原
        result = [0] * n
        result[0] = diff[0]
        for i in range(1, n):
            result[i] = result[i - 1] + diff[i]

        return result
```

> 注意 1-indexed 到 0-indexed 的转换：`first - 1` 和 `last`（因为差分数组中 `end+1` 位置才减，原来是 `last+1`，转 0-indexed 后就是 `last`）。

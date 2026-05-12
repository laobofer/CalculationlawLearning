# 矩阵算法

## 适用场景

矩阵算法处理二维网格上的操作，常见于以下问题：

- **坐标变换**：旋转、转置、对角线遍历——核心是找到变换前后坐标的对应关系
- **螺旋/蛇形遍历**：按特定顺序（顺时针螺旋、对角线、之字形）遍历矩阵——维护边界或方向向量
- **二维前缀和**：快速查询矩形区域的和——将一维前缀和推广到二维
- **多路归并在矩阵上的应用**：有序矩阵中找第 K 小元素——每行/列有序 = 多个有序序列的归并
- **原地矩阵操作**：在不额外分配矩阵的情况下完成旋转、翻转等操作——利用坐标轮换或两次翻转的组合

> **核心思维**：矩阵题的关键是将二维坐标 `(i, j)` 与一维索引或几何变换建立联系。常用技巧包括 `i-j` 标识对角线、`i+j` 标识反对角线、`(j, n-1-i)` 实现顺时针旋转。

## 目录
- [二维网格迁移](#二维网格迁移)
- [将矩阵按对角线排序](#将矩阵按对角线排序)
- [旋转矩阵](#旋转矩阵)
- [矩阵转置](#矩阵转置)
- [螺旋矩阵](#螺旋矩阵)
- [有序矩阵中第 K 小的元素](#有序矩阵中第k小的元素)

---

## 二维网格迁移

**LeetCode 1260** | 难度：简单

### 题目描述

给定一个 m x n 的二维网格 `grid` 和一个整数 `k`，将网格中的所有元素向右循环移动 `k` 次。每次移动操作中，每个元素会移到其右侧相邻的位置，最后一列的元素移到下一行的第一列，最后一个元素移到第一个位置。返回移动 `k` 次后的网格。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1` | `[[9,1,2],[3,4,5],[6,7,8]]` | 所有元素右移一次 |
| `grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4` | `[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]` | 4x4 网格，移动 4 次 |
| `grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9` | `[[1,2,3],[4,5,6],[7,8,9]]` | k 等于元素总数，回到原位 |

### 思路

把二维网格视为一维数组（长度为 `m * n`），迁移 `k` 次等价于整体右移 `k % (m * n)` 个位置。用三次反转实现数组的循环移位——这是原地 O(1) 空间的标准技巧。

原代码提供了两种实现。方法一每次移动一个元素（O(k * m * n)），效率低。方法二通过三次反转（O(m * n)）更优。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 三次反转（一维化索引） | 中 | O(mn) 时间 O(1) 空间 | 首选，展示原地操作技巧 |
| 逐次移动 | 低 | O(k * mn) | 仅用于验证思路 |
| 新建矩阵填入 | 低 | O(mn) 时间 O(mn) 空间 | 不推荐，浪费空间 |

### Python 实现

```python
from typing import List


class Solution:
    def shift_grid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total

        if k == 0:
            return grid

        # 三次反转实现循环右移
        self._reverse_range(grid, 0, total - k - 1)
        self._reverse_range(grid, total - k, total - 1)
        self._reverse_range(grid, 0, total - 1)
        return grid

    def _get(self, grid: List[List[int]], index: int) -> int:
        n = len(grid[0])
        return grid[index // n][index % n]

    def _set(self, grid: List[List[int]], index: int, val: int) -> None:
        n = len(grid[0])
        grid[index // n][index % n] = val

    def _reverse_range(self, grid: List[List[int]], i: int, j: int) -> None:
        while i < j:
            val_i = self._get(grid, i)
            val_j = self._get(grid, j)
            self._set(grid, i, val_j)
            self._set(grid, j, val_i)
            i += 1
            j -= 1
```

> 核心技巧：一维索引 `index` 对应二维 `[index // n][index % n]`；循环右移 = `reverse(0, n-k-1) + reverse(n-k, n-1) + reverse(0, n-1)`。

---

## 将矩阵按对角线排序

**LeetCode 1329** | 难度：中等

### 题目描述

给定一个 m x n 的整数矩阵 `mat`，矩阵的某条对角线由满足行坐标与列坐标之差相等的所有单元格组成。要求将矩阵中的每条对角线按升序排序，并返回排序后的矩阵。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]` | `[[1,1,1,1],[1,2,2,2],[1,2,3,3]]` | 每条对角线升序排列 |
| `mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]` | `[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]` | 多条对角线分别排序 |

### 思路

同一对角线上的元素满足 **行坐标减列坐标为定值**（`i - j` 相等）。遍历所有元素按 `i - j` 分组，对每组降序排序后用栈弹出一一填回。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 哈希表分组 + 排序 | 低 | O(mn log d)，d 为对角线长度 | 首选，思路最清晰 |
| 冒泡按对角线 | 高 | O(mn * min(m,n)) | 不推荐 |

### Python 实现

```python
from typing import List


class Solution:
    def diagonal_sort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # 对角线由 (i - j) 标识
        diagonals: dict[int, list[int]] = {}

        for i in range(m):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(mat[i][j])

        # 降序排列以便 pop() 取到最小值
        for values in diagonals.values():
            values.sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()

        return mat
```

> 关键观察：同一对角线上 `i - j` 恒为定值，这是对角线分组的基础。

---

## 旋转矩阵

**LeetCode 48** | 难度：中等

### 题目描述

给定一个 n x n 的二维矩阵，要求将其顺时针旋转 90 度。必须原地修改矩阵，不能使用额外的矩阵空间。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `matrix = [[1,2,3],[4,5,6],[7,8,9]]` | `[[7,4,1],[8,5,2],[9,6,3]]` | 顺时针旋转 90 度 |
| `matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]` | `[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]` | 4x4 矩阵旋转 |

### 思路

顺时针旋转 90 度本质上是坐标变换 `(i, j) → (j, n-1-i)`。只遍历左上角 1/4 的区域，对每个位置找到对应的四个点进行一轮四向交换。

原代码用向量旋转的思路（绕中心点做 90° 旋转）实现，过于复杂且引入了浮点数。推荐的使用整数坐标直接计算四个对应点，纯整数无精度问题。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 四向原地交换（1/4 遍历） | 中 | O(n²) 时间 O(1) 空间 | 首选 |
| 先转置再水平翻转 | 低 | O(n²) 时间 O(1) 空间 | 最简单，最推荐 |
| 向量旋转法 | 高 | O(n²) | 不推荐，引入浮点 |

### Python 实现

```python
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """顺时针旋转 90 度，原地修改。"""
        n = len(matrix)

        # 先转置（对角线翻转）
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 再水平翻转（每行反转）
        for i in range(n):
            matrix[i].reverse()
```

> 考试最优解：`转置 + 水平翻转` 两行代码，比四点轮换更容易写对。逆时针旋转 90° 则是 `转置 + 垂直翻转`。

---

## 矩阵转置

**LeetCode 867** | 难度：简单

### 题目描述

给定一个 m x n 的二维整数矩阵，返回其转置矩阵。转置操作将矩阵的行和列互换，即原矩阵第 i 行第 j 列的元素变为新矩阵第 j 行第 i 列的元素。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `matrix = [[1,2,3],[4,5,6],[7,8,9]]` | `[[1,4,7],[2,5,8],[3,6,9]]` | 3x3 方阵转置 |
| `matrix = [[1,2,3],[4,5,6]]` | `[[1,4],[2,5],[3,6]]` | 非方阵转置，2x3 变 3x2 |

### 思路

Python 中直接用 `zip(*matrix)` 即可完成转置——`*` 解包每一行作为 `zip` 的参数，`zip` 将各行的同列元素组合成元组。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| `list(zip(*matrix))` | 极低 | O(mn)，C 级实现 | 首选 |
| 手动双重循环 | 低 | O(mn) | 仅在禁用 zip 时使用 |

### Python 实现

```python
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*matrix)]
```

> `zip(*matrix)` 返回的是元组，用 `list(row)` 转为列表以符合题目要求。

---

## 螺旋矩阵

**LeetCode 54** | 难度：中等

### 题目描述

给定一个 m x n 的矩阵，按照顺时针螺旋顺序遍历并返回矩阵中的所有元素。从矩阵的左上角开始，先向右、再向下、再向左、再向上，如此循环直到遍历完所有元素。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `matrix = [[1,2,3],[4,5,6],[7,8,9]]` | `[1,2,3,6,9,8,7,4,5]` | 3x3 螺旋遍历 |
| `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]` | `[1,2,3,4,8,12,11,10,9,5,6,7]` | 3x4 螺旋遍历 |
| `matrix = [[1]]` | `[1]` | 单元素矩阵 |

### 思路

维护四个边界 `top / bottom / left / right`，按「右 → 下 → 左 → 上」的顺序循环遍历。每完成一个方向，对应边界向内收缩一步。循环终止条件是边界交错。

原代码用「方向向量 + 边界检测」的方式，逻辑较绕。四边界逐步收缩法更直观且不易出错。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 四边界收缩法 | 中 | O(mn)，每个元素访问一次 | 首选 |
| 方向向量 + 访问标记矩阵 | 中 | O(mn) + O(mn) 空间 | 可接受 |
| 方向向量 + 边界碰撞检测 | 高 | O(mn) | 容易写错边界条件 |

### Python 实现

```python
from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while True:
            # 向右
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            if top > bottom:
                break

            # 向下
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # 向左
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            if top > bottom:
                break

            # 向上
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return result
```

> 四个 `while True` 内的 break 检测是关键：每次收缩边界后立即判断是否「越界」，防止重复访问。

---

## 有序矩阵中第 K 小的元素

**LeetCode 378** | 难度：中等

### 题目描述

给定一个 n x n 的矩阵，其中每行和每列都按升序排列。找出矩阵中第 k 小的元素。注意，这里的第 k 小是指在所有元素中排序后的第 k 个，而非去重后的第 k 个。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8` | `13` | 第 8 小的元素是 13 |
| `matrix = [[1,2],[1,3]], k = 2` | `1` | 有重复元素，第 2 小仍是 1 |
| `matrix = [[1,2],[3,4]], k = 4` | `4` | 最大元素即第 4 小 |

### 思路

利用每行有序的性质，用小顶堆做「多路归并」。先将每行第一个元素入堆，每次弹出最小值，然后将该值所在行的下一个元素入堆。第 k 次弹出的就是答案。

这个技巧和合并 K 个有序链表完全相同——只是数据结构从链表变成了矩阵的行。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 小顶堆多路归并 | 中 | O(k log n)，n 为行数 | 首选，利用行有序 |
| 二分查找 + 计数 | 高 | O(n log(max-min)) | 性能更好但难写对 |
| 全量排序 | 低 | O(mn log(mn)) | 简单粗暴但不推荐 |

### Python 实现

```python
import heapq
from typing import List


class Solution:
    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        # 每行第一个元素入堆：(值, 行号, 列号)
        for row_idx, row in enumerate(matrix):
            heapq.heappush(min_heap, (row[0], row_idx, 0))

        for _ in range(k - 1):
            _, row_idx, col_idx = heapq.heappop(min_heap)
            # 该行还有元素则入堆
            if col_idx + 1 < len(matrix[row_idx]):
                heapq.heappush(
                    min_heap,
                    (matrix[row_idx][col_idx + 1], row_idx, col_idx + 1)
                )

        val, _, _ = heapq.heappop(min_heap)
        return val
```

> 考试提示：这类「有序序列归并求第 K 小」的模式也适用于 `查找和最小的 K 对数字` 和 `合并 K 个有序链表`。

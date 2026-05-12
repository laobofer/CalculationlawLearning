# 滑动窗口算法

## 适用场景

滑动窗口是处理 **数组/字符串中子串（连续子序列）问题** 的核心技巧，能将许多 O(n²) 暴力解优化到 O(n)。当你遇到以下特征时应考虑滑动窗口：

- **求满足条件的「最长/最短」连续子数组/子串**：如最小覆盖子串、无重复字符的最长子串、长度最小的子数组
- **求满足条件的子数组/子串「个数」**：如乘积小于 K 的子数组、和为 K 的子数组
- **固定长度的窗口匹配**：如字符串排列判断、字母异位词搜索
- **窗口内包含有限制条件**：如最多包含 K 个 0 的最长连续 1、最多替换 K 个字符的最长重复串
- **滚动哈希匹配**：如 Rabin-Karp 字符串匹配，用滑动窗口维护滚动哈希值

> **核心标志**：题目要求找「连续子数组/子串」且暴力法需要两层循环枚举所有子数组——这就是滑动窗口的信号。

## 核心模式

滑动窗口本质是维护一个 `[left, right)` 区间，通过**右指针扩张、左指针收缩**来动态调整窗口。所有滑动窗口问题都遵循同一个骨架：

```python
left, right = 0, 0
while right < len(arr):
    window.add(arr[right])   # 扩大窗口
    right += 1

    while need_shrink(window):  # 窗口不满足条件时收缩
        window.remove(arr[left])
        left += 1

    # 此时窗口满足条件，更新答案
    update_result()
```

**三种窗口形态：**

| 形态 | 收缩条件 | 何时更新答案 | 典型场景 |
|------|---------|-------------|---------|
| 不定长—求最长 | 窗口不合法时收缩 | 收缩完成后（窗口合法） | 无重复字符的最长子串、最大连续 1 |
| 不定长—求最短 | 窗口合法时收缩 | 收缩过程中（窗口从合法变为不合法之前） | 最小覆盖子串、长度最小的子数组 |
| 定长窗口 | 窗口大小超过固定长度时收缩 | 窗口恰好等于固定长度时 | 字符串排列、字母异位词、Rabin-Karp |

> **关键区分**：求最长 → 收缩后更新；求最短 → 收缩时更新。两者差一个缩进位置。

---

## 目录
- [最小覆盖子串](#最小覆盖子串)
- [无重复字符的最长子串](#无重复字符的最长子串)
- [长度最小的子数组](#长度最小的子数组)
- [字符串的排列](#字符串的排列)
- [找到字符串中所有字母异位词](#找到字符串中所有字母异位词)
- [乘积小于 K 的子数组](#乘积小于k的子数组)
- [最大连续 1 的个数 III](#最大连续1的个数iii)
- [替换后的最长重复字符](#替换后的最长重复字符)
- [存在重复元素 II](#存在重复元素ii)
- [存在重复元素 III](#存在重复元素iii)
- [将 x 减到 0 的最小操作数](#将x减到0的最小操作数)
- [至少有 K 个重复字符的最长子串](#至少有k个重复字符的最长子串)
- [Rabin-Karp 字符串匹配算法](#rabin-karp-字符串匹配算法)

---

## 最小覆盖子串

**LeetCode 76** | 难度：困难

### 题目描述

给你一个字符串 s 和一个字符串 t，返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，返回空字符串 ""。t 中可能会有重复字符，子串中每个字符的出现次数必须不少于 t 中的次数。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `s = "ADOBECODEBANC", t = "ABC"` | `"BANC"` | 最短的覆盖子串 |
| `s = "a", t = "a"` | `"a"` | 单字符匹配 |
| `s = "a", t = "aa"` | `""` | s 中不够两个 'a' |

### 思路

不确定长度的滑动窗口求最短。维护 `window` 字典记录窗口内各字符出现次数，`need` 字典记录 t 的需求。当窗口覆盖了所有 need 中的字符（每个字符的数量 >= 需求），尝试收缩左侧找更短的解。

收缩过程中持续更新最短答案，直到窗口不再满足覆盖条件。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 滑动窗口 + 双字典 | 中 | O(n) | 首选 |
| 滑动窗口 + 优化 check（计数匹配数） | 中高 | O(n) | 更高效 |
| 暴力枚举 | 低 | O(n²) | 超时 |

### Python 实现

```python
from collections import defaultdict


class Solution:
    def min_window(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = defaultdict(int)
        for ch in t:
            need[ch] += 1

        left, right = 0, 0
        res_start, res_len = 0, float("inf")

        while right < len(s):
            ch = s[right]
            window[ch] += 1
            right += 1

            while self._covered(window, need):
                if right - left < res_len:
                    res_start, res_len = left, right - left
                ch = s[left]
                window[ch] -= 1
                left += 1

        return s[res_start:res_start + res_len] if res_len != float("inf") else ""

    def _covered(self, window, need):
        for ch, num in need.items():
            if window[ch] < num:
                return False
        return True
```

> 优化点：用 `valid` 计数器记录已满足的字符种类数，避免每次都遍历 need 字典检查覆盖状态。

---

## 无重复字符的最长子串

**LeetCode 3** | 难度：中等

### 题目描述

给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `s = "abcabcbb"` | `3` | 最长无重复子串 "abc" |
| `s = "bbbbb"` | `1` | 最长无重复子串 "b" |
| `s = "pwwkew"` | `3` | 最长无重复子串 "wke" |

### 思路

不定长窗口求最长。右指针不断扩张，当新加入的字符使窗口出现重复（该字符计数 >= 2）时，收缩左指针直到该字符计数回到 1。每次窗口合法时更新最大长度。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 滑动窗口 + 哈希表 | 低 | O(n) | 首选 |
| 滑动窗口 + 字符下标跳跃 | 中 | O(n) | 更高效（左指针可一次跳到重复位置后） |
| 暴力枚举 | 低 | O(n²) | 不推荐 |

### Python 实现

```python
from collections import defaultdict


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        window = defaultdict(int)
        left, right = 0, 0
        res = 0

        while right < len(s):
            ch = s[right]
            window[ch] += 1
            right += 1

            while window[ch] >= 2:  # 出现重复，需要收缩
                ch_ = s[left]
                window[ch_] -= 1
                left += 1

            res = max(res, right - left)

        return res
```

> 求最长 → 收缩完成后（窗口合法时）更新答案。

---

## 长度最小的子数组

**LeetCode 209** | 难度：中等

### 题目描述

给定一个含有 n 个正整数的数组和一个正整数 target，找出该数组中满足其总和大于等于 target 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `target = 7, nums = [2,3,1,2,4,3]` | `2` | 子数组 `[4,3]` 长度最小 |
| `target = 4, nums = [1,4,4]` | `1` | 单个元素 4 即满足 |
| `target = 11, nums = [1,1,1,1,1,1,1,1]` | `0` | 总和远不足 target |

### 思路

不定长窗口求最短。右指针扩张累加和，当 `window_sum >= target` 时收缩左指针，收缩过程中记录最小长度。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 滑动窗口 | 低 | O(n) | 首选 |
| 前缀和 + 二分查找 | 中 | O(n log n) | 也可 |
| 暴力枚举 | 低 | O(n²) | 超时 |

### Python 实现

```python
from typing import List


class Solution:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        left, right = 0, 0
        res = float("inf")

        while right < len(nums):
            window_sum += nums[right]
            right += 1

            while window_sum >= target:
                res = min(res, right - left)
                window_sum -= nums[left]
                left += 1

        return res if res != float("inf") else 0
```

> 求最短 → 收缩过程中（窗口合法时）更新答案。这和最长子串刚好相反。

---

## 字符串的排列

**LeetCode 567** | 难度：中等

### 题目描述

给你两个字符串 s1 和 s2，判断 s2 是否包含 s1 的排列。如果是，返回 true；否则返回 false。换句话说，s1 的排列之一是 s2 的子串。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `s1 = "ab", s2 = "eidbaooo"` | `true` | s2 包含 "ba"，是 "ab" 的排列 |
| `s1 = "ab", s2 = "eidboaoo"` | `false` | "ab" 的排列 "ab"/"ba" 都不是 s2 的子串 |

### 思路

定长滑动窗口。窗口长度固定为 `len(s1)`，当窗口长度等于 `len(s1)` 时检查窗口字符计数是否与 s1 完全匹配。每次窗口移动时右进左出，始终保持定长。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 定长滑动窗口 | 低 | O(n) | 首选 |
| 暴力枚举 + 排序比较 | 低 | O(n·m log m) | 不推荐 |

### Python 实现

```python
from collections import defaultdict


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        need = defaultdict(int)
        for ch in s1:
            need[ch] += 1

        left, right = 0, 0

        while right < len(s2):
            ch = s2[right]
            window[ch] += 1
            right += 1

            while right - left == len(s1):  # 定长窗口收缩条件
                if self._matches(window, need):
                    return True
                ch = s2[left]
                window[ch] -= 1
                if window[ch] == 0:
                    del window[ch]
                left += 1

        return False

    def _matches(self, window, need):
        if len(window) != len(need):
            return False
        for ch, num in need.items():
            if window[ch] != need[ch]:
                return False
        return True
```

> 定长窗口的标志：收缩条件为 `right - left == window_size`，答案在窗口长度恰好等于目标时判断。

---

## 找到字符串中所有字母异位词

**LeetCode 438** | 难度：中等

### 题目描述

给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。异位词指由相同字母重排列形成的字符串（包括相同的字符串）。不考虑答案输出的顺序。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `s = "cbaebabacd", p = "abc"` | `[0,6]` | 子串 "cba"（下标 0）和 "bac"（下标 6） |
| `s = "abab", p = "ab"` | `[0,1,2]` | 子串 "ab", "ba", "ab" 都是 "ab" 的异位词 |

### 思路

与「字符串的排列」几乎相同，不同之处在于这里是找到所有匹配的起始位置而非仅判断是否存在。同样是定长窗口，当窗口字符计数与 p 匹配时记录左指针位置。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 定长滑动窗口 | 低 | O(n) | 首选 |
| 暴力枚举 + 排序 | 低 | O(n·m log m) | 不推荐 |

### Python 实现

```python
from collections import defaultdict
from typing import List


class Solution:
    def find_anagrams(self, s: str, p: str) -> List[int]:
        window = defaultdict(int)
        need = defaultdict(int)
        for ch in p:
            need[ch] += 1

        left, right = 0, 0
        res = []

        while right < len(s):
            ch = s[right]
            window[ch] += 1
            right += 1

            while right - left == len(p):
                if self._matches(window, need):
                    res.append(left)
                ch = s[left]
                window[ch] -= 1
                if window[ch] == 0:
                    del window[ch]
                left += 1

        return res

    def _matches(self, window, need):
        if len(window) != len(need):
            return False
        for ch, num in need.items():
            if window[ch] != need[ch]:
                return False
        return True
```

> 本质上就是「字符串的排列」的变体，将 bool 返回值改为收集所有匹配位置。

---

## 乘积小于 K 的子数组

**LeetCode 713** | 难度：中等

### 题目描述

给定一个正整数数组 nums 和一个整数 k，返回乘积小于 k 的连续子数组的个数。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [10,5,2,6], k = 100` | `8` | 8 个乘积小于 100 的子数组：`[10]`,`[5]`,`[2]`,`[6]`,`[10,5]`,`[5,2]`,`[2,6]`,`[5,2,6]` |
| `nums = [1,2,3], k = 0` | `0` | k 为 0，无正整数乘积 < 0 |

### 思路

不定长窗口求个数。右指针扩张累积乘积，当 `product >= k` 时收缩左指针。每次窗口合法时，以 `right - 1` 为右端点的所有合法子数组数量恰好为 `right - left`。

关键洞察：当 `[left, right)` 的乘积 < k 时，以 `right-1` 结尾、从 `left..right-1` 任一位置开头的子数组都合法——共 `right - left` 个。

### Python 实现

```python
from typing import List


class Solution:
    def num_subarray_product_less_than_k(
        self, nums: List[int], k: int
    ) -> int:
        if k <= 1:
            return 0

        product = 1
        left, right = 0, 0
        res = 0

        while right < len(nums):
            product *= nums[right]
            right += 1

            while product >= k:
                product //= nums[left]
                left += 1

            res += right - left

        return res
```

> 核心技巧：`res += right - left`——以 `right-1` 为右端点的合法子数组个数。`k <= 1` 直接返回 0 是边界优化。

---

## 最大连续 1 的个数 III

**LeetCode 1004** | 难度：中等

### 题目描述

给定一个由若干 0 和 1 组成的数组 nums，以及一个整数 k。最多可以将 k 个 0 翻转成 1，求翻转后数组中最长连续 1 的子数组长度。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2` | `6` | 翻转下标 3 和 4 的 0 后，最长连续 1 为 `[1,1,1,1,1,1]` |
| `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3` | `10` | 翻转 3 个 0 后得到最长连续 1 |

### 思路

不定长窗口求最长。将问题转化为：找最长的子数组，使得其中 0 的个数不超过 k。窗口内统计 0 的个数，超过 k 时收缩左指针。

### Python 实现

```python
from typing import List


class Solution:
    def longest_ones(self, nums: List[int], k: int) -> int:
        zeros = 0
        left, right = 0, 0
        res = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            right += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            res = max(res, right - left)

        return res
```

> 转化思维：不真的翻转元素，而是统计窗口内 0 的个数，允许不超过 k 个 0 存在于窗口中。

---

## 替换后的最长重复字符

**LeetCode 424** | 难度：中等

### 题目描述

给你一个字符串 s 和一个整数 k，你可以将字符串中任意 k 个字符替换成任何其他字符。在执行最多 k 次替换后，返回包含相同字母的最长子串的长度。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `s = "ABAB", k = 2` | `4` | 替换两个 'A' 或两个 'B'，整个字符串变成相同字符 |
| `s = "AABABBA", k = 1` | `4` | 替换中间的一个 'A' 或一个 'B'，得到 "AABBBBA" 中 "BBBB" 长度为 4 |

### 思路

不定长窗口求最长。窗口合法的条件是：窗口长度 - 窗口内出现次数最多的字符数 <= k（即需要替换的字符数不超过 k）。当不满足条件时收缩左指针。

优化：不需要每次都重新计算窗口内出现次数最多的字符数，可以维护 `max_freq` 变量。因为只有 `max_freq` 增大时才可能得到更长的结果，所以 `max_freq` 只需单调不减即可。

### Python 实现

```python
from collections import defaultdict


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        max_freq = 0
        left, right = 0, 0
        res = 0

        while right < len(s):
            ch = s[right]
            window[ch] += 1
            max_freq = max(max_freq, window[ch])
            right += 1

            while (right - left) - max_freq > k:
                ch = s[left]
                window[ch] -= 1
                left += 1

            res = max(res, right - left)

        return res
```

> 核心条件：`window_length - max_freq <= k`。需要替换的字符 = 总长度 - 最多的同种字符数。

---

## 存在重复元素 II

**LeetCode 219** | 难度：简单

### 题目描述

给你一个整数数组 nums 和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k`。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,2,3,1], k = 3` | `true` | nums[0]=nums[3]=1，间距 3 <= 3 |
| `nums = [1,0,1,1], k = 1` | `true` | nums[2]=nums[3]=1，间距 1 <= 1 |
| `nums = [1,2,3,1,2,3], k = 2` | `false` | 所有重复元素的间距都 > 2 |

### 思路

定长滑动窗口（窗口最大长度为 k+1）。右指针扩张加入元素，如果新元素在窗口中已存在则找到答案。当窗口长度 > k 时收缩左指针，移除最左侧元素。

也可以直接用哈希表记录每个元素最近出现的位置，更简单。但滑动窗口版本展示了如何用窗口维护「最近 k 个元素」。

### Python 实现

```python
from collections import defaultdict
from typing import List


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        window = defaultdict(int)
        left, right = 0, 0

        while right < len(nums):
            num = nums[right]
            window[num] += 1
            right += 1

            while right - left > k + 1:
                num_ = nums[left]
                window[num_] -= 1
                left += 1

            if window[num] > 1:
                return True

        return False
```

> 此题最优解是哈希表记录最近下标——O(n) 时间 O(k) 空间且无需滑动窗口的收缩逻辑。但滑动窗口版本是展示窗口思维的练习。

---

## 存在重复元素 III

**LeetCode 220** | 难度：困难

### 题目描述

给你一个整数数组 nums 和两个整数 indexDiff 和 valueDiff。找出满足以下条件的下标对 (i, j)：`i != j`，`abs(i - j) <= indexDiff`，且 `abs(nums[i] - nums[j]) <= valueDiff`。如果存在返回 true，否则返回 false。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,2,3,1], indexDiff = 3, valueDiff = 0` | `true` | nums[0]=nums[3]=1，下标差 3，值差 0 |
| `nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3` | `false` | 所有满足下标差的元素对，值差都不满足 |

### 思路

滑动窗口 + 桶排序。将窗口内元素按 `valueDiff + 1` 的大小分桶：元素 `x` 的桶号为 `x // (valueDiff + 1)`。如果两个元素落在同一个桶，它们的差值一定 <= valueDiff；落在相邻桶也可能差值 <= valueDiff，需要额外检查。

滑动窗口维护最近 `indexDiff` 个元素，新元素入窗时检查同桶和相邻桶即可。

### Python 实现

```python
from typing import List


class Solution:
    def contains_nearby_almost_duplicate(
        self, nums: List[int], index_diff: int, value_diff: int
    ) -> bool:
        bucket = {}
        width = value_diff + 1
        left, right = 0, 0

        while right < len(nums):
            num = nums[right]
            bid = num // width

            if bid in bucket:
                return True
            if bid - 1 in bucket and num - bucket[bid - 1] <= value_diff:
                return True
            if bid + 1 in bucket and bucket[bid + 1] - num <= value_diff:
                return True

            bucket[bid] = num
            right += 1

            while right - left > index_diff:
                num_ = nums[left]
                bid_ = num_ // width
                if bid_ in bucket and bucket[bid_] == num_:
                    del bucket[bid_]
                left += 1

        return False
```

> 桶宽度 `valueDiff + 1` 是关键：保证桶内任意两个元素的差 <= valueDiff。窗口收缩时注意桶的清理逻辑。

---

## 将 x 减到 0 的最小操作数

**LeetCode 1658** | 难度：中等

### 题目描述

给你一个整数数组 nums 和一个整数 x。每一次操作，你应当移除数组最左边或最右边的元素，然后从 x 中减去该元素的值。如果可以将 x 恰好减到 0，返回最小操作数；否则返回 -1。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `nums = [1,1,4,2,3], x = 5` | `2` | 移除最右边的 3 和最右边的 2：3+2=5，操作数 2 |
| `nums = [5,6,7,8,9], x = 4` | `-1` | 无法恰好减到 0 |
| `nums = [3,2,20,1,1,3], x = 10` | `5` | 移除左边 3+2 和右边 1+1+3 = 10，操作数 5 |

### 思路

逆向思维：移除左右两端元素等价于保留一个中间连续子数组，使得子数组和为 `sum(nums) - x`。问题转化为找最长的中间子数组使其和为 `target = sum - x`。

用滑动窗口维护 `window_sum`，当 `window_sum > target` 时收缩，等于时更新最长长度。最终答案 = `n - max_len`。

### Python 实现

```python
from typing import List


class Solution:
    def min_operations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)

        window_sum = 0
        left, right = 0, 0
        max_len = -1

        while right < len(nums):
            window_sum += nums[right]
            right += 1

            while window_sum > target and left < right:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                max_len = max(max_len, right - left)

        return len(nums) - max_len if max_len != -1 else -1
```

> 关键转化：移除两端 → 保留中间最长合法子数组。做完转化后就是标准的「和为 target 的最长子数组」。

---

## 至少有 K 个重复字符的最长子串

**LeetCode 395** | 难度：中等

### 题目描述

给你一个字符串 s 和一个整数 k，请你找出 s 中的最长子串，要求该子串中的每个字符出现次数都不少于 k。返回这一子串的长度。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `s = "aaabb", k = 3` | `3` | 最长子串 "aaa"，其中 'a' 出现 3 次 |
| `s = "ababbc", k = 2` | `5` | 最长子串 "ababb"，其中 'a' 出现 2 次，'b' 出现 3 次 |
| `s = "aaabbb", k = 3` | `6` | 整个字符串满足条件 |

### 思路

直接滑动窗口不可行——不知道何时扩张、何时收缩（窗口合法性无法单调地随扩张/收缩变化）。

**解法一（推荐）**：枚举窗口内可能出现的不同字符种类数（1 到 26），将问题转化为「窗口内恰好有 n 种不同字符，且每种出现次数 >= k」的最长子串。这样窗口的收缩条件变为「不同字符种类数 > n」，恢复了单调性。

**解法二**：分治法。找到出现次数 < k 的字符作为分隔点，递归处理各段。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 枚举字符种类 + 滑动窗口 | 中 | O(26·n) | 首选，展示了转化思维 |
| 分治 | 中 | O(n·log n) | 可作为备选方案 |

### Python 实现

```python
from collections import defaultdict


class Solution:
    def longest_substring(self, s: str, k: int) -> int:
        res = 0
        for target_kinds in range(1, 27):
            res = max(
                res, self._longest_with_n_kinds(s, k, target_kinds)
            )
        return res

    def _longest_with_n_kinds(self, s: str, k: int, target_kinds: int) -> int:
        window = defaultdict(int)
        left, right = 0, 0
        valid_kinds = 0  # 满足 >= k 的字符种类数
        res = 0

        while right < len(s):
            ch = s[right]
            window[ch] += 1
            if window[ch] == k:
                valid_kinds += 1
            right += 1

            while len(window) > target_kinds:
                ch = s[left]
                if window[ch] == k:
                    valid_kinds -= 1
                window[ch] -= 1
                if window[ch] == 0:
                    del window[ch]
                left += 1

            if valid_kinds == target_kinds:
                res = max(res, right - left)

        return res
```

> 此题展示了滑动窗口的一个进阶技巧：当窗口合法性不单调时，通过**枚举某种维度**（如字符种类数）使其恢复单调性。

---

## Rabin-Karp 字符串匹配算法

**LeetCode 28（相关）** | 难度：算法模板

### 题目描述

在文本串 txt 中查找模式串 pat 的首次出现位置。使用滚动哈希在 O(n) 时间内完成匹配，避免每次截取子串的 O(m) 开销。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `txt = "hello", pat = "ll"` | `2` | "ll" 在位置 2 |
| `txt = "aaaaa", pat = "bba"` | `-1` | 不存在匹配 |
| `txt = "abcab", pat = "cab"` | `2` | 在位置 2 匹配 |

### 思路

定长滑动窗口 + 滚动哈希。将字符串视为以 256 为基的数字，用取模避免溢出。新字符入窗：`hash = (R * hash + new_char) % Q`；旧字符出窗：`hash = (hash - old_char * R^(L-1)) % Q`。

哈希值相等时再逐字符比对，防止哈希冲突。

### Python 实现

```python
def rabin_karp(txt: str, pat: str) -> int:
    L = len(pat)
    R = 256        # 进制
    Q = 1658598167  # 大素数取模

    # 预计算 R^(L-1) % Q
    RL = 1
    for _ in range(1, L):
        RL = (RL * R) % Q

    # 计算模式串哈希
    pat_hash = 0
    for ch in pat:
        pat_hash = (R * pat_hash + ord(ch)) % Q

    # 滑动窗口
    window_hash = 0
    left, right = 0, 0

    while right < len(txt):
        window_hash = (R * window_hash + ord(txt[right])) % Q
        right += 1

        if right - left == L:
            if window_hash == pat_hash:
                if pat == txt[left:right]:  # 防哈希冲突
                    return left

            # 移除左侧字符
            window_hash = (window_hash - ord(txt[left]) * RL % Q + Q) % Q
            left += 1

    return -1
```

> 定长窗口 + 自定义哈希 = Rabin-Karp。`+ Q` 的技巧保证了取模结果的非负性。实际工程中 Python 的字符串切片已经足够快，但 Rabin-Karp 的思想广泛应用于各类字符串匹配和查重场景。

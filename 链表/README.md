# 链表算法

## 适用场景

链表算法主要考察指针操作和边界处理能力，常见于以下问题类型：

- **链表遍历与修改**：反转链表（全部/部分）、删除节点、分割链表——核心是维护 `prev/cur/next` 指针关系
- **快慢指针**：找中点、判断环、找环的入口、删除倒数第 K 个节点——利用速度差或路程差
- **多路归并**：合并两个或 K 个有序链表——小顶堆实现 O(N log K) 的 K 路归并
- **数学运算模拟**：两个链表表示的大数相加（正序/逆序存储）——模拟竖式加法，注意进位
- **回文/对称性判断**：判断回文链表——找中点 + 反转后半段 + 比较
- **链表重组**：旋转链表、重排链表——连接成环或定位分割点

> **核心守则**：链表题的头号陷阱是指针丢失和成环。使用哑节点（dummy node）可统一头节点的特殊处理；修改 `next` 指针前先保存后续节点的引用；操作完成后检查是否会形成环。

## 核心技巧速查

| 技巧 | 典型场景 |
|------|---------|
| 快慢指针 | 找中点、判环、倒数第 k 个节点 |
| 哑节点 (dummy) | 简化头节点变动的逻辑 |
| 递归反转 | 反转整个链表 / 前 N 个 / 范围 |
| 多路归并 (堆) | 合并 K 个有序链表 |
| 栈 | 处理需要从后往前操作的场景 |

---

## 目录
- [使用链表实现的两数加法](#使用链表实现的两数加法)
- [使用链表实现的两数加法 II](#使用链表实现的两数加法-ii)
- [分割链表](#分割链表)
- [删除单链表的倒数第 K 个节点](#删除单链表的倒数第k个节点)
- [删除排序链表中的重复元素 II](#删除排序链表中的重复元素-ii)
- [单链表的中间节点](#单链表的中间节点)
- [反转链表](#反转链表)
- [反转范围链表](#反转范围链表)
- [合并两个有序链表](#合并两个有序链表)
- [合并 K 个有序链表](#合并k个有序链表)
- [回文链表](#回文链表)
- [旋转链表](#旋转链表)
- [环形链表的起始点](#环形链表的起始点)
- [相交链表](#相交链表)

---

## 使用链表实现的两数加法

**LeetCode 2** | 难度：中等

### 题目描述

给你两个**非空**的链表，表示两个非负的整数。它们每位数字都是按照**逆序**的方式存储的（个位在头节点），每个节点只存储一位数字。请你将两个数相加，并以相同链表形式返回它们的和。你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `l1 = [2,4,3]`, `l2 = [5,6,4]` | `[7,0,8]` | 342 + 465 = 807 |
| `l1 = [0]`, `l2 = [0]` | `[0]` | 0 + 0 = 0 |
| `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]` | `[8,9,9,9,0,0,0,1]` | 所有位都进位 |

### 思路

链表是逆序存储的（个位在头节点），天然适合从低位向高位逐位相加。同时遍历两个链表，维护进位 `carry`，每次 `sum = val1 + val2 + carry`，当前位 `= sum % 10`，进位 `= sum // 10`。

关键：循环终止条件是「两个链表都空 AND 进位为 0」，否则会漏掉最高位的进位。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 模拟竖式加法 | 低 | O(max(m,n)) | 首选 |

此题解法唯一，唯一需要注意的是不要忘记最后的进位。

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

        return dummy.next
```

---

## 使用链表实现的两数加法 II

**LeetCode 445** | 难度：中等

### 题目描述

给你两个**非空**的链表，表示两个非负的整数。与 LeetCode 2 不同，这里每位数字按照**正序**的方式存储（高位在头节点）。请你将两个数相加，并以相同链表形式返回它们的和。你不能反转输入的链表。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `l1 = [7,2,4,3]`, `l2 = [5,6,4]` | `[7,8,0,7]` | 7243 + 564 = 7807 |
| `l1 = [2,4,3]`, `l2 = [5,6,4]` | `[8,0,7]` | 243 + 564 = 807 |
| `l1 = [0]`, `l2 = [0]` | `[0]` | 0 + 0 = 0 |

### 思路

与题目「两数加法」的区别在于链表是正序存储的（高位在头节点）。需要从低位加起，所以用两个**栈**把链表元素倒过来，再从栈顶（低位）逐位相加，结果用**头插法**构建新链表。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 双栈 + 头插法 | 低 | O(m+n) 时间 O(m+n) 空间 | 首选 |
| 反转两个链表后再加 | 中 | O(m+n) 时间 O(1) 空间 | 可以，但需恢复原链表 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        dummy = ListNode(-1)
        carry = 0

        while stack1 or stack2 or carry:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()

            carry = total // 10
            # 头插法
            new_node = ListNode(total % 10)
            new_node.next = dummy.next
            dummy.next = new_node

        return dummy.next
```

---

## 分割链表

**LeetCode 86** | 难度：中等

### 题目描述

给你一个链表的头节点 `head` 和一个特定值 `x`，请你对链表进行分隔，使得所有**小于** `x` 的节点都出现在**大于或等于** `x` 的节点之前。你应当**保留**两个分区中每个节点的初始相对位置。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,4,3,2,5,2]`, `x = 3` | `[1,2,2,4,3,5]` | 小于3的元素保持相对顺序 |
| `head = [2,1]`, `x = 2` | `[1,2]` | 小于2的移到前面 |
| `head = [1,4,3,2,5,2]`, `x = 5` | `[1,4,3,2,2,5]` | 所有元素都小于5 |

### 思路

创建两个哑节点分别作为「小于 x」和「大于等于 x」的链表头。遍历原链表，根据值的大小分流到两个链表中，最后把小链表的尾部指向大链表的头部。

关键：分流时**必须断开原节点的 next 指针**，否则会产生环。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 双哑节点分流 | 低 | O(n) | 首选 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def partition(
        self, head: Optional[ListNode], x: int
    ) -> Optional[ListNode]:
        left_dummy = ListNode(-1)
        right_dummy = ListNode(-1)
        left = left_dummy
        right = right_dummy

        cur = head
        while cur:
            next_node = cur.next
            cur.next = None  # 断开，避免残留指针造成环
            if cur.val < x:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next
            cur = next_node

        left.next = right_dummy.next
        return left_dummy.next
```

---

## 删除单链表的倒数第 K 个节点

**LeetCode 19** | 难度：中等

### 题目描述

给你一个链表，删除链表的倒数第 `n` 个节点，并且返回链表的头节点。要求使用一遍扫描实现。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,3,4,5]`, `n = 2` | `[1,2,3,5]` | 删除倒数第2个节点4 |
| `head = [1]`, `n = 1` | `[]` | 删除唯一节点 |
| `head = [1,2]`, `n = 1` | `[1]` | 删除倒数第1个节点2 |

### 思路

快慢指针：快指针先走 `n+1` 步（因为要删除倒数第 n 个，需要定位到倒数第 `n+1` 个的前驱），然后快慢一起走，快指针到末尾时慢指针正好在待删节点的前驱。

哑节点可以统一「删除头节点」和「删除中间节点」的处理逻辑。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 快慢指针（一遍扫描） | 低 | O(n) | 首选 |
| 两次遍历（先计长再定位） | 低 | O(n) | 可接受但不优雅 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def remove_nth_from_end(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast = slow = dummy

        # 快指针先走 n+1 步
        for _ in range(n + 1):
            fast = fast.next

        # 一起走到底
        while fast:
            fast = fast.next
            slow = slow.next

        # slow 指向待删节点的前驱
        slow.next = slow.next.next
        return dummy.next
```

---

## 删除排序链表中的重复元素 II

**LeetCode 82** | 难度：中等

### 题目描述

给定一个已排序的链表的头节点 `head`，删除原始链表中所有重复出现数字的节点，只留下**没有重复**的数字。返回同样排序的结果链表。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,3,3,4,4,5]` | `[1,2,5]` | 3和4重复，全部删除 |
| `head = [1,1,1,2,3]` | `[2,3]` | 1重复，全部删除 |
| `head = [1,2,3,4]` | `[1,2,3,4]` | 没有重复元素 |

### 思路

维护两个哑节点链：一个收集「唯一的」节点，一个收集「重复的」节点。遍历时，如果当前节点值与下一个节点值相同，或与上一个重复节点的值相同，就归入重复链；否则归入唯一链。

最后断开两个链尾的 next 指针，防止带回无效节点。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 双哑节点分流 | 中 | O(n) | 可行 |
| 直接跳过重复段 | 中 | O(n) | 更简洁 |

更简洁的做法是直接跳过：当发现 `cur.val == cur.next.val` 时，内循环跳过所有相同值，然后把前驱指向下一段。

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def delete_duplicates(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy

        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                dup_val = prev.next.val
                # 跳过所有等于 dup_val 的节点
                while prev.next and prev.next.val == dup_val:
                    prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next
```

---

## 单链表的中间节点

**LeetCode 876** | 难度：简单

### 题目描述

给定一个带有头节点 `head` 的非空单链表，返回链表的中间节点。如果有两个中间节点（链表长度为偶数），则返回**第二个**中间节点。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,3,4,5]` | `[3,4,5]` | 第3个节点3是中间节点 |
| `head = [1,2,3,4,5,6]` | `[4,5,6]` | 偶数长度，返回第4个节点4 |
| `head = [1]` | `[1]` | 单节点链表 |

### 思路

快慢指针：fast 每次走两步，slow 每次走一步。fast 到末尾时 slow 在中间。

细节：偶数量时返回第二个中间节点。当 `fast.next is None`（奇数个）时 slow 就是中点；当 `fast.next.next is None`（偶数个）时需返回 `slow.next`。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 快慢指针 | 低 | O(n) 时间 O(1) 空间 | 首选 |
| 计数后走一半 | 低 | O(n) 两遍扫描 | 次选 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
```

> 如果要求返回第一个中间节点（偶数时偏左），初始化 `fast = head.next` 即可。

---

## 反转链表

**LeetCode 206** | 难度：简单

### 题目描述

给你单链表的头节点 `head`，请你反转链表，并返回反转后的链表。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,3,4,5]` | `[5,4,3,2,1]` | 完全反转 |
| `head = [1,2]` | `[2,1]` | 两个节点反转 |
| `head = []` | `[]` | 空链表 |

### 思路

**迭代法**：维护 `prev / cur / next` 三个指针，每次将 `cur.next` 指回 `prev`，然后三指针一起右移。

**递归法**：假设 `head.next` 已反转好，只需把 `head` 接到尾部即可。反转后原 `head.next` 成为新链表的尾节点。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 迭代法 | 低 | O(n) 时间 O(1) 空间 | 首选，面试高频 |
| 递归法 | 中 | O(n) 时间 O(n) 栈空间 | 理解递归思想时使用 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev
```

---

## 反转范围链表

**LeetCode 92** | 难度：中等

### 题目描述

给你单链表的头节点 `head` 和两个整数 `left` 和 `right`，其中 `left <= right`。请你反转从位置 `left` 到位置 `right` 的链表节点，返回反转后的链表。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,3,4,5]`, `left = 2`, `right = 4` | `[1,4,3,2,5]` | 反转区间[2,4] |
| `head = [5]`, `left = 1`, `right = 1` | `[5]` | 反转单节点 |
| `head = [3,5]`, `left = 1`, `right = 2` | `[5,3]` | 反转整个链表 |

### 思路

定位到 `left-1` 位置（前驱），然后调用「反转前 N 个节点」的子函数反转 `[left, right]` 范围，最后把前驱接回反转后的子链表头。

当 `left == 1` 时没有前驱，直接反转前 `right` 个节点即可。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 定位前驱 + 反转前 N 个 | 中 | O(n) | 首选，模块化思路 |
| 头插法（穿针引线） | 中 | O(n) | 也可以 |
| 截断 + 反转 + 接回 | 中 | O(n) | 直观但需额外变量 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def reverse_between(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == 1:
            return self._reverse_n(head, right)

        prev = head
        for _ in range(left - 2):
            prev = prev.next

        prev.next = self._reverse_n(prev.next, right - left + 1)
        return head

    def _reverse_n(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """反转链表的前 n 个节点，返回新头。"""
        if not head or not head.next:
            return head

        prev, cur = None, head
        for _ in range(n):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # head 现在是反转后的尾节点，接上剩余部分
        head.next = cur
        return prev
```

---

## 合并两个有序链表

**LeetCode 21** | 难度：简单

### 题目描述

将两个升序链表合并为一个新的**升序**链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `l1 = [1,2,4]`, `l2 = [1,3,4]` | `[1,1,2,3,4,4]` | 合并两个有重复元素的链表 |
| `l1 = []`, `l2 = []` | `[]` | 两个空链表 |
| `l1 = []`, `l2 = [0]` | `[0]` | 一个为空 |

### 思路

用哑节点简化头节点处理。两个指针分别遍历两条链，每次取较小的节点接到结果链尾部。最后把剩余未遍历完的链整体接入。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 哑节点 + 双指针 | 低 | O(m+n) | 首选 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 接上剩余部分
        cur.next = list1 if list1 else list2
        return dummy.next
```

---

## 合并 K 个有序链表

**LeetCode 23** | 难度：困难

### 题目描述

给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `lists = [[1,4,5],[1,3,4],[2,6]]` | `[1,1,2,3,4,4,5,6]` | 合并3个有序链表 |
| `lists = []` | `[]` | 空数组 |
| `lists = [[],[1]]` | `[1]` | 含空链表的数组 |

### 思路

用小顶堆做「多路归并」。每个链表当前节点入堆（需要放入 `(val, index, node)` 三元组，`index` 用来打破值相等时的比较——`ListNode` 不可比较）。

每次弹出最小节点接到结果链，然后该节点所在链表的下一个节点入堆。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 小顶堆多路归并 | 中 | O(N log K)，N 为总节点数 | 首选 |
| 两两合并 | 中 | O(N K) 或 O(N log K) 分治 | 次选 |

### Python 实现

```python
import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def merge_k_lists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        min_heap = []

        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, idx, head))

        dummy = ListNode(-1)
        cur = dummy

        while min_heap:
            _, idx, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(
                    min_heap, (node.next.val, idx, node.next)
                )

        return dummy.next
```

> 注意 `while not pq` 是原代码的 bug——应该用 `while pq`。

---

## 回文链表

**LeetCode 234** | 难度：简单

### 题目描述

给你一个单链表的头节点 `head`，请你判断该链表是否为回文链表。如果是，返回 `true`；否则，返回 `false`。要求使用 O(n) 时间和 O(1) 空间。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,2,1]` | `true` | 对称链表 |
| `head = [1,2]` | `false` | 不对称 |
| `head = [1]` | `true` | 单节点视为回文 |

### 思路

经典解法：找中点 → 反转后半段 → 前后两段逐一比较 → 恢复链表（可选）。这样用 O(1) 空间。

原代码用了栈（O(n) 空间），虽然正确但不够优化。下面给出 O(1) 空间的解法。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 中点 + 反转后半 + 比较 | 中 | O(n) 时间 O(1) 空间 | 首选，展示优化意识 |
| 栈 | 低 | O(n) 时间 O(n) 空间 | 快速 AC 可用 |
| 复制到数组 + 双指针 | 低 | O(n) 时间 O(n) 空间 | 简单但有空间开销 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1. 快慢指针找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半段
        second_half = self._reverse(slow)

        # 3. 比较
        first, second = head, second_half
        result = True
        while second:
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next

        # 4. 可选：恢复后半段
        self._reverse(second_half)

        return result

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
```

---

## 旋转链表

**LeetCode 61** | 难度：中等

### 题目描述

给你一个链表的头节点 `head`，旋转链表，将链表每个节点向右移动 `k` 个位置。即原本的第 `len - k` 个节点成为新的头节点，原尾节点与原头节点相连。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [1,2,3,4,5]`, `k = 2` | `[4,5,1,2,3]` | 每个节点右移2位 |
| `head = [0,1,2]`, `k = 4` | `[2,0,1]` | k大于链表长度，等效k=1 |
| `head = [1,2]`, `k = 1` | `[2,1]` | 右移1位 |

### 思路

先将链表连成环（尾节点 next 指向头节点），然后计算需要断开的位置 `len - k % len`。从断开位置的前驱切断环，返回新的头节点。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 连成环 + 定位切断 | 低 | O(n) | 首选 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node


class Solution:
    def rotate_right(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 计算长度并找到尾节点
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 连成环
        tail.next = head

        # 找新尾节点：从 head 走 length - k%length - 1 步
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
```

---

## 环形链表的起始点

**LeetCode 142** | 难度：中等

### 题目描述

给定一个链表的头节点 `head`，返回链表开始入环的第一个节点。如果链表无环，则返回 `null`。不允许修改链表。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `head = [3,2,0,-4]`, 尾节点指向第2个节点 | `节点值为2` | 环入口为节点2 |
| `head = [1,2]`, 尾节点指向第1个节点 | `节点值为1` | 环入口为节点1 |
| `head = [1]`, 无环 | `null` | 单节点无环 |

### 思路

Floyd 判圈算法：快慢指针相遇后，将其中一个指针移回 head，然后两个指针同步每次走一步，再次相遇的位置就是环的起点。

数学证明：设 head 到环入口距离为 `a`，环入口到相遇点距离为 `b`，相遇点到环入口距离为 `c`。相遇时 slow 走了 `a + b`，fast 走了 `a + b + n*(b+c)`。由 `2*(a+b) = a+b + n*(b+c)` 得 `a = (n-1)*(b+c) + c`，即从 head 走 `a` 步和从相遇点走 `a` 步（绕若干圈）会在环入口相遇。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| Floyd 快慢指针 | 中 | O(n) 时间 O(1) 空间 | 首选 |
| 哈希表记录访问过节点 | 低 | O(n) 时间 O(n) 空间 | 简单但非最优 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def detect_cycle(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            # 无环
            return None

        # 有环，找入口
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow
```

> 这个技巧也用于 `寻找重复数`（Floyd 判圈在数组上的应用）。

---

## 相交链表

**LeetCode 160** | 难度：简单

### 题目描述

给你两个单链表的头节点 `headA` 和 `headB`，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null`。

### 示例

| 输入 | 输出 | 说明 |
|------|------|------|
| `listA = [4,1,8,4,5]`, `listB = [5,6,1,8,4,5]` | `节点值为8` | 在节点8相交 |
| `listA = [1,9,1,2,4]`, `listB = [3,2,4]` | `节点值为2` | 在节点2相交 |
| `listA = [2,6,4]`, `listB = [1,5]` | `null` | 不相交 |

### 思路

原代码用了集合做 O(n) 空间的记录。更优解法是用**双指针交替遍历**：指针 A 走完链表 A 后跳到链表 B 的头继续走，指针 B 同理。如果相交则必然在交点相遇（都走了 `len(A) + len(B) - 共同段` 步），如果不相交则同时为 None。

### 考试权衡

| 方案 | 实现难度 | 性能 | 推荐 |
|------|---------|------|------|
| 双指针交替遍历 | 低 | O(m+n) 时间 O(1) 空间 | 首选，技巧性强 |
| 哈希表 | 低 | O(m+n) 时间 O(n) 空间 | 简单可用 |

### Python 实现

```python
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        pa, pb = head_a, head_b

        while pa is not pb:
            pa = pa.next if pa else head_b
            pb = pb.next if pb else head_a

        return pa
```

> 核心思想：两指针走过的总路程相等。即使没有交点，最终也会同时为 None，循环退出。

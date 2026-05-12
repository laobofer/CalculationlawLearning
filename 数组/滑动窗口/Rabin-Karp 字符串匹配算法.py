# 是用来做字符串匹配的
# 思想上是自己实现一个 hash 算法, 使得不需要每一步都把 L 长度的子串显式提取出来
# 为了避免基数(256: ascii 码)过大导致的溢出, 这里使用了余数


def rabinKarp(txt: str, pat: str) -> int:
    # 位数
    L = len(pat)
    
    # 进制（只考虑 ASCII 编码）
    R = 256
    
    # 取一个比较大的素数作为求模的除数
    Q = 1658598167
    
    # R^(L - 1) 的结果
    RL = 1
    for i in range(1, L):
        # 计算过程中不断求模，避免溢出
        RL = (RL * R) % Q
    
    # 计算模式串的哈希值
    patHash = 0
    for i in range(len(pat)):
        patHash = (R * patHash + ord(pat[i])) % Q

    # 滑动窗口中子字符串的哈希值
    windowHash = 0

    # 滑动窗口代码框架
    left, right = 0, 0
    while right < len(txt):
        # 扩大窗口，移入字符
        windowHash = ((R * windowHash) % Q + ord(txt[right])) % Q
        right += 1

        # 当子串的长度达到要求
        if right - left == L:
            # 根据哈希值判断是否匹配模式串
            if windowHash == patHash:
                # 当前窗口中的子串哈希值等于模式串的哈希值
                # 还需进一步确认窗口子串是否真的和模式串相同，避免哈希冲突
                if pat == txt[left:right]:
                    return left
            
            # 缩小窗口，移出字符
            windowHash = (windowHash - (ord(txt[left]) * RL) % Q + Q) % Q
            # X % Q == (X + Q) % Q 是一个模运算法则
            # 因为 windowHash - (txt[left] * RL) % Q 可能是负数
            # 所以额外再加一个 Q，保证 windowHash 不会是负数
            left += 1
    
    # 没有找到模式串
    return -1
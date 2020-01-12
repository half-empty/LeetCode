"""
给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

 

示例 1：



输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
示例 2：

输入：a = 4, b = 2, c = 7
输出：1
示例 3：

输入：a = 1, b = 2, c = 3
输出：0
 

提示：

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        la, lb, lc = len(a), len(b), len(c)
        n = max(la, lb, lc)
        a = (n - la) * '0' + a
        b = (n - lb) * '0' + b
        c = (n - lc) * '0' + c
        ans = 0
        for i in range(n):
            if c[i] == '0':
                if a[i] == '1':
                    ans += 1
                if b[i] == '1':
                    ans += 1
            else:
                if a[i] == '0' and b[i] == '0':
                    ans += 1
        return ans

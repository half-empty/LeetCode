"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

官方题解：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode/
Manacher算法：https://segmentfault.com/a/1190000008484167?utm_source=tag-newest
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 中心扩展算法
        # def judge(a, b):
        #     while (a >= 0) and (b < length) and s[a] == s[b]:
        #         a -= 1
        #         b += 1
        #     return a + 1, b - 1
        # length = len(s)
        # max_s = ""
        # for i in range(length):
        #     a, b = judge(i, i)
        #     if b - a + 1 > len(max_s):
        #         max_s = s[a : b + 1]
        # for i in range(length - 1):
        #     a, b = judge(i, i + 1)
        #     if b - a + 1 > len(max_s):
        #         max_s = s[a : b + 1]
        # return max_s

        # Manacher算法
        s = '#'.join('$' + s + '\0')
        length = len(s)
        p = [1] * length
        max_s = ""
        mx = 0
        id = 0
        for i in range(1, length - 1):
            if i < mx:
                p[i] = min(p[2 * id - i], mx - i)
            while s[i - p[i]] == s[i + p[i]]:
                p[i] += 1
            if mx < i + p[i]:
                id = i
                mx = i + p[i]
            if p[i] * 2 - 1 > len(max_s):
                max_s = s[i - p[i] + 1 : i + p[i]]
        return max_s.replace('#', '')

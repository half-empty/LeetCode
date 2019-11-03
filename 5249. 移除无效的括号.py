"""
给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
 

示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
示例 2：

输入：s = "a)b(c)d"
输出："ab(c)d"
示例 3：

输入：s = "))(("
输出：""
解释：空字符串也是有效的
示例 4：

输入：s = "(a(b(c)d)"
输出："a(b(c)d)"
 

提示：

1 <= s.length <= 10^5
s[i] 可能是 '('、')' 或英文小写字母
"""

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        cnt = 0
        left_list = list()
        length = 0
        for c in s:
            if c == '(':
                cnt += 1
                res += c
                left_list.append(length)
                length += 1
            elif c == ')':
                if cnt > 0:
                    cnt -= 1
                    res += c
                    length += 1
            else:
                res += c
                length += 1
        while cnt > 0:
            tmp = left_list[-1]
            res = res[:tmp] + res[tmp + 1:]
            cnt -= 1
            del left_list[-1]
        return res

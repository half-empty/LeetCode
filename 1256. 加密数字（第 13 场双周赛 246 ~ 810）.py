"""
题目已被锁
"""

class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        m, n, s = 1, 0, 0
        if num == 0:
            return ""
        while s < num:
            m *= 2
            s += m
            n += 1
        return bin(num - s + m - 1)[2:].zfill(n)

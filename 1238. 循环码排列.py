"""
给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足：

p[0] = start
p[i] 和 p[i+1] 的二进制表示形式只有一位不同
p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同
 

示例 1：

输入：n = 2, start = 3
输出：[3,2,0,1]
解释：这个排列的二进制表示是 (11,10,00,01)
     所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
示例 2：

输出：n = 3, start = 2
输出：[2,6,7,5,4,0,1,3]
解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
 

提示：

1 <= n <= 16
0 <= start < 2^n
"""

class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        # res = list(range(2 ** n))
        # for i in range(len(res)):
        #     old = bin(res[i])
        #     new = list(old[2])
        #     for j in range(3, len(old)):
        #         new.append(str(int(old[j - 1]) ^ int(old[j])))
        #     res[i] = int(''.join(new), base=2)
        # tmp = res.index(start)
        # return res[tmp:] + res[:tmp]
        res = list()
        flag = 0
        for i in range(2 ** n):
            res.append(i ^ (i >> 1))
            if res[-1] == start:
                flag = len(res) - 1
        return res[flag:] + res[:flag]

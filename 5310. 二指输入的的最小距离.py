"""
二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。

给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的距离是 |x1 - x2| + |y1 - y2|。 

注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。

 

示例 1：

输入：word = "CAKE"
输出：3
解释： 
使用两根手指输入 "CAKE" 的最佳方案之一是： 
手指 1 在字母 'C' 上 -> 移动距离 = 0 
手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 
手指 2 在字母 'K' 上 -> 移动距离 = 0 
手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1 
总距离 = 3
示例 2：

输入：word = "HAPPY"
输出：6
解释： 
使用两根手指输入 "HAPPY" 的最佳方案之一是：
手指 1 在字母 'H' 上 -> 移动距离 = 0
手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
手指 2 在字母 'P' 上 -> 移动距离 = 0
手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
总距离 = 6
示例 3：

输入：word = "NEW"
输出：3
示例 4：

输入：word = "YEAR"
输出：7
 

提示：

2 <= word.length <= 300
每个 word[i] 都是一个大写英文字母。
"""

from typing import List


# 做出来的时候结束5分钟了，想的太久了，其实就是滚动求解，记录每一层可达状态
class Solution:
    def minimumDistance(self, word: str) -> int:
        import math
        keyboard = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZ']
        c2i = {chr(i + ord('A')):i + 1 for i in range(26)}
        move = dict()
        move[0] = dict()
        for i in range(1, 27):
            move[0][i] = 0
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                move[c2i[keyboard[i][j]]] = dict()
                for ii in range(len(keyboard)):
                    for jj in range(len(keyboard[ii])):
                        move[c2i[keyboard[i][j]]][c2i[keyboard[ii][jj]]] = abs(i - ii) + abs(j - jj)
        old = [[math.inf] * 27 for _ in range(27)]  # 手指当前位置
        old[0][0] = 0
        for c in word:
            new = [[math.inf] * 27 for _ in range(27)]
            cur = c2i[c]
            for i in range(27):
                for j in range(27):
                    if old[i][j] != math.inf:
                        new[cur][j] = min(new[cur][j], old[i][j] + move[i][cur])
                        new[i][cur] = min(new[i][cur], old[i][j] + move[j][cur])
            old = new
        ans = math.inf
        for i in range(27):
            for j in range(27):
                ans = min(ans, old[i][j])
        return ans


s = Solution()
print(eval(f"s.{dir(s)[-1]}")(
    word = "CAKE"
))
print(eval(f"s.{dir(s)[-1]}")(
    word = "HAPPY"
))
print(eval(f"s.{dir(s)[-1]}")(
    word = "NEW"
))
print(eval(f"s.{dir(s)[-1]}")(
    word = "YEAR"
))

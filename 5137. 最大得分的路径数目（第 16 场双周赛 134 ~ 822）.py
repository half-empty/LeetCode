"""
给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。

你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。

一条路径的 「得分」 定义为：路径上所有数字的和。

请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。

如果没有任何路径可以到达终点，请返回 [0, 0] 。

 

示例 1：

输入：board = ["E23","2X2","12S"]
输出：[7,1]
示例 2：

输入：board = ["E12","1X1","21S"]
输出：[4,2]
示例 3：

输入：board = ["E11","XXX","11S"]
输出：[0,0]
 

提示：

2 <= board.length == board[i].length <= 100
"""

from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # 需要反省一下，每次这种题目都喜欢用搜索来做，而不是先考虑dp，另外1000000007条件经常漏
        length = len(board)
        new_board = list()
        for row in board:
            tmp = list()
            for i in row:
                if i == 'S' or i == 'E':
                    tmp.append(0)
                elif i == 'X':
                    tmp.append(-1)
                else:
                    tmp.append(int(i))
            new_board.append(tmp)
        score_map = [[-1] * length for _ in range(length)]
        score_map[0][0] = 0
        score_map[-1][-1] = 0
        cnt_map = [[0] * length for _ in range(length)]
        cnt_map[-1][-1] = 1
        for i in range(length)[::-1]:
            for j in range(length)[::-1]:
                if new_board[i][j] == -1:
                    continue
                a1, a2, a3 = -1, -1, -1
                if i + 1 < length:
                    a1 = score_map[i + 1][j]
                if j + 1 < length:
                    a2 = score_map[i][j + 1]
                if i + 1 < length and j + 1 < length:
                    a3 = score_map[i + 1][j + 1]
                score = max(a1, a2, a3)
                if score == -1:
                    continue
                if a1 == score:
                    cnt_map[i][j] += cnt_map[i + 1][j]
                if a2 == score:
                    cnt_map[i][j] += cnt_map[i][j + 1]
                if a3 == score:
                    cnt_map[i][j] += cnt_map[i + 1][j + 1]
                score_map[i][j] = score + new_board[i][j]
        return [score_map[0][0], cnt_map[0][0] % 1000000007]

        # # 搜索超时，可能要优化score=的情况
        # length = len(board)
        # score_map = [[-1] * length for _ in range(length)]
        # new_board = list()
        # for row in board:
        #     tmp = list()
        #     for i in row:
        #         if i == 'S' or i == 'E':
        #             tmp.append(0)
        #         elif i == 'X':
        #             tmp.append(-1)
        #         else:
        #             tmp.append(int(i))
        #     new_board.append(tmp)
        # # max_score, cnt
        # res = [0, 0]
        # def dfs(x, y, score):
        #     if x < 0 or y < 0:
        #         return
        #     if x == 0 and y == 0:
        #         if score > res[0]:
        #             res[0] = score
        #             res[1] = 1
        #         elif score == res[0]:
        #             res[1] += 1
        #             res[1] %= 1000000007
        #         return
        #     if new_board[x][y] == -1:
        #         return
        #     score += int(new_board[x][y])
        #     if score <= score_map[x][y]:
        #         return
        #     score_map[x][y] = score
        #     dfs(x-1, y, score)
        #     dfs(x, y-1, score)
        #     dfs(x-1, y-1, score)
        #
        # dfs(length - 1, length - 1, 0)
        # return

s = Solution()
print(s.pathsWithMaxScore(board = ["E23","2X2","12S"]))
print(s.pathsWithMaxScore(board = ["E12","1X1","21S"]))
print(s.pathsWithMaxScore(board = ["E11","XXX","11S"]))
print(s.pathsWithMaxScore(["E11345","X452XX","3X43X4","422812","284522","13422S"]))

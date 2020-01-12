"""
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0] * n for _ in range(m)]
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            sum_line = 0
            for j in range(1, n + 1):
                sum_line += mat[i - 1][j - 1]
                if i == 0:
                    pre[i][j] = sum_line
                else:
                    pre[i][j] = pre[i - 1][j] + sum_line
        for i in range(m):
            for j in range(n):
                ia, ib = max(0, i - K), min(m, i + 1 + K)
                ja, jb = max(0, j - K), min(n, j + 1 + K)
                ans[i][j] = pre[ib][jb] + pre[ia][ja] - pre[ia][jb] - pre[ib][ja]
        return ans

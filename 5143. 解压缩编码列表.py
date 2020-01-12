"""
给你一个以行程长度编码压缩的整数列表 nums 。

考虑每相邻两个元素 [a, b] = [nums[2*i], nums[2*i+1]] （其中 i >= 0 ），每一对都表示解压后有 a 个值为 b 的元素。

请你返回解压后的列表。
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = list()
        for i in range(0, len(nums), 2):
            ans += [nums[i + 1]] * nums[i]
        return ans

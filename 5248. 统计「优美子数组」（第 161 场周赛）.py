"""
给你一个整数数组 nums 和一个整数 k。

如果某个子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        array = list()
        length = len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                array.append(i)
        cnt = len(array)
        if k > cnt:
            return 0
        res = 0
        for i in range(cnt):
            j = i + k - 1
            if j >= cnt:
                break
            a = array[i] + 1 if i == 0 else array[i] - array[i - 1]
            b = length - array[j] if j == cnt - 1 else array[j + 1] - array[j]
            res += a * b
        return res

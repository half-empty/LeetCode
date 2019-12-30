"""
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。

 

示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。
示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
 

提示：

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = [0] * 3  # 余012
        for num in nums:
            idx = num % 3  # 0~0,1~2,2~1
            new_flag = [flag[0], flag[1], flag[2]]
            if idx == 0:
                new_flag[0] = flag[0] + num
                if flag[1]:
                    new_flag[1] = flag[1] + num
                if flag[2]:
                    new_flag[2] = flag[2] + num
            elif idx == 1:
                if flag[2]:
                    new_flag[0] = max(flag[0], flag[2] + num)
                new_flag[1] = max(flag[1], flag[0] + num)
                if flag[1]:
                    new_flag[2] = max(flag[2], flag[1] + num)
            else:
                if flag[1]:
                    new_flag[0] = max(flag[0], flag[1] + num)
                if flag[2]:
                    new_flag[1] = max(flag[1], flag[2] + num)
                new_flag[2] = max(flag[2], flag[0] + num)
            flag = new_flag
        return flag[0]
    

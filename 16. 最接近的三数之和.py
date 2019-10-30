"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        result = sum(nums[:3])
        pre = None
        for i in range(length - 2):
            if nums[i] == pre:
                continue
            pre = nums[i]
            left, right = i + 1, length - 1
            while left != right:
                # min
                min_cnt = nums[i] + nums[left] + nums[left + 1]
                if min_cnt >= target:
                    if abs(min_cnt - target) < abs(result - target):
                        result = min_cnt
                    break
                # max
                max_cnt = nums[i] + nums[right] + nums[right - 1]
                if max_cnt <= target:
                    if abs(max_cnt - target) < abs(result - target):
                        result = max_cnt
                    break
                cnt = nums[i] + nums[left] + nums[right]
                if cnt == target:
                    return target
                elif cnt < target:
                    left += 1
                    while left != right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left != right and nums[right] == nums[right + 1]:
                        right -= 1
                if abs(cnt - target) < abs(result - target):
                    result = cnt
        return result

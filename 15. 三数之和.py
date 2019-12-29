"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # out of time
        # length = len(nums)
        # nums_dict = dict()
        # res = set()
        # for i in range(length):
        #     if nums[i] in nums_dict:
        #         for pair in nums_dict[nums[i]]:
        #             if i != pair[0] and i != pair[1]:
        #                 res.add(tuple(sorted((nums[i], nums[pair[0]], nums[pair[1]]))))
        #     for j in range(i + 1, length):
        #         tmp = 0 - nums[i] - nums[j]
        #         if tmp in nums_dict:
        #             nums_dict[tmp].append((i, j))
        #         else:
        #             nums_dict[tmp] = [(i, j)]
        # return list(res)

        def get_two_sum(nums, target):
            nums_set = set()
            res = set()
            for i in nums:
                if target - i in nums_set:
                    res.add((i, target - i))
                else:
                    nums_set.add(i)
            return res
        nums.sort()
        if len(nums) == 0 or nums[-1] < 0:
            return list()
        res = list()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for pair in get_two_sum(nums[i + 1:], -nums[i]):
                res.append((nums[i], ) + pair)
        return res
      

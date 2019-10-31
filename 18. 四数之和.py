"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 2sum -> 3sum -> 4sum
        nums.sort()
        length = len(nums)
        res = set()
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # min
                s = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if s == target:
                    res.add((nums[i], nums[j], nums[j + 1], nums[j + 2]))
                    break
                elif s > target:
                    continue
                # max
                s = nums[i] + nums[j] + nums[length - 2] + nums[length - 1]
                if s == target:
                    res.add((nums[i], nums[j], nums[length - 2], nums[length - 1]))
                    continue
                elif s < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return list(res)

        # # 暴力搜索+hashmap：O(N^2)速度反而比上面的O(N^3)慢，可能是因为数据不够多，也可能是因为上面的优化导致其实已经不是O(N^3)了
        # nums.sort()
        # length = len(nums)
        # hashmap = dict()
        # res = set()
        # for i in range(length - 3):
        #     for j in range(i + 1, length - 2):
        #         s = target - nums[i] - nums[j]
        #         if s not in hashmap:
        #             hashmap[s] = dict()
        #         if (nums[i], nums[j]) not in hashmap[s]:
        #             hashmap[s][nums[i], nums[j]] = i, j
        # for i in range(2, length - 1):
        #     for j in range(i + 1, length):
        #         s = nums[i] + nums[j]
        #         if s in hashmap:
        #             for k, v in hashmap[s].items():
        #                 if v[0] < v[1] < i < j:
        #                     res.add((nums[i], nums[j], nums[v[0]], nums[v[1]]))
        # return res

"""
给你一个方程，左边用 words 表示，右边用 result 表示。

你需要根据以下规则检查方程是否可解：

每个字符都会被解码成一位数字（0 - 9）。
每对不同的字符必须映射到不同的数字。
每个 words[i] 和 result 都会被解码成一个没有前导零的数字。
左侧数字之和（words）等于右侧数字（result）。 
如果方程可解，返回 True，否则返回 False。

 

示例 1：

输入：words = ["SEND","MORE"], result = "MONEY"
输出：true
解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
示例 2：

输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
输出：true
解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
示例 3：

输入：words = ["THIS","IS","TOO"], result = "FUNNY"
输出：true
示例 4：

输入：words = ["LEET","CODE"], result = "POINT"
输出：false
 

提示：

2 <= words.length <= 5
1 <= words[i].length, results.length <= 7
words[i], result 只含有大写英文字母
表达式中使用的不同字符数最大为 10
"""

# 执行用时 :80 ms, 在所有 python3 提交中击败了100.00%的用户
# 内存消耗 :12.7 MB, 在所有 python3 提交中击败了100.00%的用户
# 比赛时没考虑前导为0的情况，但通过了，不清楚是因为数据漏洞还是什么原因。
# 然后为了性能，通常会使用临时变量，也不会用defaultdict，写起来会更麻烦，但刷题场景下没必要注意这么多，影响不大。
# 除此以外，调整了下代码，主要是dfs的返回技巧，没必要用闭包，以及剪枝的优化，比不剪枝快百倍吧。
# 看了下其他人的代码，C++和Java直接不剪枝就可以过了，然而Python试了下就直接超时了。

"""
解题思路
1. 对words和result的单词进行按位统计，得到左右式的字母计算公式，目标为两式相减为0
2. 从大系数的字母开始，通过DFS进行搜索
3. 在搜索时进行剪枝，判断当前状态是否有可能形成可行解，如果不可能，则不再往下搜索。判断方式为：目前可用的最大数字(0-9)乘以还没确定数字的所有字母的正系数和，加上当前目标值不能小于0；目前可用的最大数字(0-9)乘以还没确定数字的所有字母的负系数和，加上当前目标值不能大于0
4. 额外：记录了下开头的字母，使其不能为0

作者：yi-lou-ting-feng-2
链接：https://leetcode-cn.com/problems/verbal-arithmetic-puzzle/solution/dfsjian-zhi-python-80ms-by-yi-lou-ting-feng-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        from collections import defaultdict
        letter_dict = defaultdict(int)
        not_zero_letter_set = set()
        for word in words:
            not_zero_letter_set.add(word[0])
            for i, letter in enumerate(word[::-1]):
                letter_dict[letter] += 10 ** i
        not_zero_letter_set.add(result[0])
        for i, letter in enumerate(result[::-1]):
            letter_dict[letter] -= 10 ** i
        arr = sorted(letter_dict.values(), key=lambda x: abs(x), reverse=True)
        not_zero_idx_set = {arr.index(letter_dict[letter]) for letter in not_zero_letter_set}
        length = len(arr)
        flag_num = [True] * 10
        def dfs(i, s):
            if i == length:
                if s == 0:
                    return True
                return False
            # 剪枝
            for num in range(10)[::-1]:
                if flag_num[num]:
                    if num * sum([arr[j] for j in range(i, length) if arr[j] > 0]) + s < 0 or \
                        num * sum([arr[j] for j in range(i, length) if arr[j] < 0]) + s > 0:
                        return False
                    break
            for num in range(10)[::-1]:
                if not flag_num[num] or (i in not_zero_idx_set and num == 0):
                    continue
                flag_num[num] = False
                if dfs(i + 1, s + arr[i] * num):
                    return True
                flag_num[num] = True
            return False
        return dfs(0, 0)


s = Solution()
print(s.isSolvable(words = ["SEND","MORE"], result = "MONEY"))
print(s.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
print(s.isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY"))
print(s.isSolvable(words = ["LEET","CODE"], result = "POINT"))


# class Solution:
#     def isSolvable(self, words: List[str], result: str) -> bool:
#         letter_dict = dict()
#         for word in words:
#             cnt = 1
#             for letter in word[::-1]:
#                 if letter not in letter_dict:
#                     letter_dict[letter] = 0
#                 letter_dict[letter] += cnt
#                 cnt *= 10
#         cnt = 1
#         for letter in result[::-1]:
#             if letter not in letter_dict:
#                 letter_dict[letter] = 0
#             letter_dict[letter] -= cnt
#             cnt *= 10
#         arr = sorted(letter_dict.values(), key=lambda x: abs(x), reverse=True)
#         length = len(arr)
#         flag_num = [True] * 10
#         flag_res = [False]
#         def dfs(i, s):
#             if flag_res[0]:
#                 return
#             if i == length:
#                 if s == 0:
#                     flag_res[0] = True
#                 return
#             # 剪枝
#             num = 10
#             for num in range(10)[::-1]:
#                 if flag_num[num]:
#                     break
#             if num * sum([abs(arr[j]) for j in range(i, length)]) < abs(s):
#                 return
#
#             for num in range(10)[::-1]:
#                 if not flag_num[num]:
#                     continue
#                 flag_num[num] = False
#                 dfs(i + 1, s + arr[i] * num)
#                 flag_num[num] = True
#         dfs(0, 0)
#         return flag_res[0]

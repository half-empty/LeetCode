"""
请你设计一个迭代器类，包括以下内容：

一个构造函数，输入参数包括：一个 有序且字符唯一 的字符串 characters（该字符串只包含小写英文字母）和一个数字 combinationLength 。
函数 next() ，按 字典序 返回长度为 combinationLength 的下一个字母组合。
函数 hasNext() ，只有存在长度为 combinationLength 的下一个字母组合时，才返回 True；否则，返回 False。
 

示例：

CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator

iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false
 

提示：

1 <= combinationLength <= characters.length <= 15
每组测试数据最多包含 10^4 次函数调用。
题目保证每次调用函数 next 时都存在下一个字母组合。
"""

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters = characters
        self.combinationLength = combinationLength
        self.length = len(self.characters)
        self.cur = [1] * self.combinationLength + [0] * (self.length - self.combinationLength)
        self.start = True


    def next(self):
        """
        :rtype: str
        """
        if self.start:
            self.start = False
        else:
            zero_idx = 0
            for i in range(self.length)[::-1]:
                if self.cur[i] == 0 and self.cur[i - 1] == 1:
                    zero_idx = i
                    break
            one_cnt = 0
            for i in range(zero_idx - 1, self.length):
                if self.cur[i] == 1:
                    one_cnt += 1
                    self.cur[i] = 0
            for i in range(zero_idx, zero_idx + one_cnt):
                self.cur[i] = 1
        return ''.join([self.characters[i] for i in range(self.length) if self.cur[i] == 1])


    def hasNext(self):
        """
        :rtype: bool
        """
        for i in self.cur[self.length - self.combinationLength:]:
            if i != 1:
                return True
        return False

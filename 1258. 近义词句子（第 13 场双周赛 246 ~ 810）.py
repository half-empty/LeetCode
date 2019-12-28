"""
题目已被锁
"""

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        def dfs(n):
            if n == length:
                result.add(" ".join(word_list))
                return
            dfs(n + 1)
            if word_list[n] in synonym_dict:
                tmp = word_list[n]
                for word in synonym_dict[tmp]:
                    word_list[n] = word
                    dfs(n + 1)
                word_list[n] = tmp
        result = set()
        synonym_dict = dict()
        for synonym in synonyms:
            if synonym[0] not in synonym_dict and synonym[1] not in synonym_dict:
                synonym_dict[synonym[0]] = synonym_dict[synonym[1]] = set()
            elif synonym[0] not in synonym_dict:
                synonym_dict[synonym[0]] = synonym_dict[synonym[1]]
            elif synonym[1] not in synonym_dict:
                synonym_dict[synonym[1]] = synonym_dict[synonym[0]]
            synonym_dict[synonym[0]].add(synonym[0])
            synonym_dict[synonym[0]].add(synonym[1])
        word_list = text.split(" ")
        length = len(word_list)
        dfs(0)
        return sorted(result)

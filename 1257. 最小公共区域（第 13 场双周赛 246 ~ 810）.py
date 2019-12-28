"""
题目已被锁
"""

class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        region_dict = dict()
        for region in regions:
            for i in region[1:]:
                region_dict[i] = region[0]
        s1 = set()
        s1.add(region1)
        while region1 in region_dict:
            region1 = region_dict[region1]
            s1.add(region1)
        if region2 in s1:
            return region2
        while region2 in region_dict:
            region2 = region_dict[region2]
            if region2 in s1:
                return region2

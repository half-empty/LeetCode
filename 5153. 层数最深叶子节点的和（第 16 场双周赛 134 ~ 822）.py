"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。

 

示例：



输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
 

提示：

树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。
"""

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # max_deep, sum_val
        v = [-1, 0]
        def dfs(r, deep):
            if deep > v[0]:
                v[0] = deep
                v[1] = r.val 
            elif deep == v[0]:
                v[1] += r.val
            if r.left:
                dfs(r.left, deep + 1)
            if r.right:
                dfs(r.right, deep + 1)
        dfs(root, 0)
        return v[1]

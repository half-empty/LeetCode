"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# # 递归实现简洁优美，具体参考https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/kge-yi-zu-fan-zhuan-lian-biao-by-powcai/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        cnt = 0
        while cur and cnt < k:
            cnt += 1
            cur = cur.next
        if cnt == k:
            cur = self.reverseKGroup(cur, k)
            while cnt > 0:
                cnt -= 1
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
            head = cur
        return head

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# def print_listnode(node):
#     while node:
#         print("{}->".format(node.val), end='')
#         node = node.next
#     print("end")
#
#
# def make_listnode():
#     head = res = ListNode(0)
#     for i in range(10):
#         res.next = ListNode(i)
#         res = res.next
#     return head
#
#
# def reverseKGroup(head, k):
#     cur = head
#     cnt = 0
#     while cur and cnt < k:
#         cnt += 1
#         cur = cur.next
#     if cnt == k:
#         cur = reverseKGroup(cur, k)
#         while cnt > 0:
#             cnt -= 1
#             tmp = head.next
#             head.next = cur
#             cur = head
#             head = tmp
#         head = cur
#     return head
#
#
# if __name__ == '__main__':
#     t = make_listnode()
#     print_listnode(t)
#     print_listnode(reverseKGroup(t, 3))

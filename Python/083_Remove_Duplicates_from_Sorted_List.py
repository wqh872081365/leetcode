"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node:
            while node.next:
                while node.val == node.next.val:
                    if node.next.next:
                        node.next = node.next.next
                    else:
                        node.next = None
                        break
                if node.next:
                    node = node.next
                else:
                    break
        return head
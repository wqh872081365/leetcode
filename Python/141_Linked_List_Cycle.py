"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        low = head
        fast = head
        while low and fast:
            if fast.next:
                if low is fast.next:
                    return True
                else:
                    low = low.next
                    fast = fast.next.next
            else:
                return False
        return False
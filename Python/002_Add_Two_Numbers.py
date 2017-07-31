"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []
        while 1:
            l1_list.append(l1.val)
            l1 = l1.next
            if not l1:
                break
        while 1:
            l2_list.append(l2.val)
            l2 = l2.next
            if not l2:
                break

        l1 = l1_list
        l2 = l2_list
        l1_len = len(l1)
        l2_len = len(l2)
        result = []
        index = 0
        for i in range(max(l1_len, l2_len) + 1):
            if (i < min(l1_len, l2_len)):
                result.append((l1[i] + l2[i] + index) % 10)
                index = (l1[i] + l2[i] + index) / 10
            elif (i < max(l1_len, l2_len)):
                if (l1_len > l2_len):
                    result.append((l1[i] + index) % 10)
                    index = (l1[i] + index) / 10
                else:
                    result.append((l2[i] + index) % 10)
                    index = (l2[i] + index) / 10
            else:
                if (index == 0):
                    break
                else:
                    result.append(index)
        return result
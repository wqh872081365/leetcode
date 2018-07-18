"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # cur_node_val = None
        # val_index_list = []
        # for index, list_node in enumerate(lists):
        #     if cur_node_val is not None:
        #         if list_node is not None:
        #             if list_node.val < cur_node_val:
        #                 cur_node_val = list_node.val
        #                 val_index_list = [index]
        #             elif list_node.val == cur_node_val:
        #                 val_index_list.append(index)
        #     else:
        #         if list_node is not None:
        #             cur_node_val = list_node.val
        #             val_index_list = [index]
        # if cur_node_val is not None:
        #     val_count = 0
        #     for index in val_index_list[::-1]:
        #         list_node = lists[index]
        #         while list_node and list_node.val == cur_node_val:
        #             list_node = list_node.next
        #             val_count += 1
        #         if list_node:
        #             lists[index] = list_node
        #         else:
        #             lists.pop(index)
        #     result = ListNode(cur_node_val)
        #     result_next = result
        #
        #     for _index in range(val_count - 1):
        #         result_next.next = ListNode(cur_node_val)
        #         result_next = result_next.next
        #
        #     while cur_node_val is not None:
        #         new_val = None
        #         val_index_list = []
        #         for index, list_node in enumerate(lists):
        #             if new_val is not None:
        #                 if list_node is not None:
        #                     if list_node.val < new_val:
        #                         new_val = list_node.val
        #                         val_index_list = [index]
        #                     elif list_node.val < new_val:
        #                         val_index_list.append(index)
        #             else:
        #                 if list_node is not None:
        #                     new_val = list_node.val
        #                     val_index_list = [index]
        #         cur_node_val = new_val
        #         if cur_node_val is not None:
        #             val_count = 0
        #             for index in val_index_list[::-1]:
        #                 list_node = lists[index]
        #                 while list_node and list_node.val == cur_node_val:
        #                     list_node = list_node.next
        #                     val_count += 1
        #                 if list_node:
        #                     lists[index] = list_node
        #                 else:
        #                     lists.pop(index)
        #             for _index in range(val_count):
        #                 result_next.next = ListNode(cur_node_val)
        #                 result_next = result_next.next
        #
        #     return result
        # else:
        #     return None

        new_lists = []
        for node in lists:
            while node:
                new_lists.append(node.val)
                node = node.next
        new_lists.sort()
        if new_lists:
            result = ListNode(new_lists[0])
            result_next = result
            for val in new_lists[1:]:
                result_next.next = ListNode(val)
                result_next = result_next.next
            return result
        else:
            return None

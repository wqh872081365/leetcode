"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            node_list = [root]
        else:
            node_list = []
        while node_list:
            node = node_list[-1]
            result.append(node.val)
            node_list_tem = []
            for node in node_list:
                if node.left:
                    node_list_tem.append(node.left)
                if node.right:
                    node_list_tem.append(node.right)
            node_list = node_list_tem
        return result

"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        node_dict = {}
        exist_dict = {}

        def get_path_str(node):
            if node.left:
                left = get_path_str(node.left)
            else:
                left = "^"
            if node.right:
                right = get_path_str(node.right)
            else:
                right = "$"
            tem = left + str(node.val) + right
            if tem in exist_dict:
                exist_dict[tem] += 1
            else:
                exist_dict[tem] = 1
                node_dict[tem] = node
            return tem

        if root:
            get_path_str(root)
        else:
            return []
        node_list = [k for k, v in exist_dict.items() if v > 1]
        return [node_dict[n] for n in node_list]

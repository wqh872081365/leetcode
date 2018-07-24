"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def get_inorder_list(node):
            if node.left:
                get_inorder_list(node.left)
            result.append(node.val)
            if node.right:
                get_inorder_list(node.right)

        if root:
            get_inorder_list(root)
        return result

        # result = []
        # if root:
        #     stack = [root]
        # else:
        #     stack = []
        # cur = root
        # while stack:
        #     while cur and cur.left:
        #         stack.append(cur.left)
        #         cur = cur.left
        #     node = stack.pop()
        #     result.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     cur = node.right
        # return result

"""
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def tree_print(node, h, index):
            if node.left:
                self.result[h][index - 2 ** (self.height - 1 - h)] = str(node.left.val)
                tree_print(node.left, h + 1, index - 2 ** (self.height - 1 - h))
            if node.right:
                self.result[h][index + 2 ** (self.height - 1 - h)] = str(node.right.val)
                tree_print(node.right, h + 1, index + 2 ** (self.height - 1 - h))

        self.height = 0
        node_list = [root]
        while node_list:
            self.height += 1
            node_list_new = []
            for node in node_list:
                if node.left:
                    node_list_new.append(node.left)
                    if node.right:
                        node_list_new.append(node.right)
                else:
                    if node.right:
                        node_list_new.append(node.right)
            node_list = node_list_new
        self.result = []
        for _ in range(self.height):
            self.result.append([""] * (2 ** self.height - 1))
        self.result[0][2 ** (self.height - 1) - 1] = str(root.val)
        tree_print(root, 1, (2 ** (self.height - 1) - 1))

        return self.result
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
def search(node):
    if (node == None):
        return
    a = copy.copy(node.left)
    node.left = copy.copy(node.right)
    node.right = copy.copy(a)
    search(node.left)
    search(node.right)
        
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        search(root)
        return root
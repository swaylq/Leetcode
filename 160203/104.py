# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def search(node):
    if node == None:
        return 0
        
    val = 0
    if node.left == None and node.right == None:
        val = 1
    else:
        leftVal = search(node.left) + 1
        rightVal = search(node.right) + 1
        val = rightVal if rightVal > leftVal else leftVal
    return val
                
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return search(root)
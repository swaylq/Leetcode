# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def search(p, q):
    if p == None and q == None:
        return True
    elif p == None or q == None:
        return False
    else:
        return p.val == q.val and search(p.left, q.left) and search(p.right, q.right)

class Solution(object):
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return search(p, q)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, node, number):
        if self.result: return
        if node == None: return
        if node.left == None and node.right == None and number + node.val == self.sum:
            self.result = True
            return
        self.search(node.left, number + node.val)
        self.search(node.right, number + node.val)
        
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        self.result = False
        self.search(root, 0)
        return self.result
        

def test():
    root = TreeNode(5)
    left = TreeNode(4)
    right = TreeNode(3)
    root.left = left
    root.right = right
    
    s = Solution()
    print s.hasPathSum(root, 9)
    
test()
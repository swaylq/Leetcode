class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def search(self, node, p, q):
        if self.done == True: return [False, False]
        if node == None: return [False, False]
        left = self.search(node.left, p, q)
        right = self.search(node.right, p, q)
        result = [left[i] or right[i] for i in range(0, 2)]
        if node.val == p.val: result[0] = True
        if node.val == q.val: result[1] = True
        if result == [True, True] and self.resultNode == None:
            self.done = True
            self.resultNode = node
        return result
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.done = False
        self.resultNode = None
        self.search(root, p, q)
        return self.resultNode.val
        
def test():
    roota = TreeNode(11)
    root = TreeNode(10)
    roota.left = root
    roota.right = None
    aLeft = TreeNode(5)
    bLeft = TreeNode(2)
    root.left = aLeft
    root.right = bLeft
    s = Solution()
    print s.lowestCommonAncestor(roota, aLeft, bLeft)
    
test()
    
        
        

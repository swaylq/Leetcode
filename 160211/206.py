class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swap(self, a, b):
        c = a
        a = b
        b = c
    def search(self, node):
        if node == None: return
        self.list.append(node.val)
        self.search(node.next)
    def fill(self, node, num):
        if node == None: return
        node.val = self.list[num]
        self.fill(node.next, num + 1)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.list = []
        self.search(head)
        print self.list
        for i in range(0, len(self.list) / 2):
            self.list[i], self.list[len(self.list) - i - 1] = self.list[len(self.list) - i - 1], self.list[i]
        self.fill(head, 0)
        return head
        

def test():
    nodeA = ListNode(1)
    nodeB = ListNode(2)
    nodeA.next = nodeB
    s = Solution()
    print s.reverseList(nodeA).val
    
test()

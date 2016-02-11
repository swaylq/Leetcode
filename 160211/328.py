# Definition for singly-linked list.
import copy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            currentNode = head.next
            oddNode = head
            firstEvenNode = head.next
            evenNode = head.next
            i = 2
            if currentNode:
                while not (currentNode.next == None):
                    i += 1
                    currentNode = currentNode.next
                    if i % 2 == 0:
                        evenNode.next = currentNode
                        evenNode = currentNode
                    else:
                        oddNode.next = currentNode
                        oddNode = currentNode
                oddNode.next = firstEvenNode
            if evenNode: evenNode.next = None
        return head
        
def test():
    nodeA = ListNode(1)
    nodeB = ListNode(2)
    nodeA.next = nodeB
    s = Solution()
    print s.oddEvenList(nodeA).val
    
test()
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastNode = None
        currentNode = head
        dict = {}
        while not (currentNode == None):
            if not dict.has_key(currentNode.val):
                dict[currentNode.val] = True
                if lastNode: lastNode.next = currentNode
                lastNode = currentNode
                currentNode = currentNode.next
            else:
                currentNode = currentNode.next
        if lastNode: lastNode.next = None
        return head

def test():
    a = ListNode(1)
    s = Solution()
    s.deleteDuplicates(a)

test()
    


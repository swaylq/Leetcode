# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        pointOne = l1
        pointTwo = l2
        if l1.val < l2.val:
            head = l1
            pointOne = l1.next
        else:
            head = l2
            pointTwo = l2.next
        
        current = head
        while pointOne != None or pointTwo != None:
            if pointTwo == None or (pointOne != None and pointOne.val < pointTwo.val):
                current.next = pointOne
                current = current.next
                pointOne = pointOne.next
            else:
                current.next = pointTwo
                current = current.next
                pointTwo = pointTwo.next
        return head
        
def display(node):
    x = node
    list = []
    while x != None:
        list.append(x.val)
        x = x.next
    print list

def test():
    s = Solution()
    l1 = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    l1.next = a
    a.next = b
    l2 = ListNode(4)
    c = ListNode(5)
    d = ListNode(6)
    l2.next = c
    c.next = d
    display(s.mergeTwoLists(l1, l2))
test()
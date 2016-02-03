# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def search(node):
    if node == None:
        return
    next = node.next
    if next != None:
        node.val = next.val
        if next.next == None:
            node.next = None
        else:
            search(next)
    

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        search(node)
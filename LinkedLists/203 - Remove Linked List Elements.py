# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        temp = start
        while temp != None:
            if temp.next != None and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        head = start.next
        return head



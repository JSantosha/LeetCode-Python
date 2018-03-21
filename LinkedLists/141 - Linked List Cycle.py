# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        temp2 = head
        if head == None:
            return False
        if head.next == None:
            return False
        while temp != None and temp2 != None and temp2.next != None:
            temp = temp.next
            temp2 = temp2.next.next
            if temp2 == temp:
                return True

        return False
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        temp = head
        first = None
        second = None
        result = head.next
        while temp != None and temp.next != None:
            first = temp
            second = temp.next
            if temp.next.next != None and temp.next.next.next != None:
                temp = temp.next.next
                print "hai"
            else:
                first.next = temp.next.next
                second.next = first
                break
            first.next = temp.next
            second.next = first

        return result
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head != None:
            node = None
            temp = head.next
            while temp != None:
                head.next = node
                node = head
                head = temp
                temp = temp.next

            head.next = node
            return head
        else:
            return head
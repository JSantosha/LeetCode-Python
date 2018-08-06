# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        if head == None:
            return head
        if temp.next == None:
            return temp
        if temp.next.next == None:
            return temp.next
        temp2 = head
        while True:
            if temp2.next == None:
                return temp
            if temp2.next.next == None:
                return temp.next
            temp = temp.next
            temp2 = temp2.next.next
            # Solution 2
#         length = 0
#         temp = head
#         while temp:
#             length += 1
#             temp = temp.next

#         mid = (int(length)/2)+1
#         temp = head
#         while mid>1:
#             temp = temp.next
#             mid -= 1

#         return temp



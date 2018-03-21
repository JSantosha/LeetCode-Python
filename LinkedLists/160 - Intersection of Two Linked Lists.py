# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp = headA
        temp2 = headB
        count1 = 0
        count2 = 0
        while temp != None:
            count1 += 1
            temp = temp.next
        while temp2 != None:
            count2 += 1
            temp2 = temp2.next

        d = abs(count1 - count2)

        temp = headA
        temp2 = headB
        if count1 > count2:
            while d != 0:
                temp = temp.next
                d -= 1
        elif count2 > count1:
            while d != 0:
                temp2 = temp2.next
                d -= 1
        while temp != None and temp2 != None:
            if temp.val == temp2.val:
                return temp
            temp = temp.next
            temp2 = temp2.next

        return None

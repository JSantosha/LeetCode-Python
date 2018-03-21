# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        less = ListNode(0)
        more = ListNode(0)

        startless = less
        startmore = more

        temp = head
        while temp != None:
            if temp.val < x:
                less.next = temp
                temp = temp.next
                less = less.next
                less.next = None
            elif temp.val >= x:
                more.next = temp
                temp = temp.next
                more = more.next
                more.next = None

        if startless.next == None and startmore.next == None:
            return None
        elif startless.next == None:
            return startmore.next
        elif startmore.next == None:
            return startless.next
        else:
            less.next = startmore.next
            return startless.next

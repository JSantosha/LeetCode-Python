# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or k == 0 or head.next == None:
            return head
        temp = head
        count = 0

        while temp != None:
            count += 1
            temp = temp.next
        if count < k:
            k = k % count
            if k == 0:
                return head
            count = count - k
        else:
            count = count - k

        if count == 0:
            return head
        temp = head
        print count
        while count - 1 > 0:
            temp = temp.next
            count -= 1
        second = temp.next
        temp.next = None
        temp = head

        temp2 = second
        while temp2.next != None:
            temp2 = temp2.next

        temp2.next = head
        head = second

        return head



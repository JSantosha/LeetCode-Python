# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        prev = head
        rem = head

        count = 1
        if head == None or (head.next == None and n == 1):
            return None

        while temp.next != None:
            if count >= n:
                rem = rem.next
                temp = temp.next
                if count >= n + 1:
                    prev = prev.next
                count += 1
            else:
                count += 1
                temp = temp.next

        if prev == rem and prev == head:
            head = head.next
        else:
            prev.next = rem.next

        return head
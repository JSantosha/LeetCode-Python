# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None or m == n:
            return head

        temp = head
        count = 0
        start = None
        prev = None
        end = None
        while temp != None:
            count += 1
            if count == m and temp == head:
                start = head
                prev = None
                temp = temp.next
            elif count == m and temp != head:
                start = temp
                temp = temp.next
                prev.next = None
            elif count == n:
                end = temp
                temp = temp.next
                end.next = None
                break
            elif count < m:
                prev = temp
                temp = temp.next
            elif count > m and count < n:
                temp = temp.next

        print start.val
        print end.val

        if start != None:
            node = None
            temp2 = start.next
            while temp2 != None:
                start.next = node
                node = start
                start = temp2
                temp2 = temp2.next

            start.next = node
        temp2 = start
        while temp2.next != None:
            temp2 = temp2.next

        temp2.next = temp
        if prev == None:
            head = start
        else:
            prev.next = start
        return head






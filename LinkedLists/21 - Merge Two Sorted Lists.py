# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 != None or l2 != None:
            if l2 == None and l1 != None:
                curr.next = ListNode(0)
                curr.next.val = l1.val
                l1 = l1.next
                curr.next.next = None
                curr = curr.next
            elif l1 == None and l2 != None:
                curr.next = ListNode(0)
                curr.next.val = l2.val
                l2 = l2.next
                curr.next.next = None
                curr = curr.next
            else:
                if l1.val >= l2.val:
                    temp = ListNode(0)
                    temp.val = l2.val
                    l2 = l2.next
                    temp.next = None
                    if curr == None:
                        head.val = temp.val
                        head.next = curr
                        curr = head
                    else:
                        curr.next = temp
                        curr = curr.next
                elif l2.val > l1.val:
                    temp = ListNode(0)
                    temp.val = l1.val
                    l1 = l1.next
                    temp.next = None
                    if curr == None:
                        head.val = temp.val
                        head.next = curr
                        curr = head
                    else:
                        curr.next = temp
                        curr = curr.next

        return head

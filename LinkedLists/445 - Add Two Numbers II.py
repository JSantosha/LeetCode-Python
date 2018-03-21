# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l1
        temp2 = l2
        sum1 = 0
        sum2 = 0
        while temp != None:
            sum1 = sum1 * 10 + temp.val
            temp = temp.next

        while temp2 != None:
            sum2 = sum2 * 10 + temp2.val
            temp2 = temp2.next

        result = sum1 + sum2
        curr = None
        if result == 0:
            return ListNode(0)

        while result != 0:
            temp = ListNode(result % 10)
            result = result / 10
            temp.next = curr
            curr = temp

        return curr




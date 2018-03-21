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

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        carry = 0
        result = ListNode(0)
        temp3 = result
        sum2 = 0
        while temp != None or temp2 != None or carry != 0:
            if temp != None and temp2 != None:
                sum2 = temp.val + temp2.val + carry
            elif temp == None and temp2 != None:
                sum2 = temp2.val + carry
            elif temp2 == None and temp != None:
                sum2 = temp.val + carry
            elif carry != 0 and temp == None and temp2 == None:
                sum2 = carry
            value = sum2 % 10
            sum2 = sum2 / 10
            carry = sum2 % 10
            sum1 = ListNode(value)
            temp3.next = sum1
            temp3 = temp3.next
            if temp != None:
                temp = temp.next
            if temp2 != None:
                temp2 = temp2.next

        if carry != 0:
            sum1 = ListNode(carry)
            temp3.next = sum1
            temp3 = temp3.next
        return result.next





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        temp2 = head
        if head == None:
            return None
        if head.next == None:
            return None

        flag = 0

        temp3 = None

        while temp != None and temp2 != None and temp2.next != None:
            temp = temp.next
            temp2 = temp2.next.next
            if temp2 == temp:
                flag = 1
                temp3 = temp
                break

        if flag == 0:
            return None
        temp = head
        while temp != None:
            if temp == temp3:
                return temp
            else:
                temp = temp.next
                temp3 = temp3.next






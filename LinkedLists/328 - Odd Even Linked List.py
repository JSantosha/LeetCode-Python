# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        startodd = head
        starteven = head.next

        temp = head.next.next
        startodd.next = None
        starteven.next = None
        tempodd = startodd
        tempeven = starteven
        flag = 1
        while temp != None:
            if flag == 1:
                tempodd.next = temp
                tempodd = tempodd.next

                flag = 0
            else:
                tempeven.next = temp
                tempeven = tempeven.next

                flag = 1
            temp = temp.next
            tempodd.next = None
            tempeven.next = None

        tempodd.next = starteven
        return startodd
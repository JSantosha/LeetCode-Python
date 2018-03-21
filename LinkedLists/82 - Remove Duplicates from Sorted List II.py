# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        temp = head
        while temp != None:
            if d.get(temp.val, 0) == 0:
                d[temp.val] = 1
            else:
                d[temp.val] += 1
            temp = temp.next

        result = ListNode(0)
        temp2 = result
        temp = head
        while temp != None:
            if d[temp.val] == 1:
                temp3 = ListNode(temp.val)
                temp2.next = temp3
                temp2 = temp3
            temp = temp.next

        return result.next

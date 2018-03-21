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
        if head == None:
            return head
        curr = None
        temp2 = head
        head2 = ListNode(0)
        while temp2 != None:
            temp = ListNode(0)
            temp.val =  temp2.val
            if curr == None:
                head2.val = temp.val
                head2.next = temp.next
                curr = head2
                print temp2.val
            else:
                if curr.val != temp.val:
                    print temp2.val
                    curr.next = temp
                    curr = curr.next
                else:
                    del temp
            temp2 = temp2.next
        return head2
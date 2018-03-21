# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        s = ""
        while temp != None:
            s = s + str(temp.val)
            temp = temp.next
        print s
        temp = head
        prev = None
        curr = head
        while temp != None:
            temp = temp.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev
        temp = head
        revs = ""
        while temp != None:
            revs = revs + str(temp.val)
            temp = temp.next

        print revs

        if revs == s:
            return True
        else:
            return False
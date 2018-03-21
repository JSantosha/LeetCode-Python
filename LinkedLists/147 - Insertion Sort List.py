# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        l = []
        if temp == None or temp.next == None:
            return temp
        while temp != None:
            l.append(temp.val)
            temp = temp.next
        key = 0
        for j in xrange(1, len(l)):
            key = l[j]
            i = j - 1
            while i >= 0 and l[i] > key:
                l[i + 1] = l[i]
                i -= 1

            l[i + 1] = key

        print l[0]
        result = ListNode(0)
        temp = result
        for i in range(len(l)):
            temp2 = ListNode(l[i])
            temp.next = temp2
            temp = temp.next
        # head = result.next
        return result.next

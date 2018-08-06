# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        result = []
        for i in xrange(len(lists)):
            temp = lists[i]
            while temp:
                result.append(temp.val)
                temp = temp.next

        result.sort()
        print result
        if len(result) == 0:
            return None
        head = ListNode(result[0])
        curr = head
        for i in xrange(1, len(result)):
            temp = ListNode(result[i])
            curr.next = temp
            curr = curr.next

        return head

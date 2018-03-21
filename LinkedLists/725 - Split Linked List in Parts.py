# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = [[] for i in xrange(k)]
        if k == 1:
            temp = root
            while temp != None:
                l[k - 1].append(temp.val)
                temp = temp.next
            return l

        count = 0

        temp = root
        while temp != None:
            count += 1
            temp = temp.next

        if k < count:

            num = count % k
            elements = count / k
            i = 0
            temp = root
            while k > 0 and temp != None:
                t = elements
                if num != 0:
                    while t + 1 > 0:
                        l[i].append(temp.val)
                        t -= 1
                        temp = temp.next
                    num -= 1
                else:
                    while t > 0:
                        l[i].append(temp.val)
                        t -= 1
                        temp = temp.next

                i += 1
                k -= 1

        else:
            i = 0
            temp = root
            while temp != None:
                l[i].append(temp.val)
                i += 1
                temp = temp.next

        return l





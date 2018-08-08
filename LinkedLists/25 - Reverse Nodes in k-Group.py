# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = head
        length = 0
        # Calculating the length of the linked list.
        while temp:
            length += 1
            temp = temp.next

        # if there is only one element in the list then return the list as it is.
        if head == None or head.next == None:
            return head;

        # if the value of k is more than the length of the list return the list itself
        if k > length or k == 1:
            return head

        # Calculating the elements  that need not be reversed in the list. The elements that were leftout after forming the groups.
        leftout = length % k

        t = k
        parthead = None
        parttail = None
        curr = head
        head1 = None
        prev = None
        temp = None
        # count = 0
        previter = None
        # itereate over the list and reverse the elements as k groups until the elements that wont form a group.
        while length > leftout:
            t = k
            parthead = curr
            head1 = parthead
            # count +=1
            while t > 0:
                # print head1.val
                # When the list is pointing to the start element of the group to be reversed. Then point the next of the start element to null. Else point the elements next to the previous element.
                if parthead == head1:
                    temp = parthead
                    curr = curr.next
                    temp.next = None
                    parthead = curr
                    prev = temp
                    parttail = temp
                    t -= 1
                    length -= 1
                else:
                    temp = parthead
                    curr = curr.next
                    temp.next = prev
                    prev = temp
                    parthead = curr
                    t -= 1
                    length -= 1
            # At the end of one group point, make sure the last element of the group in the previous iteration is pointing to the first element in the current evaluated group.
            if previter == None:
                previter = parttail
                head = temp
            else:
                previter.next = temp
                previter = parttail
            temp2 = temp
            # print count
            # while temp2:
            #     print str(temp2.val)+"->"
            #     temp2 = temp2.next
        parttail.next = curr
        return head

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # if head:
        #     head2=None
        #     curr2=head2
        #     curr=head
        #     dic=dict()
        #     while curr:
        #         if dic.get(curr):
        #             curr2=dic[curr]
        #         else:
        #             dic[curr]=RandomListNode(curr.label)
        #             curr2=dic[curr]
        #         if curr.next:
        #             if dic.get(curr.next):
        #                 curr2.next=dic[curr.next]
        #             else:
        #                 curr2.next=RandomListNode(curr.next.label)
        #                 dic[curr.next]=curr2.next
        #         if curr.random:
        #             if dic.get(curr.random):
        #                 curr2.random=dic[curr.random]
        #             else:
        #                 curr2.random=RandomListNode(curr.random.label)
        #                 dic[curr.random]=curr2.random
        #         print(curr2.label)
        #         curr2=curr2.next
        #         curr=curr.next
        #     return head2
        # return None
        if head == None:
            return head
        curr = head
        newlist = RandomListNode(0)
        head1 = newlist
        d = {}
        while curr != None:
            temp = RandomListNode(curr.label)
            newlist.next = temp
            newlist = newlist.next
            d[curr] = newlist
            curr = curr.next

        newlist = head1.next
        curr = head
        while curr:
            newlist.random = d.get(curr.random, None)
            newlist = newlist.next
            curr = curr.next

        return head1.next




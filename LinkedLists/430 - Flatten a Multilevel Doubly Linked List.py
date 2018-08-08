"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head

        if head.next == None and head.child == None:
            return head
        temp = head
        while temp:
            if temp.child != None:
                childlstend = self.getchildlist(temp.child)
                temp2 = temp.next
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None
                if temp2 != None:
                    temp2.prev = childlstend
                    childlstend.next = temp2
                else:
                    childlstend.next = None
            temp = temp.next

        return head

    def getchildlist(self, root):
        if root == None:
            return None
        else:
            temp = root
            while temp.next:
                temp = temp.next
            return temp


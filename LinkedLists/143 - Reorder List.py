# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head != None and head.next != None and head.next.next != None:

            temp = head
            count = 0

            while temp != None:
                temp = temp.next
                count += 1

            count = count / 2
            temp = head
            while count - 1 > 0:
                temp = temp.next
                count -= 1
            second = temp.next
            temp.next = None

            if second != None:
                node = None
                temp = second.next
                while temp != None:
                    second.next = node
                    node = second
                    second = temp
                    temp = temp.next

                second.next = node

            result = ListNode(0)
            temp = head
            flag = 0
            temp3 = result
            while temp != None or second != None:
                if flag == 0:
                    if temp != None:
                        temp4 = temp
                        temp = temp.next
                        temp4.next = None
                        temp3.next = temp4
                        temp3 = temp3.next
                        flag = 1
                    else:
                        flag = 1
                elif flag == 1:
                    if second != None:
                        temp4 = second
                        second = second.next
                        temp4.next = None
                        temp3.next = temp4
                        temp3 = temp3.next
                        flag = 0
                    else:
                        flag = 0

            head = result.next



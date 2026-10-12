# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head

        op = dummy
        temp = head

        while temp is not None:
            if temp.val == val:
                op.next = temp.next
            else:
                op = temp

            temp = temp.next

        return dummy.next
        
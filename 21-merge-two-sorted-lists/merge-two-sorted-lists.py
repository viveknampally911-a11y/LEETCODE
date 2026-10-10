# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return
        temp1=list1
        temp2=list2
        op=ListNode()
        temp=op
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next

        if list1 is not None:
            temp.next=list1
        else:
            temp.next=list2
        return op.next

            
        
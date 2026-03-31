# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t,p = head,None

        while t:
            temp = t.next
            t.next = p
            p = t
            t = temp
        return p
        

        
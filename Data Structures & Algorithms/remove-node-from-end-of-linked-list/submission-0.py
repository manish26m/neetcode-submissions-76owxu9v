# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        g=head
        c=0
        while curr:
            c+=1
            curr=curr.next
        c=c-n
        k=0
        if c == 0:
            return head.next

        while head:
            k+=1
            if k==c:
                head.next=head.next.next
            head=head.next

        return g
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        y=head
        count=0
        while y:
            count+=1
            y=y.next
        z=count-n+1
        t=0
        print(count)
        print(head)
        if z==1:
            return head.next
        y=head
        for _ in range(z-2):
            y=y.next
        if y.next:
            y.next=y.next.next
        return head



        
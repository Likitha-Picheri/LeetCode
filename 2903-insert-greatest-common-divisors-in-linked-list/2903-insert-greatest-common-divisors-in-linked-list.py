import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
       
        while curr.next:
            temp=curr.next
            gcd1=math.gcd(curr.val,temp.val)
            t=ListNode(gcd1)
            curr.next=t
            t.next=temp
            curr=curr.next.next
           
        return head

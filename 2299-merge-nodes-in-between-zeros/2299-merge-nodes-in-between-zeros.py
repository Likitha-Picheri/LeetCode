# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        sum=0
        temp=curr
        while temp.next:
            temp=temp.next
            if temp.val==0:
                t=ListNode(sum)
                curr.next=t
                curr=curr.next
                sum=0
            sum+=temp.val
            
        return head.next


        
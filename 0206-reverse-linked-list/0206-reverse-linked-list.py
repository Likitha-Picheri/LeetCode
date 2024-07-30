# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        x=[]
        curr=head
        while curr:
            x.append(curr.val)
            curr=curr.next
        print(x)
        t=len(x)
        hea=node1=ListNode(x[-1])
        for i in range(1,len(x)):
            y=ListNode(x[t-i-1])
            node1.next=y
            node1=node1.next
        return hea
        
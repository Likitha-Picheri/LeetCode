# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        a=[]
        while temp:
            a.append(temp.val)
            temp=temp.next
        a.sort()
        temp1=head
        while temp1:
            temp1.val=a.pop(0)
            temp1=temp1.next
        return head
            
            


        
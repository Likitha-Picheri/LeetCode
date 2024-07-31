# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=None
      
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev

        # if not head:
        #     return head
        # x=[]
        # curr=head
        # while curr:
        #     x.append(curr.val)
        #     curr=curr.next
        # print(x)
        # t=len(x)
        # hea=node1=ListNode(x[-1])
        # for i in range(1,len(x)):
        #     y=ListNode(x[t-i-1])
        #     node1.next=y
        #     node1=node1.next
        # return hea
        
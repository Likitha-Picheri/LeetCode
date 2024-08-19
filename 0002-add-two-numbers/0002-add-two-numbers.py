# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        dummy=node
        sum=0
        rem=0
        curr1=l1
        curr2=l2
        t=0
        while(curr1 or  curr2 or rem):
            val1 =curr1.val if curr1 else 0
            val2=curr2.val if curr2 else 0
            x=val1+val2
            sum=val1+val2+rem
            rem=sum//10
            sum=sum%10
            # if x>9:
            #     x=x%10
            #     sum=x+rem
            #     rem=1
            # else:
            #     sum=x+rem
            #     rem=0
            
            if curr1:

                curr1=curr1.next
            if curr2:

                curr2=curr2.next
            dummy.next=ListNode(sum)
            dummy=dummy.next

        return node.next





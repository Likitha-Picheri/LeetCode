# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        length=length/2
        dumm=head

        while length>0:
            dumm=dumm.next
            length-=1
        return dumm

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        
        dummy=head
        ans=dummy.val
        dummy=dummy.next
        while dummy:
            ans=ans*2+dummy.val
            dummy=dummy.next
        return ans
        """
        :type head: ListNode
        :rtype: int
        """
        
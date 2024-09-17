# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        a=deque([root])
        cnt=0
        if root is None:
            return 0
        while a:
            node=a.popleft()
            cnt+=1
            if node:
                a.extend([node.left,node.right])
        return cnt//2
        

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        stack=[root]
        while stack:
            temp=stack.pop()
            if temp:
                a.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
        return a 
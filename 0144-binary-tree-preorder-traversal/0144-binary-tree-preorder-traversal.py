# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a=[]
        def preorder(root,a):
            if root==None:
                return None
            a.append(root.val)
            if root.left:
                preorder(root.left,a)
            if root.right:
                preorder(root.right,a)
            
        preorder(root,a)
        return a
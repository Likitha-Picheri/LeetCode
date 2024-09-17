# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def mirror(left1,right1):
            if not left1 and not right1:
                return True
            elif not left1 or not right1:
                return False
            else:
                return left1.val==right1.val and mirror(left1.left,right1.right) and mirror(left1.right,right1.left)
            
        return  mirror(root.left,root.right)
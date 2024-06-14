# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        else:

            left_height = height(root.left)
            right_height = height(root.right)
        
            if abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False








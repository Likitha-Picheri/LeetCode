# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def inorder(root1):
            if root is None:
                return None
            if root1:
                inorder(root1.left)
                ans.append(root1.val)
                inorder(root1.right)
        inorder(root)
        return ans[k-1]

        
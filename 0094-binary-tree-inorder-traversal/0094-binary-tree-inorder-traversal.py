# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stac=[]
        def inorder(root,stac):
            if root is None:
                return None
            inorder(root.left,stac)
            stac.append(root.val)
            inorder(root.right,stac)
        inorder(root,stac)
        return stac
        
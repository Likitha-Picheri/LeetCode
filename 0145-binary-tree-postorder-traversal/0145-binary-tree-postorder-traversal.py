# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stac=[]
        def postorder(root,stac):
            if root is None:
                return None
            if root.left is not None:
                postorder(root.left,stac)
            if root.right is not None:
                postorder(root.right,stac)
            stac.append(root.val)
        postorder(root,stac)
        return stac

        
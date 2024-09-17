# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stac=[root]
        ans=[]
        while stac:
            temp=stac.pop()
            if temp:
                ans.append(temp.val)
                stac.append(temp.left)
                stac.append(temp.right)
                
        return ans[::-1]

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        a=[]
        if root is None:
            return 0
        stack=[root]
        while stack:
            temp=stack.pop()
            if temp:
                if temp.left:
                    stack.append(temp.left)
                    stack.append(temp.right)
                a.append(temp.val)
        return len(a)

        
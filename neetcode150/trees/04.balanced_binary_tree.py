# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return 1
            lh = inorder(root.left)
            rh = inorder(root.right)
            if not lh or not rh or abs(lh-rh)>1:
                return 0
            return 1+max(lh,rh)
        return not inorder(root)==0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if not p and not q:
                return True
            if p and not q or q and not p or p.val!=q.val:
                return False
            return sametree(p.left,q.left) and sametree(p.right,q.right)
        def inorder(root):
            if not root:
                return False
            if sametree(root,subRoot):
                return True
            return inorder(root.left) or inorder(root.right)
        return inorder(root)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cur_dia = 0
        def inorder(root):
            if not root:
                return 0
            nonlocal cur_dia
            lh = inorder(root.left)
            rh = inorder(root.right)
            cur_dia = max(cur_dia,lh+rh)
            return 1+max(lh,rh)
        inorder(root)
        return cur_dia
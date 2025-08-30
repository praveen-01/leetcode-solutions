'''
basically preorder traversal [0] would be the root and that elemnt left in inorder would be left subtreee and right would be right subtree
use a map to find the idx in O(1) in inorder as we pop through each element in preorder traversal
we can use start and end pointers to track the subarrays in inorder
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i
        def construct_tree(start,end):
            if start>end: return None
            root = TreeNode(preorder[0])
            mid = d[preorder[0]]
            preorder.pop(0)
            root.left = construct_tree(start,mid-1)
            root.right = construct_tree(mid+1,end)
            return root
        return construct_tree(0,len(preorder)-1)
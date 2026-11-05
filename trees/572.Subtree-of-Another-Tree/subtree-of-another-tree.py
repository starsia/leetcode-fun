# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)

        if isSame(root, subRoot):
            return True
        elif not root:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


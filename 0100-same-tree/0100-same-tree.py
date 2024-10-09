# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.is_equal(p,q)

    def is_equal(self,root_1,root_2):
        if not root_1 and not root_2:
            return True
        elif not root_1 or not root_2:
            return False
        else:
            return root_1.val == root_2.val and self.is_equal(root_1.right,root_2.right) and self.is_equal(root_1.left,root_2.left) 

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanceAndHeight(root):
            if not root:
                return True, 0
            
            left_bool, left_h = balanceAndHeight(root.left)
            right_bool, right_h = balanceAndHeight(root.right)

            root_h = max(left_h, right_h) + 1
            root_bool = (abs(left_h - right_h) <= 1) and left_bool and right_bool

            return root_bool, root_h

        root_bool, _ = balanceAndHeight(root)
        return root_bool
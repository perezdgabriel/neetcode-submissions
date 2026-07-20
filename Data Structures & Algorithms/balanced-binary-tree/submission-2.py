# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = []

        def getHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            child = root
            height = 1 + max(getHeight(child.right), getHeight(child.left))
            return height
        
        def preorder(root: Optional[TreeNode]) -> None:
            if not root:
                return
            balanced.append(abs(getHeight(root.left) - getHeight(root.right)) <= 1)
            preorder(root.left)
            preorder(root.right)

        if root:
            preorder(root)
            return all(balanced)

        return True
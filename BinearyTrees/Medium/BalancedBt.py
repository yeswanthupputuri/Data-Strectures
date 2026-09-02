class Solution:
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    def isBalanced(self, root):
        if root is None:
            return True
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        if abs(leftheight - rightheight) > 1:
            return False 
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
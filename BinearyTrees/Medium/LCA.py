class Solution:
    def lowestcommonancestor(self, root, p, q):
        if root == p or root == q or root is None:
            return root
        left = self.lowestcommonancestor(root.left, p, q)
        right = self.lowestcommonancestor(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root
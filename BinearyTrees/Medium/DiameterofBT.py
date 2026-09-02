class Solution:
    def height(self, root, diameter):
        if not root:
            return 0
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        diameter[0] = max(diameter, lh + rh)
        return 1 + max(lh + rh)
        
    def diameterodBt(self, root):
        diameter = [0]
        self.height(root, diameter)
        return diameter[0]
    

    
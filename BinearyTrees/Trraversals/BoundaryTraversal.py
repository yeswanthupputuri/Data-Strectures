class Solution:
    def isleaf(self, root):
        return not root.left and not root.right
    
    def leftside(self, root, res):
        curr = root.left 
        while curr:
            if not self.isleaf(curr):
                res.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
                
    def rightside(self, root, res):
        curr = root.right
        temp = []
        while curr:
            if not self.isleaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        res.extend(temp[::-1])
                
    def leafnodes(self, root, res):
        if self.isleaf(root):
            res.append(root.data)
            return
        if root.left:
            self.leafnodes(root.left, res)
        if root.right:
            self.leafnodes(root.right, res)

    def boundary(self, root):
        res = []
        if not root:
            return root
        if not self.isleaf(root):
            res.append(root.data)
        self.leftside(root, res)
        self.leafnodes(root, res)
        self.rightside(root, res)
        return res
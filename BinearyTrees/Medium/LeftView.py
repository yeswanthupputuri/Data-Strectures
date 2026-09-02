# Recursive APPROACH

class Solution:
    def rightsideview(self, root):
        res = []
        self.recursiveright(root, 0, res)
        return res 
    
    def recursiveright(self, root, level, res):
        if root is None:
            return 
        if len(res) == level:
            res.append(root.data)
        self.recursiveright(root.right, level + 1, res)
        self.recursiveright(root.left, level + 1, res)
        
    def leftsideview(self, root):
        res = []
        self.recursiveleft(root, 0, res)
        return res 
    
    def recursiveleft(self, root, level, res):
        if root is None:
            return 
        if len(res) == level:
            res.append(root.data)
        self.recursiveright(root.left, level + 1, res)
        self.recursiveright(root.right, level + 1, res)
        
# Iterative Approach 
from collections import deque
class Solution:
    def rightview(self, root):
        res = []
        q = deque([root])
        while q:
            size = len(q)
            node = q.popleft()
            for i in range(size):
                if i == size - 1:
                    res.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
            
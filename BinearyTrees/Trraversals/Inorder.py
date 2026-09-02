# In-Order Traversal
class Solution:
    def recusiveapproch(self, root, arr):
        if root is None:
            return
        self.recusiveapproch(root.left, arr)
        arr.append(root.data)
        self.recusiveapproch(root.right, arr)
    def inorder(self, root):
        arr = []
        self.recusiveapproch(root, arr)
        return arr

#Pre-Order Traversal
class Solution:
    def recusiveapproch(self, root, arr):
        if root is None:
            return
        arr.append(root.data)
        self.recusiveapproch(root.left, arr)
        self.recusiveapproch(root.right, arr)
    def preorder(self, root):
        arr = []
        self.recusiveapproch(root, arr)
        return arr
    
#Post Order Traversal
class Solution:
    def recusiveapproch(self, root, arr):
        if root is None:
            return
        self.recusiveapproch(root.left, arr)
        self.recusiveapproch(root.right, arr)
        arr.append(root.data)
    def postorder(self, root):
        arr = []
        self.recusiveapproch(root, arr)
        return arr

# Level-Order Travesal : Queue Based Approach
from collections import deque
class Solution:
    def levelorder(self, root):
        q = deque([root])
        if not root:
            return ans
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans

                
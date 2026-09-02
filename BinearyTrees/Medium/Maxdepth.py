'''  
Given root of the binary tree, return its maximum depth.

A binary tree's maximum depth is number of nodes along the longest path from root node down to the farthest node.
'''

# Recursive Approch

class Solution:
    def maxdepth(self, root):
        if root is None:
            return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        return 1 + max(left, right)
    
# Recusive Approach 
from collections import deque
class Solution:
    def maxdepth(self, root):
        if root is None:
            return 0
        q = deque([root])
        level = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                front = q.popleft()
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            level += 1
        return level
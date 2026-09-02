from collections import deque
class Solution:
    def topview(self, root):
        ans = []
        if not root:
            return ans 
        mpp = {}
        q = deque([root, 0])
        while q:
            node, x = q.popleft()
            if x not in mpp:
                mpp[x] = node.data
            if node.left:
                q.append([node.left, x - 1])
            if node.right:
                q.append([node.right, x + 1])
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])
        return ans
            
                
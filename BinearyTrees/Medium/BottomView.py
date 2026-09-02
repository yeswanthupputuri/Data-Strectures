from collections import deque
class Solution:
    def bottomview(self, root):
        mpp = {}
        q = deque([root, 0])
        ans = []
        while q:
            node, x = q.popleft()
            mpp[x] = node.data
            if node.left:
                q.append((node.left, x - 1))
            if node.right:
                q.append((node.right, x + 1))
        for keys in sorted(mpp.keys()):
            ans.append(mpp[key])
        return ans
        
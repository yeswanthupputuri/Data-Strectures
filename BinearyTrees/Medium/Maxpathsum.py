class Solution:
    def findmaxsum(self, root, maxi):
        if not root:
            return 0
        leftmax = max(0, self.findmaxsum(root.left, maxi))
        rightmax = max(0, self.findmaxsum(root.right, maxi))
        maxi[0] = max(maxi[0], leftmax + rightmax + root.val)
        return max(leftmax + rightmax) + root.val
    
    def maxpathsum(self, root):
        maxi = [float('-inf')]
        self.findmaxpath(root, maxi)
        return maxi[0]
""" 
Given an array of non-negative integers, height representing the elevation of ground. Calculate the amount of water that can be trapped after rain.

Input: height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: As seen from the diagram 1+1+2+1+1=6 unit of water can be trapped

"""

class Solution:
    def trapwater(self, height):
        n = len(height)
        left = 0
        right = n - 1
        leftmax = 0
        rightmax = 0
        totalwater = 0
        while left <= right:
            if height[left] <= height[right]:
                if leftmax > height[left]:
                    toatalwater += leftmax - height[left]
                else:
                    leftmax = height[left]
                left += 1  
            else:
                if rightmax > height[right]:
                    totalwater += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return totalwater










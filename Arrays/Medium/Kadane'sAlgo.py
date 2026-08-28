''' 
find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1
Input: nums = [2, 3, 5, -2, 7, -4]
Output: 15
'''
class Solution:
    def maxsubArray(self, nums):
        sum = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi
    
'''  
Printing the subarray that has the max sum?
'''

class Solution:
    def maxsubArray(self, nums):
        sum = 0
        maxi = float('-inf')
        start = 0
        ansstart = -1
        ansend = -1 
        for i in range(len(nums)):
            if sum == 0:
                start = i
            sum += nums[i]
            if sum > maxi:
                maxi = sum 
                ansstart = start
                ansend = i
            if sum < 0:
                sum = 0
        return nums[ansstart:ansend + 1]
'''  
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
'''

# If arrays consists of both positives and negative elements 

class Solution:
    def countSunarrays(self, nums, k):
        n = len(nums)
        cnt = 0
        sum = 0
        mpp ={0:1}
        for i in range(n):
            sum += nums[i]
            rem = sum - k
            if rem in mpp:
                cnt += mpp[rem]
            mpp[sum] = mpp.get(sum, 0) + 1
        return cnt
    # Time Complexity : O(N) or O(nlogn) , Depends on map DS used if we are using C++ , which we take unodered map it takes logn.


# If array consists of Positive integers
class Solution:
    def numofsubarrays(self, nums, goal):
        return self.noofsubarrayslessthanequaltogoal(nums, goal) - self.noofsubarrayslessthanequaltogoal(nums, goal - 1)
    
    def noofsubarrayslessthanequaltogoal(self, nums, goal):
        if goal < 0:
            return 0
        l, r = 0, 0
        sum = 0
        cnt = 0
        while r < len(nums):
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            cnt += (r - l + 1)
            r += 1
        return cnt 
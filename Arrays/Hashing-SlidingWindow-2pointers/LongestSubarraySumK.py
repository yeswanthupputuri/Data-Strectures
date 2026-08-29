''' 
Longest subarray with sum K :
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

'''
# If the Array Consists of both Positives and Negatives

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        mpp = {}
        max_len = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            rem = sum - k
            if sum == k:
                max_len = max(max_len, i + 1)
            if rem in mpp:
                length = i - mpp[rem]
                max_len = max(max_len, length)
            if sum not in mpp:
                mpp[sum] = i
        return max_len
    # Time Complexity : O(N) or O(nlogn)

# if Array Consists of only positive numbers

class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        max_len = 0
        sum = nums[0]
        right = 0
        left = 0
        while right < n:
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            if sum == k:
                max_len = max(max_len, right - left + 1)
            right += 1
            if right < n:
                sum += nums[right]
        return max_len
        # Time Complexity : O(N)
        
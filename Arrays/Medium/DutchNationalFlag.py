'''  
An array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.

Dutch National Flag Algorithm
'''

class Solution:
    def sortZerosoneTwo(self, nums):
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
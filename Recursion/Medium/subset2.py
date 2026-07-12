""" 
Given an integer array nums, which can have duplicate entries, provide the power set.
Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.

Example -->
Input : nums = [1, 2, 2]
Output : [ [ ] , [1] , [1, 2] , [1, 2, 2] , [2] , [2, 2] ]
"""

class Solution:
    def possible(self, index, current, result, nums):
        if index == len(nums):
            result.append(current[:])
            return 
        current.append(nums[index])
        self.possible(index + 1, current, result, nums)
        current.pop()
        for i in range(index + 1, len(nums)):
            if nums[i] != nums[index]:
                self.possible(i, current, result, nums)
        self.possible(index + 1, current, result, nums)
        
    def subset2(self, nums):
        result = []
        current = []
        self.possible(0, current, result, nums)
        return result
        
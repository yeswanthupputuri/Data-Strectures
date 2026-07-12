""""  
Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.
Do not include the duplicates in the answer.

Example 1
Input : nums = [1, 2, 3]
Output : [ [ ] , [1] , [2] , [1, 2] , [3] , [1, 3] , [2, 3] , [1, 2 ,3] ]
"""
class Solution:
    def possible(self,index, current, result, nums):
        if index == len(nums):
            result.append(current[:])
            return
        current.append(nums[index])
        self.possible(index + 1, current, result, nums)
        current.pop()
        self.possible(index + 1, current, result, nums)
        
    def powerset(self, nums):
        n = len(nums)
        result = []
        current = []
        self.possible(0,current,result,nums)
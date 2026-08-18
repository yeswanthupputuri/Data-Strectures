class Solution:
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]
        
    def possible(self, index, ans, nums):
        if index == len(nums):
            ans.append(nums[:])
            return 
        for i in range(index, len(nums)):
            self.swap(index, i, nums)
            self.possible(index + 1, ans, nums)
            self.swap(i, index, nums)
            
    def permute(self, nums):
        n = len(nums)
        ans = []
        self.possible(0, ans, nums)
        return ans
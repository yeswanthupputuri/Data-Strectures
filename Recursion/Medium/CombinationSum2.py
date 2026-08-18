class Solution:
    def possible(self, index, current, ans, nums, sum, n):
        if sum < 0 or index == n:
            return
        if sum == 0:
            ans.append(current[:])
            return
        
        current.append(nums[index])
        self.possible(index + 1, current, ans, nums, sum - nums[index], n)
        current.pop()
        for i in range(index + 1, n):
            if nums[i] != nums[index]:
                self.possible(i, current, ans, nums, sum, n)
                break 
                    
    def combinationsum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = []
        current = []
        self.possible(0, current, ans, nums, target, n)
        return ans
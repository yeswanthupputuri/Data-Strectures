class Solution:
    def possibilites(self, index, current, ans, nums, target, n):
        if target < 0:
            return
        if target == 0:
            ans.append(current[:])
            return
        if index == n:
            if target == 0:
                ans.append(current[:])
                return
        current.append(nums[index])
        self.possibilities(self, index, current, ans, nums, target - nums[index], n)
        current.pop()
        self.possibilities(self, index + 1, current, ans, nums, target, n)
        
    def combination(self, nums, target):
        n = len(nums)
        current = []
        ans = []
        self.possibilities(0, current, ans, nums, target, n)
        return ans
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        mpp = {}
        for i in range(n):
            curr = nums[i]
            required = target - curr
            if required in mpp:
                return [i, mpp[required]]
            mpp[curr] = i
        return False
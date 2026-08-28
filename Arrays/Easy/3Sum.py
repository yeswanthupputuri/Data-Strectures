class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]
                if sum_val < 0:
                    j += 1
                elif sum_val > 0: 
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k += 1
        return ans
    
'''  
Time Complexity : O(nlogn) + 0(n^2)
'''
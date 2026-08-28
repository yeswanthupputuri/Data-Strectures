class Solution:
    def reversePairs(self, nums):
        return self.mergesort(nums, 0, len(nums) - 1)
    
    def mergesort(self, nums, low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        cnt = 0
        cnt += self.mergesort(nums, low, mid)
        cnt += self.mergesort(nums, mid+1, high)
        cnt += self.countpairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)  
        return cnt 
    
    def countpairs(self, nums, low, mid, high):
        cnt = 0
        right = mid + 1
        for i in range(low, mid+1):
            while nums[i] > 2 * nums[right]:
                right += 1
            cnt += right - ( mid + 1)
        return cnt
            

    def merge(self, nums, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid :
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        nums[low:high + 1] = temp
class Solution:
    def merge(self,arr,low,mid,high):
        st = []
        left = low
        right = mid+1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                st.append(arr[left])
                left += 1
            else:
                st.append(arr[right])
                right += 1
        while left <= mid:
            st.append(arr[left])
            left += 1
        while right <= high:
            st.append(arr[right])
            right += 1
        for i in range(low,high+1):
            arr[i] = st[i - low]
            
    def mergeflow(self, arr, low, high):
        if low >= high:
            return 
        mid = (low + high) // 2
        self.mergeflow(arr,low,mid)
        self.mergeflow(arr,mid+1,high)
        self.merge(arr,low,mid,high)
        
    def mergesort(self, nums):
        n = len(nums)
        self.mergeflow(nums,0,n-1)
        return nums
        
# Time Complexity: O(nlogn). 
# At each step, we divide the whole array, which takes logn steps, and we assume n steps are taken to sort the array. So, the overall time complexity is nlogn.
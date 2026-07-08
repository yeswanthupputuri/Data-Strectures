

class Solution:
    def nextgreatestelement(self,nums):
        st = []
        n = len(nums)
        nge = [0] * n
        for ind in range(n - 1, -1, -1):
            while st and st[-1] <= nums[ind]:
                st.pop()
            if not st:
                nge[ind] = -1
            else:
                nge[ind] = st[-1]
            st.append(nums[ind])
        return nge
            
"""
if given array circular integer array then we can use the below code

class Solution:
    def nextGreaterElements(self, arr):
        n = len(arr)
        ans = [0] * n 
        st = []
        for i in range(2 * n - 1, -1, -1):
            ind = i % n
            currele = arr[ind]
            while st and st[-1] <= currele:
                st.pop()
            if not st:
                ans[ind] = -1
            else:
                ans[ind] = st[-1]
            st.append(currele)
        return ans
        
"""         
class Solution:
    def nextgreatestelement(self,nums):
        st = []
        n = len(nums)
        nse = [0] * n
        for ind in range(n - 1, -1, -1):
            while st and st[-1] >= nums[ind]:
                st.pop()
            if not st:
                nse[ind] = -1
            else:
                nse[ind] = st[-1]
            st.append(nums[ind])
        return nse
            
            
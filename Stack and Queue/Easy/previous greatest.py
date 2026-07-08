class Solution:
    def previousgreatestelement(self,nums):
        st = []
        n = len(nums)
        pge = [0] * n
        for ind in range(n):
            while st and st[-1] <= nums[ind]:
                st.pop()
            if not st:
                pge[ind] = -1
            else:
                pge[ind] = st[-1]
            st.append(nums[ind])
        return pge
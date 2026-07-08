class Solution:
    def previoussmallestelement(self,nums):
        st = []
        n = len(nums)
        pse = [0] * n
        for ind in range(n):
            while st and st[-1] >= nums[ind]:
                st.pop()
            if not st:
                pse[ind] = -1
            else:
                pse[ind] = st[-1]
            st.append(nums[ind])
        return pse
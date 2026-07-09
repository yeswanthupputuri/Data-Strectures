class Solution:
    def prevsmall(self, nums):
        st = []
        n = len(nums)
        pse = [0] * n
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                pse[i] = st[-1]
            else:
                pse[i] = -1
            st.append(i)
        return pse

    def nextsmall(self, nums):
        st = []
        n = len(nums)
        nse = [0] * n
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            else:
                nse[i] = n
            st.append(i)
        return nse

    def sumofmini(self, nums):
        n = len(nums)
        mod = 10**9 + 7
        total = 0
        pse = self.prevsmall(nums)
        nse = self.nextsmall(nums)
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            possibilities = left * right * 1
            currvalue = ( possibilities * nums[i]) % mod
            total = (total + currvalue) % mod
        return total
            
class Solution:
    def findpge(self, arr):
        n = len(arr)
        st = []
        ans = [0] * n
        for i in range(n):
            currele = arr[i]
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            if not st:
                ans[i] = -1
            else:
                ans[i] = st[-1]
            st.append(i)
        return ans
    def stockSpan(self, arr, n):
        pge = self.findpge(arr)
        ans = [0] * n 
        for i in range(n):
            ans[i] = i - pge[i]
        return ans
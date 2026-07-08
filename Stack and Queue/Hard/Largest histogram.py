class Solution:
    def largehistogram(self, heights):
        n = len(heights)
        nse, pse = 0, 0
        area = 0
        largestarea = 0
        st = []
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                nse = i
                ind = st.pop()
                pse = st[-1] if st else -1
                area = heights[ind] * (nse - pse - 1)
                largestarea = max(largestarea, area)
            st.append(i)
        while st:
            nse = n
            ind = st.pop()
            pse = st[-1] if st else -1
            area = heights[ind] * (nse - pse - 1)
            largestarea = max(largestarea, area)
        return largestarea
            
        
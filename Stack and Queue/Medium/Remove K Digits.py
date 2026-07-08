class Solution:
    def removekdigit(self, nums, k):
        st = []
        for num in nums:
            while st and st[-1] > num and k > 0:
                st.pop()
                k -= 1
            st.append(num)
        while st and k > 0:
            st.pop()
            k -= 1
        if not st:
            return "0"
        result = ""
        while st:
            result += st.pop()
        result = result.lstrip("0")
        result = result[::-1]
        if not result:
            return "0"
        return result
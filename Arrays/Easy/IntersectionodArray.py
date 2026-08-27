class Solution:
    def intersectionArray(self, nums1, nums2):
        i = 0
        j = 0
        n = len(nums1)
        m = len(nums2)
        st = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if nums1[i] == nums2[j]:
                    st.append(nums1[i])
                    i += 1
                    j += 1
        return st
  
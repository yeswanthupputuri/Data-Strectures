class Solution:
    def unionArray(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        st = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if not st or st[-1] != nums1[i]:
                    st.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                if not st or st[-1] != nums2[j]:
                    st.append(nums2[j])
                j += 1
            else:
                if not st or st[-1] != nums2[j]:
                    st.append(nums2[j])
                i += 1
                j += 1
        while i < n:
            if not st or st[-1] != nums1[i]:
                st.append(nums1[i])
            i += 1
        while j < m:
            if not st or st[-1] != nums2[j]:
                st.append(nums2[j])
            j += 1
        return st
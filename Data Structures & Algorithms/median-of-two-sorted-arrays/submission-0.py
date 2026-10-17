class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        N = len(nums1) + len(nums2)
        half = int(N / 2)
        l, r = 0, len(nums1) - 1
        while True:
            m = (l + r) // 2
            k = half - m - 2
            Aleft = nums1[m] if m >= 0 else float("-infinity")
            Aright = nums1[m + 1] if (m + 1) < len(nums1) else float("infinity")
            Bleft = nums2[k] if k >= 0 else float("-infinity")
            Bright = nums2[k + 1] if (k + 1) < len(nums2) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if N % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1

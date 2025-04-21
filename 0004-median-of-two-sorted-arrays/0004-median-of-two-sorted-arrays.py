class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2,nums1
        total = len(nums1)+len(nums2)
        half = total//2

        l , r = 0 , len(nums1)-1

        while True:
            midA = (l+r)//2
            midB = half - midA - 2
            Aleft = nums1[midA] if midA >= 0 else float("-inf")
            Aright = nums1[midA+1] if midA+1 < len(nums1) else float("inf")
            Bleft = nums2[midB] if midB >= 0 else float("-inf")
            Bright = nums2[midB+1] if midB+1 < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft,Bleft) + min(Bright,Aright)) / 2.0
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1
   
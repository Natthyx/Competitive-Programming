class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n= len(nums1)
        if n % 2 ==1:
            return nums1[n//2]
        else:
            mid1 = nums1[n//2 - 1]
            mid2 = nums1[n//2]
            return (mid1+mid2)/2
            
            
            
            
            
            
            
            
        
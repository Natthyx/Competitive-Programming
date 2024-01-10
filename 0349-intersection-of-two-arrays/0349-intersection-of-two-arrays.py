class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    result.add(i)
        return result
        
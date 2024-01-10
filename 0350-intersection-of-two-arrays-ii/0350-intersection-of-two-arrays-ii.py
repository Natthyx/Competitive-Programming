class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequency1 = {}
        frequency2 = {}

        
        for num in nums1:
            frequency1[num] = frequency1.get(num, 0) + 1

        
        for num in nums2:
            frequency2[num] = frequency2.get(num, 0) + 1

        result = []
        for num in nums1:
            if num in frequency2 and frequency2[num] > 0:
                result.append(num)
                frequency2[num] -= 1

        return result

        
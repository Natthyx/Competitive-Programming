class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = 0
        ptr2 = 0
        
        while ptr2 < n:
            if nums1[ptr1] == 0 and ptr1 >= m+ptr2:
                nums1.insert(ptr1, nums2[ptr2])
                ptr2 += 1
                nums1.pop()
            elif nums1[ptr1] <= nums2[ptr2]:
                ptr1 += 1
                continue
            else:
                nums1.insert(ptr1, nums2[ptr2])
                ptr2 += 1
                nums1.pop()
            
            ptr1 += 1
        
        return nums1
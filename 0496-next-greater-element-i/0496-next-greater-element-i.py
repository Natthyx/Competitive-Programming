class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        store = defaultdict(int)
        res = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                a = stack.pop()
                store[a]=nums2[i]
            else:
                stack.append(nums2[i])
                store[stack[-1]]= -1

        for i in range(len(nums1)):
            res.append(store[nums1[i]])

        return res


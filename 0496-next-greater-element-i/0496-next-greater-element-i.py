class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        
        next_greater_element = {
            1: 3
            3: 4
            4: 0
            2: 0
        }
        store = []
        
        [1,1,4,2]
                 
        [4,1,2]
        -1 3 -1

        '''

        next_greater_element = defaultdict(int)
        stack = []

        # iterate on second array and store it's next greater element
        for i in range(len(nums2)):
            # stack not empty and the stack top element less than the curr element
            while stack and stack[-1] < nums2[i]:
                num = stack.pop()
                next_greater_element[num] = nums2[i]
            else:
                stack.append(nums2[i])
                next_greater_element[stack[-1]] = -1
            
        
        stack.clear()
        # iterate on the first array and retrive our ans from the next_greate_element
        for num in nums1:
            stack.append(next_greater_element[num])

        return stack




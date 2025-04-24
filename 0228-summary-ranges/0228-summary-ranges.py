class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        "a->b" if a != b
        "a" if a == b

        [0,1,2,4,5,7]
        - using two pointer 
        - iterate on nums and check the difference between curr index and next index is one
        - when we find that don't satisfy the above we can check the two pointers checking if they are in the same or not so we can choose the return method from the above two
          i
        [0,2,4,5,7]
           j

        res.append("nums[i]->nums[j]")

        '''
        res = []
        i , j = 0 , 0

        while j < len(nums):
            if j == len(nums)-1 or nums[j+1]-nums[j]!=1:
                if nums[i] == nums[j]:
                    res.append(str(nums[i]))
                else:
                    res.append(f"{nums[i]}->{nums[j]}")
                i = j + 1  
            j+=1
        return res
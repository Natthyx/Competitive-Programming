class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = defaultdict(int)
        prefix = nums[0]
        prefix_arr = [0]*(len(nums))
        freq[0] = 1
        prefix_arr[0]=nums[0]

        for i in range(1,len(nums)):
            prefix+= nums[i]
            prefix_arr[i] = prefix


        count = 0
        print(prefix_arr)
        print(freq)
        for i in range(len(prefix_arr)):
            diff = prefix_arr[i] - goal
            if diff in freq.keys():
                count += freq[diff]

            freq[prefix_arr[i]]+=1



        return count


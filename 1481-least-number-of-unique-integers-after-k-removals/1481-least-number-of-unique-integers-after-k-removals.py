class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        number = {}
        for i in arr:
            number[i] = number.get(i,0)+1
        
        frequency = list(number.values())
        frequency.sort()
        
        element_removed = 0
        
        for i in range(len(frequency)):
            element_removed += frequency[i]
            
            if element_removed > k:
                return len(frequency) - i
        return 0
        
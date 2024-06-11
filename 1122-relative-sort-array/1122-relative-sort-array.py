class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        notfound = []
        
        for k in arr1:
            if k not in arr2:
                notfound.append(k)
        for i in arr2:
            for j in arr1:
                if j == i:
                    res.append(j)
                
        notfound.sort()
        for i in notfound:
            res.append(i)
        return res
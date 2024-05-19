class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = {}
        for i, j in items1:
            res[i]=j
        for i, j in items2:
            if i in res:
                res[i]+=j
            else:
                res[i]=j
        ans = []
        for key,value in res.items():
            ans.append([key,value])
            
        sorted_list = sorted(ans, key=lambda x: x[0])      
        return sorted_list
                
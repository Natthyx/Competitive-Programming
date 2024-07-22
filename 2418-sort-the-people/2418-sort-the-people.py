class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDict = {}
        res = []
        for i in range(len(heights)):
            heightDict[i]= heights[i]
   
        sorted_heights = dict(sorted(heightDict.items(), key=lambda x:x[1], reverse = True))
        # print(sorted_heights)
        
        for i in sorted_heights.keys():
            res.append(names[i])
        
        return res
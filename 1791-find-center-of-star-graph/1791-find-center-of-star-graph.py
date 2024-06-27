class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        arr = []
        for x,y in edges:
            arr.append(x)
            arr.append(y)
            
        count = Counter(arr)
        
        for key,value in count.items():
            if value == max(count.values()):
                return key
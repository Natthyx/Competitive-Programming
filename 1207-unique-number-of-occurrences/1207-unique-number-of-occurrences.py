class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lst = defaultdict()
        for i in arr:
            lst[i]=lst.get(i,0)+1
        return len(lst) == len(set(lst.values()))
       
            
            
         
        
                           
                           
                           
        
            
        
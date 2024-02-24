class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {}
        s_map = {}
        
        for idx, char in enumerate(order):
            order_map[char] = idx
        
        for idx , char in enumerate(s):
            s_map[char] = s_map.get(char,0)+1
        
        ans = ''
        
        for key, value in order_map.items():
            if key in s_map:
                ans = ans + key * s_map[key]
                
        for key, value in s_map.items():
            if key not in order_map:
                ans = ans + key * value
                
        return ans
        
            
        
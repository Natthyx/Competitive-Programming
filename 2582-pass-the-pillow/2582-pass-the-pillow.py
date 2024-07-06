class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_pillow = 1
        current_time = 0
        direction =1
        
        while current_time < time:
            if 0<current_pillow + direction <=n:
                current_pillow+=direction
                current_time+=1
            else:
                direction*= -1
        return current_pillow
        
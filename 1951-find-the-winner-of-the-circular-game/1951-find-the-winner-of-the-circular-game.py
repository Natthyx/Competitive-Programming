class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        
        i = 0
        while len(friends) > 1:
            losser = (i+k-1)%len(friends)
            i = losser
            
            friends.pop(losser)
            

        return friends[0]
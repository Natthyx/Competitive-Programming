class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for i in range(len(bills)):
            if bills[i] == 5:
                change[5]+=1
            elif bills[i] == 10:
                if change[5] >= 1:
                    change[5]-=1
                    change[10]+=1
                else:
                    return False
                
            elif bills[i] == 20:
                if change[5] >=1 and change[10]>=1:
                    change[5]-=1
                    change[10]-=1
                    change[20]+=1
                elif change[5] >=3:
                    change[5]-=3
                    change[20]+=1
                else:
                    return False

        return True


        

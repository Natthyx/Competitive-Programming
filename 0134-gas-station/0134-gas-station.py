class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = []
        i = 0

        while i < len(gas):
            arr.append(gas[i]-cost[i])
            i+=1

        sm = sum(arr)
        arr.extend(arr)
        if sm < 0:
            return -1
        else:
            ans = -1
            ind = 0
            flag = False
            print(len(arr))
            for i in range(len(arr)):
                if arr[i] >= 0:
                    if not flag:
                        flag = True
                        ind = i
                if flag:  
                    if ans == -1:
                        ans = 0  
                        
                    ans+=arr[i]
                
                if ans < 0:
                    flag = False
                    ans = -1
                if ans == sm and i >= (len(arr)//2) - 1:
                    return ind
                    

                


            


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def cal(first, second):
            arr = [str(first),str(second)]

            total = sum(len(x) for x in arr)

            while total < len(num):
                arr.append(str(int(arr[-1]) + int(arr[-2])))
                total += len(arr[-1])
            
            return "".join(arr)

        
        for left in range(1, len(num)):
            for right in range(left+1, len(num)):
                if num[left] == "0" and right - left > 1:
                    break
                
                first = int(num[:left])
                second = int(num[left:right])

                s = cal(first,second)
                if s == num:
                    return True

            if num[0] == "0":
                break
        return False
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answerKey = list(answerKey)
        my_dict = defaultdict(int)
        maxP = 0
        left = 0
        
        for right in range(len(answerKey)):
            my_dict[answerKey[right]]+=1
            
            n = max(my_dict.values())
            
            while (right-left+1)-n > k:
                my_dict[answerKey[left]]-=1
                left+=1
            maxP = max(maxP,right-left+1)
            
        return maxP
        
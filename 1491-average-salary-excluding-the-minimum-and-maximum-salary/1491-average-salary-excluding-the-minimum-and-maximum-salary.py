class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sums = 0
        for i in range(1,len(salary)-1):
            sums += salary[i]
            ave = sums / (len(salary)-2)
        return ave
            
        
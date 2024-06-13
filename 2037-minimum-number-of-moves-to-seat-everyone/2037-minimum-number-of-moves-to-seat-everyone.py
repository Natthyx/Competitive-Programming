class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0 
        
        i , j = 0 ,0 
        
        while i < len(seats) and j < len(students):
            res += abs(students[j] - seats[i])
            i+=1
            j+=1
        return res
        
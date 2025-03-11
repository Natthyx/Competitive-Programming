class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        arr = []
        prev = self.getRow(rowIndex-1)
        for i in range(len(prev)-1):
            arr.append(prev[i]+prev[i+1])

        return [1]+arr+[1]
        
        
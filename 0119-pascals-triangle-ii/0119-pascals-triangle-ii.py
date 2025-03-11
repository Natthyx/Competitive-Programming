class Solution:
    @cache
    def triangle(self, row, col):

        if col == 0:
            return 1
        if row == col:
            return 1
        return self.triangle(row-1,col-1)+self.triangle(row-1,col)


    def getRow(self, rowIndex: int) -> List[int]:
        
        arr = []
        for col in range(0,rowIndex+1):
            arr.append(self.triangle(rowIndex,col))
        return arr
        
        
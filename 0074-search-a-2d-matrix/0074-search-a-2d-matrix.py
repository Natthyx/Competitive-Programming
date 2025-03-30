class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchInRow(target):
            l , r = 0 , len(matrix)-1

            while l <= r:
                mid = (l+r)//2
            
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            
            return r

        
        def searchinCol(i):
            l , r = 0 , len(matrix[i])-1

            while l<= r:
                mid = (l+r)//2

                if matrix[i][mid]== target:
                    return True

                elif matrix[i][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return False

        x = searchInRow(target)

        if x is True:
            return True

        if x < 0:
            return False

        return searchinCol(x)
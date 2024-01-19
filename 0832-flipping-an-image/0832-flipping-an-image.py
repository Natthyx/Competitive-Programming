class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left , right = 0 , len(row)-1
            while left<= right:
                row[left] , row[right] = 1-row[right] , 1 - row[left]
                left+=1
                right-=1
        return image
#         for row in image:
#             row.reverse()
            
#             for i in range(len(row)):
#                 row[i] = 1- row[i]
#         return image
            
        
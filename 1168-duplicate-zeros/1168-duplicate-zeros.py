class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        temp = []
        for i in range(len(arr)):
            if arr[i]==0:
                temp.extend([0,0])
            else:
                temp.append(arr[i])

        for i in range(len(arr)):
            arr[i]=temp[i]
                


                
                

                

        
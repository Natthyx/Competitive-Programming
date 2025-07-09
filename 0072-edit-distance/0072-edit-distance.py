class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        logic behind it
        i start from 0 and goes to len(word1)
        j start from 0 and goes to len(word2)
        - if word1[i] == word2[j] -> 0(no operation needed) + (i+1, j+1)
        else:
            delete -> 1+ (i+1, j)
            insert -> 1+ (i, j+1)
            update -> 1+ (i+1,j+1)
        '''
        cache = [[float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word2)+1):
            cache[len(word1)][i] = len(word2) - i
        
        for j in range(len(word1)+1):
            cache[j][len(word2)] = len(word1) - j
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])
        
        return cache[0][0]


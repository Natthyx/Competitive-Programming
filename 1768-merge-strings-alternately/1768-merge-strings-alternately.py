class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        merged = ""
        for i in range(min_len):
            merged += word1[i]+word2[i]
        merged += word1[min_len:]+ word2[min_len:]
        return merged

        
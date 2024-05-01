class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            ind_ch = word.index(ch)
            rev_word = word[:ind_ch+1][::-1] + word[ind_ch+1:]

            return rev_word
        
        
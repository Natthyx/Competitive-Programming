class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        def get_original_position(word):
            return int(word[-1])
        words.sort(key=get_original_position)
        original_sentence = ' '.join(word[:-1] for word in words)

        return original_sentence
        
        
        
        
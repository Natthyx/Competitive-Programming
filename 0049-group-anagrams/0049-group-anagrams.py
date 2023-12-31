from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        result = []
        for s in strs:
            sorted_a = tuple(sorted(s))
            anagram[sorted_a].append(s)
        for value in anagram.values():
            result.append(value)
        return result
            
        
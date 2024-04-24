class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s= list(s)
        count = Counter(s)
        values = list(count.values())
        return all(value == values[0] for value in values)
        
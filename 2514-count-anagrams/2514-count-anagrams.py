class Solution:
    def countAnagrams(self, s: str) -> int:
        def fact(n):
            product = 1
            for num in range(2, n + 1):
                product = (product * num) % M
            return product

        M = 1000000007
        numerator, denominator = 1, 1

        for word in s.split():
            numerator = (numerator * fact(len(word))) % M
            for count in collections.Counter(word).values():
                denominator = (denominator * fact(count)) % M

        return (numerator * pow(denominator, -1, M)) % M
        
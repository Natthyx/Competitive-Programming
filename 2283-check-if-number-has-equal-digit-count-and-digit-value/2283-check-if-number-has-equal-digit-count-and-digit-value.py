class Solution:
    def digitCount(self, num: str) -> bool:
        marked = set()
        k = 0
        while k<len(num):
            if num[k] not in marked:
                count = num.count(str(k))
                if int(num[k]) != count:
                    return False
                else:
                    marked.add(num[k])
                    k += 1
            else:
                k += 1
        return True
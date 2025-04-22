class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ln = len(deck)
        ans = [0]*ln
        queue = deque(range(ln))
        i = 0
        while queue:
            ind = queue.popleft()
            ans[ind] = deck[i]
            i+=1
            if queue:
                queue.append(queue.popleft())

        return ans

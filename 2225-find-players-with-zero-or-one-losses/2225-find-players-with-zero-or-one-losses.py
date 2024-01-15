class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_dict = defaultdict(int)
        first = set()
        arr = []
        for winner, loser in matches:
            loser_dict[loser] += 1
        for winner, loser in matches:
            if loser_dict[winner] == 0:
                first.add(winner)
        for key, value in loser_dict.items():
            if value == 1:
                arr.append(key)
        
        first_list = list(first)
        first_list.sort()
        arr.sort()
        return [first_list,arr]
        
        
        
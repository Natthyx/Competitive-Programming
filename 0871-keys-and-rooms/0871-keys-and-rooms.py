class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        keys.add(0)

        def dfs(node,visited):
            visited.add(node)

            for n in rooms[node]:
                keys.add(n)
                if n not in visited:
                    dfs(n,visited)

            
        dfs(0,set())

        for i in range(len(rooms)):
            if i not in keys:
                return False

        return True

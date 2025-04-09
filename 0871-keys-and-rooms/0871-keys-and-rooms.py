class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node,visited):
            visited.add(node)

            for n in rooms[node]:
                if n not in visited:
                    dfs(n,visited)

        visited = set()
        dfs(0,visited)

        return len(visited)== len(rooms)

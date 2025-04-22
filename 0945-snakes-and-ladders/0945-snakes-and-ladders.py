class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ln = len(board)
        board.reverse()
        def helper(square):
            row = ((square-1) // ln)
            col = (square-1) % ln
            if row % 2:
                col = ln - 1 - col
            return [row,col]
        
        queue = deque()
        visited = set()
        queue.append([1,0])

        while queue:
            sqr , move = queue.popleft()

            for i in range(1,7):
                new_sqr = sqr + i

                r , c = helper(new_sqr)
                if board[r][c] != -1:
                    new_sqr = board[r][c]
                if new_sqr == ln**2:
                    return move + 1
                if new_sqr not in visited:
                    visited.add(new_sqr)
                    queue.append([new_sqr, move + 1])
        return -1
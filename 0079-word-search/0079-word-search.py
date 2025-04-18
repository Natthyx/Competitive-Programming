class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        visited = [[False]*len(board[0])]
        
        def checker(row,col,ind,visited):
            visited.add((row,col))
            if ind == len(word):
                return True
            
            for r , c in direction:
                new_row , new_col = row + r , col + c

                if inbound(new_row,new_col) and ((new_row,new_col) not in visited) and board[new_row][new_col] == word[ind]:
                    if checker(new_row,new_col,ind+1,visited):
                        return True

            visited.remove((row,col))
            return False

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if checker(i,j,1,visited):
                        return True
        return False

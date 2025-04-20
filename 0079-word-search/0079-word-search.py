class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_char = Counter(char for row in board for char in row)
        word_char = Counter(word)

        for ch in word_char:
            if word_char[ch] > board_char[ch]:
                return False
        
        if board_char[word[0]] > board_char[word[-1]]:
            word = word[::-1]

        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def checker(row,col,ind,visited):
            visited[row][col] = True
            if ind == len(word):
                return True
            
            for r , c in direction:
                new_row , new_col = row + r , col + c

                if inbound(new_row,new_col) and ( not visited[new_row][new_col]) and board[new_row][new_col] == word[ind]:
                    if checker(new_row,new_col,ind+1,visited):
                        return True

            visited[row][col] = False
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False]*len(board[0]) for _ in range(len(board))]
                    if checker(i,j,1,visited):
                        return True
        return False

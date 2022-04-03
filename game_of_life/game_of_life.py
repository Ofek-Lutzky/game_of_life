import random


class Board: # the board class build me a board object
    def __init__(self, length = 0, width = 0): # init to make a board object at len, and width we want
        #if the player want borad at size (len, width)
        self.len = length
        self.wid = width
        board = [[0 for _ in range(width)] for x in range(length)] # making a list of lists according to the user input
        self.board = board

    #the next two func is helping me make a random board with random live\dead cells
    def random_board_size(self):
        self.len  =  random.randint(20,50)#TODO change to 0,500
        self.wid = random.randint(20,50)
        board = Board(self.len, self.wid) # i want that my random board will be no more then 100,100 size
        return board

    def random_the_board_inside(self): #TODO make a full random board with live and dead cells (0/1)
        self = self.random_board_size()
        for i in range(0,self.len-1):
            for j in range(0,self.wid-1):
                self.board[i][j] = random.randint(0,1)
        return self

    def __repr__(self): # the func help me to print the board without ".board" a method in python
        return str(self.board)




def checker(board): #the func will send each cell to the helper and fix the board according to the lows and will return the new board
    for i  in range(len(board)-1):
        for j  in range(len(board[0])-1):
            print(i,j)
            board = checker_helper(i,j,board)
            print(board)

    return board



def checker_helper(r, c, board):  # -->check each sell: will help us to get over each one and fix it
    moves = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1),
             (0, 1)]  # all the moves that available in matrix for each cell  ( raw, column)
    counter = 0  # will help us determine the cell situation and count the alive's cell around him
    # print(r, c)
    for move in moves:
        if 0 <= move[0] + r < len(board) and 0 <= move[1] + c < len(board[0]):
            if board[move[0] + r][move[1] + c] == 1:
                counter += 1

    # situation 1 + situation 2
    if board[r][c] == 1 and counter == 0 or board[r][c] == 1 and counter == 1 or board[r][c] == 1 and counter > 3:  # die for lonelyness or dir from densty
        board[r][c] = 0
        # print(board)
        return board

    # situation 3
    elif board[r][c] == 0 and counter == 3:  # was dead and have three nirghboors make him alive
        board[r][c] = 1
        # print(board)
        return board

    # situation 4
    else:
        # print(board)
        return board




#
#this func is just helped me to run my project and to do an easy tests
# the random board helped me fund the difficult cases that the code can have difficulte
if __name__ == '__main__':
    board = Board()
    # print(board.board)
    # print(board.random_board_size())
    # print(board.random_the_board_inside())
    checker(board.random_the_board_inside().board)

    # matrix to check the checker helper func for the middle cell
    # matrix1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]  # die lonley
    # matrix2 = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]  # die densty
    # matrix3 = [[0, 0, 0], [0, 1, 0], [0, 1, 1]]  # stay the same
    # matrix4 = [[0, 0, 1], [1, 0, 0], [1, 0, 0]]  # make him alive
    # matrix5 = [[1,1,1],[1,1,1],[1,1,1]]
    # checker(matrix3)
    # checker(matrix5)


    # test checker helper
    # print(checker_helper(1,1,matrix1))
    # print(checker_helper(1, 1, matrix2))
    # print(checker_helper(1, 1, matrix3))
    # print(checker_helper(1, 1, matrix4))

    # print(checker(matrix1))
    # print(checker(matrix2))
    # print(checker(matrix3))
    # print(checker(matrix4))
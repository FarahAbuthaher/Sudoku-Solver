def Sudoku_solve(bo):
    emty_sqr= find_empty(bo) # locates empty squares
    if not emty_sqr: # stops when finds a solution
        return True
    else:
        row, col = emty_sqr

    for i in range(1, 10):  # try in the square from 1 to 9
        if check_number(bo, (row, col), i):
            bo[row][col] = i

            if Sudoku_solve(bo): # keeps going until there are no empty squares
                return True
            bo[row][col] = 0 # recursive solution to backtrack and find the best fit in the squares
    return False  # returns false when all numbers from 1 to 9 can't fill the square


def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

def check_number(bo, pos, num):
    # Need to check if pos is valid in row, column and box
    # start with row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check for column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check in box
    x = pos[1] // 3 # this gives the box you're in an ID number
    y = pos[0] // 3
    for i in range(y*3, y*3+3):
        for j in range(x*3, x*3+3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print('|',end=' ')
            if j == 8:
                print(str(bo[i][j])+" |")
            else:
                print(str(bo[i][j]),end=' ')
    print("-------------------------")
board = [
    [9,3,4,0,0,0,6,0,0],
    [2,0,0,0,6,0,0,9,4],
    [0,0,0,4,2,0,5,0,0],
    [0,7,3,2,0,5,4,0,0],
    [8,0,0,1,0,0,0,0,0],
    [5,0,2,0,0,8,0,7,0],
    [0,0,1,0,0,6,0,0,0],
    [6,0,0,7,5,2,1,0,0],
    [0,0,7,0,1,0,0,0,0]
]
board2 = [
    [0,0,0,1,0,0,7,4,0],
    [0,5,0,0,9,0,0,3,2],
    [0,0,6,7,0,0,9,0,0],
    [4,0,0,8,0,0,0,0,0],
    [0,2,0,0,0,0,0,1,0],
    [0,0,0,0,0,9,0,0,5],
    [0,0,4,0,0,7,3,0,0],
    [7,3,0,0,2,0,0,6,0],
    [0,6,5,0,0,4,0,0,0]
]
print_board(board)
Sudoku_solve(board)
print("<><><><><><><><><><><><><><><><><><><><><>")
print_board(board)
print("<><><><><><><><><><><><><><><><><><><><><>")
print_board(board2)
Sudoku_solve(board2)
print("<><><><><><><><><><><><><><><><><><><><><>")
print_board(board2)
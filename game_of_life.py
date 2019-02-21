 #  1.  Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#  2.  Any live cell with two or three live neighbors lives on to the next generation.
#  3.  Any live cell with more than three live neighbors dies, as if by overpopulation.
#  4.  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
import time

def board(size):  # Remove unnecessary functions and tests 
    """Create a 3*3 matrix """
    board=[[1,0,0],[0,0,1],[0,1,1]]
    return board

def cell_alive_check(cell): # Name these functions as a question (is_alive)
    return cell == 1




def all_neighbour_check(board):
    result =[[0,0,0],[0,0,0],[0,0,0]]
    for row in range(3): # Don't *hardcode* for a fixed size. 
        for col in range(3): # Use len(board) for columns 
                             # and len(board[0]) for rows
            if row ==0 and col == 0:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count += 1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                if cell_alive_check(board[row+1][col+1]):
                    count +=1
                result[0][0]= count
            if row ==0 and col ==1:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count += 1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                if cell_alive_check(board[row+1][col+1]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                if cell_alive_check(board[row][col-1]):
                    count +=1
                result[0][1]= count

            if row==0 and col==2:
                count =0
                if cell_alive_check(board[row+1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                if cell_alive_check(board[row][col-1]):
                    count +=1
                result[0][2]= count
            if row==1 and col ==0:
                count=0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col+1]):
                    count += 1
                if cell_alive_check(board[row+1][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                result[1][0]= count

            if row ==1 and col ==1:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row][col-1]):
                    count += 1
                if cell_alive_check(board[row+1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col+1]):
                    count += 1
                if cell_alive_check(board[row-1][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                result[1][1]= count

            if row ==1 and col ==2 :
                count =0
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                if cell_alive_check(board[row+1][col-1]):
                    count += 1
                if cell_alive_check(board[row][col-1]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row+1][col]):
                    count += 1
                result[1][2]= count

            if row == 2 and col == 0:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col+1]):
                    count +=1
                result[2][0]= count

            if row ==2 and col == 1:
                count =0
                if cell_alive_check(board[row][col+1]):
                    count +=1
                if cell_alive_check(board[row][col-1]):
                    count += 1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col+1]):
                    count +=1
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                result[2][1] = count

            if row == 2 and col ==2:
                count =0
                if cell_alive_check(board[row][col-1]):
                    count += 1
                if cell_alive_check(board[row-1][col]):
                    count +=1
                if cell_alive_check(board[row-1][col-1]):
                    count +=1
                result[2][2]= count
        
    return result

def set_rule(board, neighbour):
    for row in range(3):
        for col in range(3):
            if cell_alive_check(board[row][col]):
                if neighbour[row][col] < 2:
                    board[row][col] = 0
                if neighbour[row][col] == 2 or neighbour[row][col] == 3:
                    board[row][col] = 1
                if neighbour[row][col] > 3:
                    board[row][col] = 0
            else:
                if neighbour[row][col] == 3:
                    board[row][col] = 1

    return board

def display(board):
    for row in range(3):
        for col in range(3):
            if cell_alive_check(board[row][col]):
                print(" 1 ", end=' ')
            else:
                print(" 0 ", end=' ')
        print("\n")

def main(board):
    display(board)
    a=  set_rule(board,all_neighbour_check(board))
    return a 
    
    
if __name__ == "__main__":
    board = [[1,0,0],[0,0,1],[0,1,1]]
    for i in range(10):
        print("\n{} Generation".format(i))
        time.sleep(1)
        main(board)
        

        

"""
a solution to the 8 queens problem generalized to n queens on a board of length n

clearly, for 1<n<4 no solutions exist; these n will be disregarded.

numpy was used for its arrays and their methods, e.g. for diagonals in valid().
2d numpy arrays are also printed as matrices, and thus there is no need for a function,
which prints the board. 

program overview
    - valid(A:array, r:int, c:int) -> bool: checks if placing a queen in a given position (r,c) is valid
    - solve(A:array, r:int)) -> bool: backtracking
    - n_queens(n:int) -> initializes the n by n array, then produces a solution with solve for row 0

literature: 
    - https://en.wikipedia.org/wiki/Eight_queens_puzzle
    - https://leetcode.com/problems/n-queens/solutions/7623161/backtracking-solution-for-n-queens-with-bgypa
    - https://www.geeksforgeeks.org/dsa/8-queen-problem/
"""
import numpy as np

def valid(A:list, r:int, c:int) -> bool:
    n = len(A)
    offset = c - r
    flip_offset = ((n - 1) - r) - c
    # check space controlled by queen in (r,c), if the sum != 0 there is at least one queen in this space
    if sum(A[r, :]) + sum(A[:, c]) + sum(A.diagonal(offset)) + sum(np.fliplr(A).diagonal(flip_offset)) != 0:
        return False
    else: 
        return True

def solve(A:list, r:int) -> list:
    n=len(A)
    if n == r:    # terminating condition: we are past last row and thus all queens have been placed
        return True
    for i in range(n):  # iterates through columns 
        if valid(A,r,i) == True:  
            A[r][i] = 1   # place queen if position is valid
            if solve(A,r+1) == True:  # checks if next row has solutions
                return True
            A[r][i] = 0   # backtracking if r+1 has no solutions
    return False

def nqueens(n:int) -> list:
    if n < 4:
        raise ValueError('meow please pick n>3')
    A = np.array([[0 for _ in range(n)] for _ in range(n)]) #initialize n by n board
    solve(A,0) # starts solving at row 0
    print(A)
    return A

nqueens(8)
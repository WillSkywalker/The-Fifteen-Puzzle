#!usr/bin/env python

import poc_fifteen

T_ONE = [[10, 2, 3, 7],
         [8, 5, 6, 9],
         [4, 1, 0, 11],
         [12, 13, 14, 15]]

T_TWO = [[7, 4, 5, 3, 8],
         [1, 2, 10, 11, 6],
         [9, 0, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]

T_THREE = [[20, 4, 5, 21, 8],
         [1, 2, 10, 11, 6],
         [9, 3, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [7, 0, 22, 23, 24]]

T_FOUR = [[4, 3, 2],
          [1, 0, 5], 
          [6, 7, 8]]

def test_lower():
    t1 = poc_fifteen.Puzzle(4, 4, T_ONE)
    # print t1.lower_row_invariant(2,2) # true
    t2 = poc_fifteen.Puzzle(5, 5, T_TWO)
    t3 = poc_fifteen.Puzzle(5, 5, T_THREE)
    print t1
    print t1.solve_interior_tile(2, 2)
    print t1
    print '==================='
    print t2
    print t2.solve_interior_tile(2, 1)
    print t2
    print t2.solve_col0_tile(2)
    print t2
    print '==================='
    print t3
    print t3.solve_interior_tile(4, 1)
    print t3
    print t3.solve_col0_tile(4)
    print t3
    # print t2.lower_row_invariant(1,2) # false
    # print t2.lower_row_invariant(2,1) # true
    # print t2.lower_row_invariant(3,4) # false


def test_upper():
    t1 = poc_fifteen.Puzzle(3, 3, T_FOUR)
    print t1.row1_invariant(1)
    

if __name__ == '__main__':
    test_upper()
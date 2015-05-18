#!usr/bin/env python

import poc_fifteen, poc_fifteen_gui

T_ONE = [[6, 2, 3, 7],
         [4, 5, 1, 0],
         [8, 9, 10, 11],
         [12, 13, 14, 15]]

T_TWO = [[8, 4, 5, 3, 7],
         [1, 2, 9, 6, 0],
         [10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]

T_THREE = [[7, 4, 5, 10, 8],
         [1, 2, 9, 6, 3],
         [0, 11, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]

T_FOUR = [[8, 7, 6], 
          [5, 4, 3], 
          [2, 1, 0]]

T_FIVE = [[7, 6, 5, 0, 4], 
          [2, 1, 3, 8, 9], 
          [10, 11, 12, 13, 14], 
          [15, 16, 17, 18, 19]]

T_T = [[4, 1, 0], 
       [2, 3, 5], 
       [6, 7, 8]]

def test_one():
    t1 = poc_fifteen.Puzzle(3, 3, T_T)
    # print t1.lower_row_invariant(2,2) # true
    t2 = poc_fifteen.Puzzle(5, 5, T_TWO)
    t3 = poc_fifteen.Puzzle(5, 5, T_THREE)
    t4 = poc_fifteen.Puzzle(4, 5, T_FIVE)
    print t1
    print t1.solve_row0_tile(2)
    print t1
    # print t1.solve_row1_tile(2)
    # print t1
    print '==================='
    print t2
    print t2.solve_row1_tile(4)
    print t2
    # print t2.solve_row1_tile(3)
    # print t2
    # print t2.solve_row1_tile(2)
    # print t2
    print '==================='
    print t3
    print t3.solve_col0_tile(2)
    print t3
    # print t3.solve_row1_tile(3)
    # print t3
    print '==================='
    print t4
    print t4.solve_row0_tile(3)
    print t4
    # print t2.lower_row_invariant(1,2) # false
    # print t2.lower_row_invariant(2,1) # true
    # print t2.lower_row_invariant(3,4) # false


def test_two():
    t1 = poc_fifteen.Puzzle(3, 3, T_FOUR)
    print t1.row1_invariant(1)
    

if __name__ == '__main__':
    test_one()
    # poc_fifteen_gui.FifteenGUI(poc_fifteen.Puzzle(2, 3, T_T))

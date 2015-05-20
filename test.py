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

T_THREE = [[7, 4, 6, 10, 8],
         [1, 2, 9, 5, 3],
         [0, 11, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]

T_FOUR = [[8, 7, 6], 
          [5, 4, 3], 
          [2, 1, 0]]

T_FIVE = [[5, 17, 6, 9, 7],
          [11, 1, 16, 3, 4],
          [20, 22, 15, 2, 12],
          [21, 10, 13, 8, 18],
          [24, 14, 23, 19, 0]]

T_SIX = [[5, 7, 1, 3, 4],
         [6, 2, 0, 8, 9],
         [10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]


T_T = [[5, 1, 3, 8, 4],
       [6, 16, 9, 13, 7],
       [10, 21, 2, 12, 18],
       [15, 22, 23, 19, 14],
       [20, 17, 11, 24, 0]]

def test_one():
    t1 = poc_fifteen.Puzzle(4, 4, T_ONE)
    # print t1.lower_row_invariant(2,2) # true
    t2 = poc_fifteen.Puzzle(5, 5, T_TWO)
    t_stop = poc_fifteen.Puzzle(5, 5, T_FIVE)
    t3 = poc_fifteen.Puzzle(5, 5, T_SIX)
    t4 = poc_fifteen.Puzzle(5, 5, T_T)
    print t1
    print t1.solve_row1_tile(3)
    print t1
    # print t1.solve_row1_tile(2)
    # print t1
    print 'ONE==================='
    print t_stop
    print t_stop.solve_interior_tile(4, 4)
    print t_stop
    print t_stop.solve_interior_tile(4, 3)
    print t_stop
    print t_stop.solve_interior_tile(4, 2)
    print t_stop
    print t_stop.solve_interior_tile(4, 1)
    print t_stop
    print t_stop.solve_col0_tile(4)
    print t_stop
    print t_stop.solve_interior_tile(3, 4)
    print t_stop
    print t_stop.solve_interior_tile(3, 3)
    print t_stop
    print t_stop.solve_interior_tile(3, 2)
    print t_stop
    print t_stop.solve_interior_tile(3, 1)
    print t_stop
    print t_stop.solve_col0_tile(3)
    print t_stop
    print t_stop.solve_interior_tile(2, 4)
    print t_stop
    print t_stop.solve_interior_tile(2, 3)
    print t_stop
    print t_stop.solve_interior_tile(2, 2)
    print t_stop
    print t_stop.solve_interior_tile(2, 1)
    print t_stop
    print t_stop.solve_col0_tile(2)
    print t_stop
    print t_stop.solve_row1_tile(4)
    print t_stop
    print t_stop.solve_row0_tile(4)
    print t_stop
    print t_stop.solve_row1_tile(3)
    print t_stop
    print t_stop.solve_row0_tile(3)
    print t_stop
    print t_stop.solve_row1_tile(2)
    print t_stop
    print t_stop.solve_row0_tile(2)
    print t_stop
    # print t2.solve_row1_tile(3)
    # print t2
    # print t2.solve_row1_tile(2)
    # print t2
    print 'TWO==================='
    print t3
    print t3.solve_row1_tile(2)
    print t3
    print t3.solve_row0_tile(2)
    # t3.solve_row1_tile(4)
    # t3.solve_row0_tile(4)
    # t3.solve_row1_tile(3)
    # t3.solve_row0_tile(3)
    # t3.solve_row1_tile(2)
    # t3.solve_row0_tile(2)
    # t3.solve_row1_tile(1)
    # t3.solve_row0_tile(1)
    print t3
    print t3.solve_2x2()
    print t3


    # print t3.solve_row1_tile(3)
    # print t3
    print 'TRE==================='
    print t4
    print len(t4.solve_puzzle())
    print t4
    # print t2.lower_row_invariant(1,2) # false
    # print t2.lower_row_invariant(2,1) # true
    # print t2.lower_row_invariant(3,4) # false


def test_two():
    puz = poc_fifteen.Puzzle(4, 4, [[15, 11, 8, 12], [14, 10, 9, 13], [2, 6, 1, 4], [3, 7, 5, 0]])
    sol = puz.solve_puzzle()
    print sol
    print len(sol)    

if __name__ == '__main__':
    test_one()
    # poc_fifteen_gui.FifteenGUI(poc_fifteen.Puzzle(2, 3, T_T))

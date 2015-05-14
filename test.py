#!usr/bin/env python

import poc_fifteen

T_ONE = [[10, 2, 3, 7],
         [8, 5, 6, 9],
         [4, 1, 0, 11],
         [12, 13, 14, 15]]

T_TWO = [[7, 4, 5, 11, 8],
         [1, 2, 10, 3, 6],
         [9, 0, 12, 13, 14],
         [15, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]

def test():
    t1 = poc_fifteen.Puzzle(4, 4, T_ONE)
    # print t1.lower_row_invariant(2,2) # true
    t2 = poc_fifteen.Puzzle(5, 5, T_TWO)
    print t1
    print t1.solve_interior_tile(2, 2)
    print t1
    print '==================='
    print t2
    print t2.solve_interior_tile(2, 1)
    print t2
    # print t2.lower_row_invariant(1,2) # false
    # print t2.lower_row_invariant(2,1) # true
    # print t2.lower_row_invariant(3,4) # false

if __name__ == '__main__':
    test()
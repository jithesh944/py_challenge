"""
Rotating Matrix:
Given an array of array as below, rotate the array 90 degrees.
Refer to sample input and output for reference:
Input:
[
[1,2,3]
[4,5,6]
[7,8,9]
]
Output:
[
[7,4,1]
[8,5,2]
[9,6,3]
]
"""

from typing import NewType


def twoD_rotation(TwoD,rotation):
    row = 0
    print("Originl array")
    for r in TwoD:
        row += 1
        col = 0
        for c in r:
            col += 1
            print(c,end=' ')
        print()
    print(f'row = {row}, column = {col}')
    
    for c in range(col):
        for r in range(row,0,-1):
            # print(c,row-r,'\n')
            print(TwoD[r-1][c],end=' ')
        print()

    # for i in range(rotation):
    #     new_TwoD= [([0] * col)]* row
    #     # new_TwoD =list(list())
    #     print(new_TwoD)
    #     print('array rotation-',i+1)
    #     # c = 0
    #     # r = row
    #     for c in range(col):
    #         for r in range(row-1,0,-1):
    #             # print(c,row-r,'\n')
    #             print(TwoD[r][c],end=' ')
    #             # new_TwoD[c][(row-1)-r] = (TwoD[r][c])
    #             # print(new_TwoD[c][row-r],end=' ')
    #             # print(new_TwoD[r])
    #         print()
    #         # new_TwoD.append(new_TwoD[r])
    #         # print('TwoD',new_TwoD)

    

if __name__ == '__main__':
    TwoD = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    rotation = int(input("Enter the no of rotations of 90 degree "))
    twoD_rotation(TwoD,rotation)
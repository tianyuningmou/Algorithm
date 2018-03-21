# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: circle_matrix.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/21 上午9:51

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/21 上午9:51
"""


# 回旋矩阵的生成
def circle_matrix(n):
    a = [[0 for col in range(n)] for row in range(n)]
    base = 0
    for k in range(0, n//2):
        for i in range(k, n-k):
            base += 1
            a[k][i] = base
        for j in range(k+1, n-1-k):
            base += 1
            a[j][n-1-k] = base
        for i in range(n-1-k, k, -1):
            base += 1
            a[n-1-k][i] = base
        for j in range(n-1-k, k, -1):
            base += 1
            a[j][k] = base
    if(n%2 == 1):
        base += 1
        a[(n-1)//2][(n-1)//2] = base
    for i in range(0, n):
        for j in range(0, n):
            print('{}'.format(a[i][j]), end='   ')
        print('\n')


if __name__ == '__main__':
    print('请输入要生成回旋矩阵的维数：')
    num = input()
    print('\n')
    circle_matrix(int(num))

# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: world_cup.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/5/29 上午10:11

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/5/29 上午10:11
"""

import sys

total_list = list()
for i in range(16):
    line = sys.stdin.readline().strip()
    values = list(map(float, line.split()))
    total_list.append(values)
# 首先计算每支队伍进入八强的概率
"""
0   1 A组第一
1   2 B组第二
2   3 C组第一
3   4 D组第二
4   5 E组第一
5   6 F组第二
6   7 G组第一
7   8 H组第二
8   9 B组第一
9   10 A组第二
10  11 D组第一
11  12 C组第二
12  13 F组第一
13  14 E组第二
14  15 H组第一
15  16 G组第二
"""
eighth = [total_list[0][1], total_list[1][0],        # 胜者1
          total_list[2][3], total_list[3][2],        # 胜者3
          total_list[4][5], total_list[5][4],        # 胜者5
          total_list[6][7], total_list[7][6],        # 胜者7
          total_list[8][9], total_list[9][8],        # 胜者2
          total_list[10][11], total_list[11][10],    # 胜者4
          total_list[12][13], total_list[13][12],    # 胜者6
          total_list[14][15], total_list[15][14]]    # 胜者8
quarter = [0 for i in range(16)]
quarter[0] = total_list[0][1] * (total_list[2][3] * total_list[0][2] + total_list[3][2] * total_list[0][3])
quarter[1] = total_list[1][0] * (total_list[2][3] * total_list[1][2] + total_list[3][2] * total_list[1][3])
quarter[2] = total_list[2][3] * (total_list[0][1] * total_list[2][0] + total_list[1][0] * total_list[2][1])
quarter[3] = total_list[3][2] * (total_list[0][1] * total_list[3][0] + total_list[1][0] * total_list[3][1])
quarter[4] = total_list[4][5] * (total_list[6][7] * total_list[4][6] + total_list[7][6] * total_list[4][7])
quarter[5] = total_list[5][4] * (total_list[6][7] * total_list[5][6] + total_list[7][6] * total_list[5][7])
quarter[6] = total_list[6][7] * (total_list[4][5] * total_list[6][4] + total_list[5][4] * total_list[6][5])
quarter[7] = total_list[7][6] * (total_list[4][5] * total_list[7][4] + total_list[5][4] * total_list[7][5])
quarter[8] = total_list[8][9] * (total_list[10][11] * total_list[8][10] + total_list[11][10] * total_list[8][11])
quarter[9] = total_list[9][8] * (total_list[10][11] * total_list[9][10] + total_list[11][10] * total_list[9][11])
quarter[10] = total_list[10][11] * (total_list[8][9] * total_list[10][8] + total_list[9][8] * total_list[10][9])
quarter[11] = total_list[11][10] * (total_list[8][9] * total_list[11][8] + total_list[9][8] * total_list[11][9])
quarter[12] = total_list[12][13] * (total_list[14][15] * total_list[12][14] + total_list[15][14] * total_list[12][15])
quarter[13] = total_list[13][12] * (total_list[14][15] * total_list[13][14] + total_list[15][14] * total_list[13][15])
quarter[14] = total_list[14][15] * (total_list[12][13] * total_list[14][12] + total_list[13][12] * total_list[14][13])
quarter[15] = total_list[15][14] * (total_list[12][13] * total_list[15][12] + total_list[13][12] * total_list[15][13])

half = [0 for i in range(16)]
half[0] = quarter[0] * (quarter[4] * total_list[0][4] + quarter[5] * total_list[0][5] + quarter[6] * total_list[0][6] + quarter[7] * total_list[0][7])
half[1] = quarter[1] * (quarter[4] * total_list[1][4] + quarter[5] * total_list[1][5] + quarter[6] * total_list[1][6] + quarter[7] * total_list[1][7])
half[2] = quarter[2] * (quarter[4] * total_list[2][4] + quarter[5] * total_list[2][5] + quarter[6] * total_list[2][6] + quarter[7] * total_list[2][7])
half[3] = quarter[3] * (quarter[4] * total_list[3][4] + quarter[5] * total_list[3][5] + quarter[6] * total_list[3][6] + quarter[7] * total_list[3][7])
half[4] = quarter[4] * (quarter[0] * total_list[4][0] + quarter[1] * total_list[4][1] + quarter[2] * total_list[4][2] + quarter[3] * total_list[4][3])
half[5] = quarter[5] * (quarter[0] * total_list[5][0] + quarter[1] * total_list[5][1] + quarter[2] * total_list[5][2] + quarter[3] * total_list[5][3])
half[6] = quarter[6] * (quarter[0] * total_list[6][0] + quarter[1] * total_list[6][1] + quarter[2] * total_list[6][2] + quarter[3] * total_list[6][3])
half[7] = quarter[7] * (quarter[0] * total_list[7][0] + quarter[1] * total_list[7][1] + quarter[2] * total_list[7][2] + quarter[3] * total_list[7][3])
half[8] = quarter[8] * (quarter[12] * total_list[8][12] + quarter[13] * total_list[8][13] + quarter[14] * total_list[8][14] + quarter[15] * total_list[8][15])
half[9] = quarter[9] * (quarter[12] * total_list[9][12] + quarter[13] * total_list[9][13] + quarter[14] * total_list[9][14] + quarter[15] * total_list[9][15])
half[10] = quarter[10] * (quarter[12] * total_list[10][12] + quarter[13] * total_list[10][13] + quarter[14] * total_list[10][14] + quarter[15] * total_list[10][15])
half[11] = quarter[11] * (quarter[12] * total_list[11][12] + quarter[13] * total_list[11][13] + quarter[14] * total_list[11][14] + quarter[15] * total_list[11][15])
half[12] = quarter[12] * (quarter[8] * total_list[12][8] + quarter[9] * total_list[12][9] + quarter[10] * total_list[12][10] + quarter[11] * total_list[12][11])
half[13] = quarter[13] * (quarter[8] * total_list[13][8] + quarter[9] * total_list[13][9] + quarter[10] * total_list[13][10] + quarter[11] * total_list[13][11])
half[14] = quarter[14] * (quarter[8] * total_list[14][8] + quarter[9] * total_list[14][9] + quarter[10] * total_list[14][10] + quarter[11] * total_list[14][11])
half[15] = quarter[15] * (quarter[8] * total_list[15][8] + quarter[9] * total_list[15][9] + quarter[10] * total_list[15][10] + quarter[11] * total_list[15][11])

winner = [0 for i in range(16)]
winner[0] = half[0] * (half[8] * total_list[0][8] + half[9] * total_list[0][9] + half[10] * total_list[0][10] + half[11] * total_list[0][11] +
                       half[12] * total_list[0][12] + half[13] * total_list[0][13] + half[14] * total_list[0][14] + half[15] * total_list[0][15])
winner[1] = half[1] * (half[8] * total_list[1][8] + half[9] * total_list[1][9] + half[10] * total_list[1][10] + half[11] * total_list[1][11] +
                       half[12] * total_list[1][12] + half[13] * total_list[1][13] + half[14] * total_list[1][14] + half[15] * total_list[1][15])
winner[2] = half[2] * (half[8] * total_list[2][8] + half[9] * total_list[2][9] + half[10] * total_list[2][10] + half[11] * total_list[2][11] +
                       half[12] * total_list[2][12] + half[13] * total_list[2][13] + half[14] * total_list[2][14] + half[15] * total_list[2][15])
winner[3] = half[3] * (half[8] * total_list[3][8] + half[9] * total_list[3][9] + half[10] * total_list[3][10] + half[11] * total_list[3][11] +
                       half[12] * total_list[3][12] + half[13] * total_list[3][13] + half[14] * total_list[3][14] + half[15] * total_list[3][15])
winner[4] = half[4] * (half[8] * total_list[0][8] + half[9] * total_list[0][9] + half[10] * total_list[0][10] + half[11] * total_list[0][11] +
                       half[12] * total_list[0][12] + half[13] * total_list[0][13] + half[14] * total_list[0][14] + half[15] * total_list[0][15])
winner[5] = half[5] * (half[8] * total_list[5][8] + half[9] * total_list[5][9] + half[10] * total_list[5][10] + half[11] * total_list[5][11] +
                       half[12] * total_list[5][12] + half[13] * total_list[5][13] + half[14] * total_list[5][14] + half[15] * total_list[5][15])
winner[6] = half[6] * (half[8] * total_list[6][8] + half[9] * total_list[6][9] + half[10] * total_list[6][10] + half[11] * total_list[6][11] +
                       half[12] * total_list[6][12] + half[13] * total_list[6][13] + half[14] * total_list[6][14] + half[15] * total_list[6][15])
winner[7] = half[7] * (half[8] * total_list[7][8] + half[9] * total_list[7][9] + half[10] * total_list[7][10] + half[11] * total_list[7][11] +
                       half[12] * total_list[7][12] + half[13] * total_list[7][13] + half[14] * total_list[7][14] + half[15] * total_list[7][15])
winner[8] = half[8] * (half[0] * total_list[8][0] + half[1] * total_list[8][1] + half[2] * total_list[8][2] + half[3] * total_list[8][3] +
                       half[4] * total_list[8][4] + half[5] * total_list[8][5] + half[6] * total_list[8][6] + half[7] * total_list[8][7])
winner[9] = half[9] * (half[0] * total_list[9][0] + half[1] * total_list[9][1] + half[2] * total_list[9][2] + half[3] * total_list[9][3] +
                       half[4] * total_list[9][4] + half[5] * total_list[9][5] + half[6] * total_list[9][6] + half[7] * total_list[9][7])
winner[10] = half[10] * (half[0] * total_list[10][0] + half[1] * total_list[10][1] + half[2] * total_list[10][2] + half[3] * total_list[10][3] +
                         half[4] * total_list[10][4] + half[5] * total_list[10][5] + half[6] * total_list[10][6] + half[7] * total_list[10][7])
winner[11] = half[11] * (half[0] * total_list[11][0] + half[1] * total_list[11][1] + half[2] * total_list[11][2] + half[3] * total_list[11][3] +
                         half[4] * total_list[11][4] + half[5] * total_list[11][5] + half[6] * total_list[11][6] + half[7] * total_list[11][7])
winner[12] = half[12] * (half[0] * total_list[12][0] + half[1] * total_list[12][1] + half[2] * total_list[12][2] + half[3] * total_list[12][3] +
                         half[4] * total_list[12][4] + half[5] * total_list[12][5] + half[6] * total_list[12][6] + half[7] * total_list[12][7])
winner[13] = half[13] * (half[0] * total_list[13][0] + half[1] * total_list[13][1] + half[2] * total_list[13][2] + half[3] * total_list[13][3] +
                         half[4] * total_list[13][4] + half[5] * total_list[13][5] + half[6] * total_list[13][6] + half[7] * total_list[13][7])
winner[14] = half[14] * (half[0] * total_list[14][0] + half[1] * total_list[14][1] + half[2] * total_list[14][2] + half[3] * total_list[14][3] +
                         half[4] * total_list[14][4] + half[5] * total_list[14][5] + half[6] * total_list[14][6] + half[7] * total_list[14][7])
winner[15] = half[15] * (half[0] * total_list[15][0] + half[1] * total_list[15][1] + half[2] * total_list[15][2] + half[3] * total_list[15][3] +
                         half[4] * total_list[15][4] + half[5] * total_list[15][5] + half[6] * total_list[15][6] + half[7] * total_list[15][7])
print('%.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f %.10f' % (winner[0], winner[1],
      winner[2], winner[3], winner[4], winner[5], winner[6], winner[7], winner[8], winner[9], winner[10], winner[11], winner[12], winner[13], winner[14], winner[15]))

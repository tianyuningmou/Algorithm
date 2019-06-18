# -*- coding: utf-8 -*-

"""
Copyright () 2019

All rights reserved

FILE: python_bisect.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2019-06-18 17:42

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2019-06-18 17:42
"""

import bisect
import random

random.seed(1)
l = []
for i in range(1, 15):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print(r, position, l)

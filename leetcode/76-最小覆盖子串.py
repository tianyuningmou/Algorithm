# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 76-最小覆盖子串.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/9/8 4:47 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/9/8 4:47 下午
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length_s, length_t = len(s), len(t)
        left, right = 0, -1
        ans, n_t = '', ''
        res = length_s
        while right < length_s:
            right += 1
            # 不包含的时候移动右边界
            if not self.check(t, n_t) and right < length_s:
                n_t += s[right]
                while self.check(t, n_t):
                    if right - left + 1 <= res:
                        ans = s[left: right + 1]
                    n_t = n_t[1:]
                    left += 1
        return ans

    def check(self, t, n_t):
        pass


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))

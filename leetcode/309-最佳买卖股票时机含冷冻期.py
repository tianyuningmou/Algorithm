# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: 309-最佳买卖股票时机含冷冻期.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/4/22 2:18 下午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/4/22 2:18 下午
"""

"""
309. 最佳买卖股票时机含冷冻期
我们用 f[i] 表示第 i 天结束之后的「累计最大收益」。根据题目描述，由于我们最多只能同时买入（持有）一支股票，并且卖出股票后有冷冻期的限制，因此我们会有三种不同的状态：
    我们目前持有一支股票，对应的「累计最大收益」记为 f[i][0]；
    我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 f[i][1]；
    我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]。

这里的「处于冷冻期」指的是在第 i 天结束之后的状态。也就是说：如果第 i 天结束之后处于冷冻期，那么第 i+1 天无法买入股票。

对于 f[i][0]，我们目前持有的这一支股票可以是在第 i-1 天就已经持有的，对应的状态为 f[i-1][0]；
或者是第 i 天买入的，那么第 i-1天就不能持有股票并且不处于冷冻期中，对应的状态为 f[i-1][2] 加上买入股票的负收益 prices[i]。因此状态转移方程为：
    f[i][0]=max(f[i−1][0], f[i−1][2]−prices[i])

对于 f[i][1]，我们在第 i 天结束之后处于冷冻期的原因是在当天卖出了股票，那么说明在第 i-1 天时我们必须持有一支股票，对应的状态为 f[i-1][0] 加上卖出股票的正收益 prices[i]。因此状态转移方程为：
    f[i][1]=f[i−1][0]+prices[i]

对于 f[i][2]，我们在第 i 天结束之后不持有任何股票并且不处于冷冻期，说明当天没有进行任何操作，即第 i-1 天时不持有任何股票：
如果处于冷冻期，对应的状态为 f[i−1][1]；如果不处于冷冻期，对应的状态为 f[i−1][2]。因此状态转移方程为：
    f[i][2]=max(f[i−1][1],f[i−1][2])

这样我们就得到了所有的状态转移方程。如果一共有 nn 天，那么最终的答案即为：
    max(f[n−1][0],f[n−1][1],f[n−1][2])

注意到如果在最后一天（第 n-1n−1 天）结束之后，手上仍然持有股票，那么显然是没有任何意义的。因此更加精确地，最终的答案实际上是 f[n-1][1]f[n−1][1] 和 f[n-1][2]f[n−1][2] 中的较大值，即：
    max(f[n−1][1],f[n−1][2])

我们可以将第 0 天的情况作为动态规划中的边界条件：
    f[0][0] = −prices[0]
    f[0][1] = 0
    f[0][2] = 0
在第 0 天时，如果持有股票，那么只能是在第 0 天买入的，对应负收益 −prices[0]；
如果不持有股票，那么收益为零。注意到第 0 天实际上是不存在处于冷冻期的情况的，但我们仍然可以将对应的状态 f[0][1] 置为零。
这样我们就可以从第 1 天开始，根据上面的状态转移方程进行进行动态规划，直到计算出第 n-1 天的结果。
"""


class Solution(object):
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            new0 = max(f0, f2 - prices[i])
            new1 = f0 + prices[i]
            new2 = max(f1, f2)
            f0, f1, f2 = new0, new1, new2
        return max(f1, f2)

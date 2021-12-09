# -*- coding: utf-8 -*-

"""
Copyright () 2019

All rights reserved

FILE: duration_calculate.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2019-06-23 15:49

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2019-06-23 15:49
"""


import datetime
from math import *


class DurationCalculate(object):
    """
    包含计算多个时间段的算法，采用双指针，时间复杂度O(n),空间复杂度O(1)
    """

    @classmethod
    def duration_calculate_to_seconds(cls, durations, date_time):
        """
        计算多个时间段之和，重叠部分不计算，并转换成秒
        :param durations:
            example: [[t1, t2], [t3, t4], ...]
        :param date_time: 截止时间，可不填
        :return:
        """
        return cls.duration_calculate(durations, date_time).seconds

    @classmethod
    def duration_calculate_to_minutes(cls, durations, date_time, *args):
        """
        计算多个时间段之和，重叠部分不计算，并转换成分钟
        :param durations:
            example: [[t1, t2], [t3, t4], ...]
        :param date_time: 截止时间，可不填
        :param args: 填写精确类型--> floor, round, ceil
        :return:
        """
        if args or args[0] == 'ceil':
            return ceil(cls.duration_calculate(durations, date_time).seconds / 60.0)
        elif args[0] == 'round':
            return round(cls.duration_calculate(durations, date_time).seconds / 60.0)
        elif args[0] == 'floor':
            return floor(cls.duration_calculate(durations, date_time).seconds / 60.0)
        else:
            return "请输入['ceil'] or ['round'] or ['floor'], 或者不填"

    @classmethod
    def duration_calculate_to_hours(cls, durations, date_time, *args):
        """
        计算多个时间段之和，重叠部分不计算，并转换成小时
        :param durations:
            example: [[t1, t2], [t3, t4], ...]
        :param date_time: 截止时间，可不填
        :param args: 填写精确类型--> floor, round, ceil
        :return:
        """
        if args or args[0] == 'ceil':
            return ceil(cls.duration_calculate(durations, date_time).seconds / 3600.0)
        elif args[0] == 'round':
            return round(cls.duration_calculate(durations, date_time).seconds / 3600.0)
        elif args[0] == 'floor':
            return floor(cls.duration_calculate(durations, date_time).seconds / 3600.0)
        else:
            return "请输入['ceil'] or ['round'] or ['floor'], 或者不填"

    @classmethod
    def duration_calculate_to_days(cls, durations, date_time):
        """
        计算多个时间段之和，重叠部分不计算，并转换成天
        :param durations:
            example: [[t1, t2], [t3, t4], ...]
        :param date_time: 截止时间，可不填
        :return:
        """
        return cls.duration_calculate(durations, date_time).days

    @classmethod
    def duration_calculate_to_months(cls, durations, date_time, *args):
        """
        计算多个时间段之和，重叠部分不计算，并转换成月
        :param durations:
            example: [[t1, t2], [t3, t4], ...]
        :param date_time: 截止时间，可不填
        :param args: 填写精确类型--> floor, round, ceil
        :return:
        """
        if args or args[0] == 'ceil':
            return ceil(cls.duration_calculate_to_days(durations, date_time) / 30.0)
        elif args[0] == 'round':
            return round(cls.duration_calculate_to_days(durations, date_time) / 30.0)
        elif args[0] == 'floor':
            return floor(cls.duration_calculate_to_days(durations, date_time) / 30.0)
        else:
            return "请输入['ceil'] or ['round'] or ['floor'], 或者不填"

    @classmethod
    def duration_calculate(cls, durations, date_time=None):
        """
        计算时间段差值的基础算法
        :param durations:
            example: [[t1, t2], [t3, t4], ...]
        :param date_time: 截止时间，可不填
        :return:
        """
        if len(durations) == 1:
            return durations[0][1] - durations[0][0]
        start = 0
        end = 1
        duration = 0
        if not date_time:
            if isinstance(durations[0][0], datetime.datetime):
                date_time = datetime.datetime.now()
            else:
                raise IOError('请输入截止值date_time')
        while end < len(durations):
            if durations[start][0] > date_time:
                break
            if durations[start][1] > date_time:
                duration += date_time - durations[start][0]
                break
            else:
                if durations[start][1] > durations[end][1]:
                    end += 1
                elif durations[end][0] < durations[start][1] < durations[end][1]:
                    duration += durations[end][0] - durations[start][0]
                    if end == len(durations) - 1:
                        duration += durations[end][1] - durations[end][0]
                    start = end
                    end += 1
                else:
                    duration += durations[start][1] - durations[start][0]
                    if end == len(durations) - 1:
                        duration += durations[end][1] - durations[end][0]
                    start = end
                    end += 1
        return duration


if __name__ == '__main__':
    print(DurationCalculate.duration_calculate([[1, 5], [2, 3], [6, 9]], date_time=10))

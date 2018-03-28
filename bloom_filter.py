# -*- coding: utf-8 -*-

"""
Copyright () 2018

All rights reserved

FILE: bloom_filter.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2018/3/28 上午9:44

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2018/3/28 上午9:44
"""

"""
    布隆过滤器：可以用于检索一个元素是否在一个集合中
    优点：空间效率和查询时间都远远超过一般的算法
    缺点：有一定的误识别率和删除困难
"""

from bitarray import bitarray
import mmh3


class BloomFilter(set):

    def __init__(self, size, hash_count):
        super(BloomFilter, self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.size = size
        self.hash_count = hash_count

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.bit_array)

    def __contains__(self, item):
        out = True
        for ii in range(self.hash_count):
            index = mmh3.hash(item, ii) % self.size
            if self.bit_array[index] == 0:
                out = False
        return out

    def add(self, item):
        for ii in range(self.hash_count):
            index = mmh3.hash(item, ii) % self.size
            self.bit_array[index] = 1
        return self


def main():
    bloom = BloomFilter(100, 10)
    animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle', 'bird', 'bison', 'boar', 'butterfly',
               'ant', 'anaconda', 'bear', 'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
    for animal in animals:
        bloom.add(animal)
    for animal in animals:
        if animal in bloom:
            print('{} is in bloom filter as expected'.format(animal))
        else:
            print('Something is terribly went wrong for {}'.format(animal))
            print('FALSE NEGATIVE!')

    other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox', 'whale', 'shark', 'fish', 'turkey', 'duck',
                     'dove', 'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla', 'hawk']
    for other_animal in other_animals:
        if other_animal in bloom:
            print('{} is not in the bloom, but a false positive'.format(other_animal))
        else:
            print('{} is not in the bloom filter as expected'.format(other_animal))


if __name__ == '__main__':
    main()

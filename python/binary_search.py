"""
binary search algorithm

CASE1
input : 1 2 5 9 10 12 15 16 17
input : 16
output : there is 16

CASE2
input : 1 4 6 9 10 11
input : 6
output : there is 6

CASE3
input : 1 4 6 9 10 11
input : 7
output : there is not 7
"""

from math import ceil


def binary_search(key, arr=[]):
    pl = 0
    pr = len(arr) - 1
    while pl <= pr:
        pc = ceil((pl + pr) / 2)
        if arr[pc] == key:
            return pc
        elif arr[pc] < key:
            pl = pc + 1
        elif arr[pc] > key:
            pr = pc - 1
    return -1


if __name__ == '__main__':
    inputArr = list(map(int, input().split()))
    inputKey = int(input())
    result = binary_search(inputKey, inputArr)
    print("there is not " + str(inputKey) if result == -1 else "there is str " + str(inputKey))
"""
sentinel linear search algorithm (보초법)
better then vanilla linear search
CASE1 (Success)
input : 1 4 6 7 9
input : 7
output : there is 7

CASE2 (Fail)
input : 2 5 6 7 9
input : 1
output : there is not 1
"""


def sentinel_linear_search(search, array=[]):
    array.append(search)
    idx = 0
    while array[idx] != search:
        idx += 1
    return -1 if idx == len(array) - 1 else search


if __name__ == '__main__':
    input_array = list(map(int, input().split()))
    input_num = int(input())
    result = sentinel_linear_search(input_num, input_array)
    if result == -1:
        print("there is not " + str(input_num))
    else:
        print("there is " + str(input_num))

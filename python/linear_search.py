"""
linear search algorithm

CASE1 (Success)
input : 1 4 6 7 9
input : 7
output : there is 7

CASE2 (Fail)
input : 2 5 6 7 9
input : 1
output : there is not 1
"""


def linear_search(num, array=[]):
    for attr in array:
        if attr == num:
            return num
    return -1


if __name__ == '__main__':
    input_array = list(map(int, input().split()))
    input_num = int(input())
    result = linear_search(input_num, input_array)
    if result == -1:
        print("there is not " + str(input_num))
    else:
        print("there is " + str(input_num))

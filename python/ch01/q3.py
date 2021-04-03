"""
search min value
int min4(int a, int b, int c);

input : 5 1 9 3
output : 1
"""
nums = list(map(int, input().split()))


def min4(array=[]):
    result = array[0]

    for num in array:
        if num < result:
            result = num


print(min4(nums))

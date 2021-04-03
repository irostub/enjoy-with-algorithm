"""
search min value
int min3(int a, int b, int c);

input : 1 4 9
output : 1
"""
nums = list(map(int, input().split()))


def min3(array=[]):
    result = array[0]

    for num in array:
        if num < result:
            result = num


print(min3(nums))

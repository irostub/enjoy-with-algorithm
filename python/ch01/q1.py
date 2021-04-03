"""
search max value
int max4(int a, int b, int c, int d);

input : 1 4 9 3
output : 9
"""
nums = list(map(int, input().split()))


def max4(array=[]):
    result = array[0]
    for num in array:
        if num > result:
            result = num
    return result


print(max4(nums))

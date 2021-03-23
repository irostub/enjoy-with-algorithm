"""
bubble sort algorithm

CASE1
input : 1 9 6 2 4 3
output : [1, 2, 3, 4, 6, 9]
"""


def bubble_sort(attrs=[]):
    for i in range(len(attrs)):
        for j in range(i + 1, len(attrs)):
            if attrs[i] > attrs[j]:
                temp = attrs[i]
                attrs[i] = attrs[j]
                attrs[j] = temp
    return attrs


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(bubble_sort(nums))

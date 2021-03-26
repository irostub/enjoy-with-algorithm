"""
bubble sort algorithm

CASE1
input : 1 9 5 4 6 7
output : [1, 4, 5, 6, 7, 9]
"""

def bubble_sort(arr=[]):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[j - 1] > arr[j]:
                temp = arr[j-1]
                arr[j - 1] = arr[j]
                arr[j] = temp
    return arr


if __name__ == '__main__':
    inputArr = list(map(int, input().split()))
    print(bubble_sort(inputArr))


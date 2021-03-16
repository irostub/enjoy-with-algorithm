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

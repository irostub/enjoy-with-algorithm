"""
search middle num

CASE1 (Success)
input : 1 4 6
output : 4
"""


def search_middle_num(array=[]):
    a, b, c = array
    if a >= b:
        if a <= c:
            return a
        elif b >= c:
            return b
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


if __name__ == '__main__':
    search_middle_num(map(int, input().split()))


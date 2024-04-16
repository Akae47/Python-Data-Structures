# This is a progrtam for binary search
def binary_search(num, arr):
    n = len(arr)
    k = 0
    i = n // 2
    while i >= 1:
        while (k + i < n) and (arr[k + i] <= num):
            k = k + 1
        i = i // 2

    return k if arr[k] == num else -1


print(binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

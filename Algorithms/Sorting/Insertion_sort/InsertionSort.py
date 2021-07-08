def insertion_sort(arr):
    for i in range(1, len(arr)):
        while(i > 0 and arr[i] < arr[i - 1]):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr

if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(arr)
    print(arr)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for arr in tests:
        insertion_sort(arr)
        print(f'sorted array: {arr}')
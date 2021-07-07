def bubble_sort(arr):
    size = len(arr)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    arr = [1,7,4,9,20,73,5]
    arr = [1,2,3,4,2]
    arr = ["python", "javascript","typescript","ruby","cpp"]

    bubble_sort(arr)
    print(arr)

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [1,7,4,9,20,73,5]
    elements = [1,2,3,4,2]
    elements = ["python", "javascript","typescript","ruby","cpp"]

    bubble_sort(elements)
    print(elements)
from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1
if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21
    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")
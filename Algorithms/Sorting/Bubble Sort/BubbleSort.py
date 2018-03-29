import random


def swap(sequence, index_one, index_two):
    """swaps the values of or two indexs in a list"""
    temp = sequence[index_one]
    sequence[index_one] = sequence[index_two]
    sequence[index_two] = temp


def bubble_sort(sequence):
    """sorts a list using the bubble sort algorithm"""
    for run in range(len(sequence), 1, -1):
        for current_index in range(0, run - 1):
            if sequence[current_index] > sequence[current_index + 1]:
                swap(sequence, current_index, current_index + 1)


def generate_list(list_size, element_min, element_max):
    """"Generates a list of length list_size contianing
    randomly generated number"""
    sequence = [random.randint(element_min, element_max)
                for num in range(list_size + 1)]
    return sequence


if __name__ == "__main__":
    LIST = generate_list(10, -50, 100)
    print(LIST)
    bubble_sort(LIST)
    print(LIST)

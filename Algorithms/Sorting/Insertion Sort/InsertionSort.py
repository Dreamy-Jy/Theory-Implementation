import random


def insertion_sort(sequence):
    """sorts a list using the insertion sort algorithm"""
    for selected_index, selected_value in enumerate(sequence):
        shift_index = selected_index
        while shift_index > 0 and not sequence[shift_index - 1] < selected_value:
            sequence[shift_index] = sequence[shift_index - 1]
            shift_index -= 1
        sequence[shift_index] = selected_value


def generate_list(list_size, element_min, element_max):
    """Generates a list contianing list_size elements.
    Each element is a random int between or equal element_min
    and element_max"""
    sequence = [random.randint(element_min, element_max)
                for num in range(list_size + 1)]
    return sequence


if __name__ == "__main__":
    LIST = generate_list(10, -50, 100)
    print(LIST)
    insertion_sort(LIST)
    print(LIST)

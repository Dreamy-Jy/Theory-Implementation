import random as rand

def swap(sequence, index_one, index_two):
    temp = sequence[index_one]
    sequence[index_one] = sequence[index_two]
    sequence[index_two] = temp

def bubble_sort(sequence):
    for run in range(len(sequence), 1, -1):
        for currentIndex in range(0, run-1):
            if sequence[currentIndex] > sequence[currentIndex + 1]:
                swap(sequence, currentIndex, currentIndex + 1)

def generate_list(listSize, elementMin, elementMax):
    sequence = [rand.randint(elementMin,elementMax) for num in range(listSize + 1)]
    return sequence

if __name__ == "__main__":
    print()
    LIST = generateList(10, -50, 100)
    print(LIST)
    bubbleSort(LIST)
    print(LIST)

def selection_sort(array):
    minimal = 0
    for i in range(len(array)-1):
        minimal = i
        for j in range(minimal + 1, len(array)):
            if array[minimal] > array[j]:
                minimal = j
        if minimal != i:
            array[i], array[minimal] = array[minimal], array[i]
    return array

        
        
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    selection_sort(arr)
    print(arr)
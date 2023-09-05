def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            # can we do swap differently? 
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
        #array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')


insertion_sort([11, 2, 9, 7, 1])

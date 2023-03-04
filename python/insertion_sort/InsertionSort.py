def insertion_sort(data: list):
    count_swaps = 0
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while (key < data[j]) and (j >= 0):
            data[j+1] = data[j]
            count_swaps+=1
            j -= 1
        data[j+1] = key
    return data, count_swaps


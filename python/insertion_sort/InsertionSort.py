def insertion_sort(data: list):
    """
        Retorna a lista ordenada em ordem crescente
        :param lista: Lista que será ordenada
        :return: Uma tupla contendo a lista ordenada e a quantidade de trocas (Swaps) que foram feitos
        Complexidade no pior caso (a lista está em ordem decrescente): O(n²)
        """
    count_swaps = 0
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while (key < data[j]) and (j >= 0):
            data[j+1] = data[j]
            count_swaps += 1
            j -= 1
        data[j+1] = key
    return data, count_swaps


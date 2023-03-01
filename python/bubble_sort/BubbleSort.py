
def bubble_sort(dados):
    """
    Ordena um array em ordem crescente utilizando o algoritmo de ordenação Bubble Sort
    :param dados: dados que serão ordenados
    :return: O array ordenado (in-place) *printa tambem a quantidade de trocas efetuadas
    """
    m = 1
    n = len(dados)
    count_swaps = 0
    for i in range(n - m):
        for j in range(n-1):
            if dados[j] > dados[j+1]:
                dados[j], dados[j+1] = dados[j+1], dados[j]
                count_swaps += 1
                # aux = dados[j]
                # dados[j] = dados[j+1]
                # dados[j + 1] = aux
        m += 1
    print(f'>> Quantidade de trocas: {count_swaps}')
    return dados




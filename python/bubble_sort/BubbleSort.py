


def bubble_sort(dados):
    m = 1
    n = len(dados)
    count_swaps = 0
    for i in range(n - m):
        for j in range(n-1):
            v1 = dados[j]
            v2 = dados[j+1]
            if v1 > v2:
                count_swaps +=1
                aux = v1
                dados[j] = v2
                dados[j + 1] = aux
        m += 1
    print(f'>> Quantidade de trocas: {count_swaps}')
    return dados




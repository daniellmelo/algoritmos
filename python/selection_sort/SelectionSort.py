
def selection_sort(lista: list):
    count_swap = 0
    """
    Retorna a lista ordenada em ordem crescente
    :param lista: Lista que será ordenada
    :return: Uma tupla contendo a lista ordenada e a quantidade de trocas (Swaps) que foram feitos
    Complexidade no pior caso (a lista está em ordem decrescente): O(n²)
    """
    n = len(lista)
    for i in range(n-1):
        menor = i
        for j in range(i+1, n):
            atual = j
            if lista[atual] < lista[menor]:
                menor = atual
        if i != menor:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux
            count_swap += 1
    return lista, count_swap




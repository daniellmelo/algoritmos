from random import sample
from MergeSort import merge_sort

dados_ordenados = [i for i in range(0, 19)]
dados_inversamente_ordenados = [i for i in range(5, 0, -1)]
dados_inversamente_ordenados_2 = [i for i in range(10, 0, -1)]
dados_inversamente_ordenados_3 = [i for i in range(20, 0, -1)]
dados_aleatorios = sample(range(1, 100), 5)
dados_aleatorios_2 = sample(range(1, 100), 10)
dados_aleatorios_3 = sample(range(1, 100), 20)
dados_repetidos = [1, 1, 1, 1, 1, 9, 9, 9, 8, 8, 8, 8, 6, 0, 0, 0, 0]


print(merge_sort(dados_ordenados))
print(merge_sort(dados_inversamente_ordenados))
print(merge_sort(dados_inversamente_ordenados_2))
print(merge_sort(dados_inversamente_ordenados_3))
print(merge_sort(dados_aleatorios))
print(merge_sort(dados_aleatorios_2))
print(merge_sort(dados_aleatorios_3))
print(merge_sort(dados_repetidos))

from bubble_sort.BubbleSort import bubble_sort
import random

dados_ordenados = [i for i in range(0, 19)]

dados_inversamente_ordenados = [i for i in range(5, 0, -1)]
dados_inversamente_ordenados_2 = [i for i in range(10, 0, -1)]
dados_inversamente_ordenados_3 = [i for i in range(20, 0, -1)]
dados_aleatorios = random.sample(range(1, 100), 5)
dados_aleatorios_2 = random.sample(range(1, 100), 10)
dados_aleatorios_3 = random.sample(range(1, 100), 20)
dados_repetidos = [1, 1, 1, 1, 1, 9, 9, 9, 8, 8, 8, 8, 6, 0, 0, 0, 0]
print('Bubble Sort:\nFaz comparações entre elementos consecutivos e troca eles de posição caso a comparação demonstre que o número da direita é menor (ou maior, dependendo da ordenação desejada).\n')
print("""O bubble sort, ou ordenação por flutuação (literalmente "por bolha"), é um algoritmo de ordenação dos mais simples. 
A ideia é percorrer o vector diversas vezes, e a cada passagem fazer flutuar para o topo o maior elemento da sequência. Essa movimentação lembra a forma como as bolhas em um tanque de água procuram seu próprio nível,e disso vem o nome do algoritmo. 
>> No melhor caso, o algoritmo executa n operações relevantes, onde n representa o número de elementos do vector. 
>> No pior caso, são feitas n^2 operações. 
>> A complexidade desse algoritmo é de ordem quadrática. Por isso, ele não é recomendado para programas que precisem de velocidade e operem com quantidade elevada de dados.\n Fonte: https://pt.wikipedia.org/wiki/Bubble_sort\n""")

print('A complexidade de espaço, no pior caso, é O(1) (auxiliar), onde ocupa-se apenas a variável auxiliar\n')

print('--------------------------------------------------------------------------------------------------------------------------------------------')
print(' --- MELHOR CASO: DADOS JÁ ORDENADOS ---')
print(f'>> Array de entrada: {dados_ordenados}')
print('>> Complexidade: O(n)')
print(f'Array de saída: {bubble_sort(dados_ordenados)}')
print('--------------------------------------------------------------------------------------------------------------------------------------------')

print(' --- PIOR CASO: DADOS INVERTIDOS ---')

print('>> Complexidade: O(n²)')
print(f'>> Observe como a quantidade de trocas aumenta muito conforme a quantidade de termos aumenta')
print('EXEMPLO 1:')
print(f'>> Array de entrada: {dados_inversamente_ordenados}')
print(bubble_sort(dados_inversamente_ordenados))
print('EXEMPLO 2:')
print(f'>> Array de entrada: {dados_inversamente_ordenados_2}')
print(bubble_sort(dados_inversamente_ordenados_2))
print('EXEMPLO 3:')
print(f'>> Array de entrada: {dados_inversamente_ordenados_3}')
print(bubble_sort(dados_inversamente_ordenados_3))
print('--------------------------------------------------------------------------------------------------------------------------------------------')
print(' --- CASO MÉDIO: NÚMEROS SORTIDOS ---')
print('>> Complexidade: O(n²)')
print('EXEMPLO 1:')
print(f'>> Array de entrada: {dados_aleatorios}')
print(bubble_sort(dados_aleatorios))
print('EXEMPLO 2:')
print(f'>> Array de entrada: {dados_aleatorios_2}')
print(bubble_sort(dados_aleatorios_2))
print('EXEMPLO 3:')
print(f'>> Array de entrada: {dados_aleatorios_3}')
print(bubble_sort(dados_aleatorios_3))
print('--------------------------------------------------------------------------------------------------------------------------------------------')
print(' --- CASO MÉDIO: NÚMEROS REPETIDOS ---')
print('>> Complexidade: O(n²)')
print(bubble_sort(dados_repetidos))
print('--------------------------------------------------------------------------------------------------------------------------------------------')

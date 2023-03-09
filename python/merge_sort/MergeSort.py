
def merge_sort(data: list, inicio=0, fim=None):
    if not fim:
        fim = len(data)
    if fim - inicio > 1:
        meio = (fim + inicio)//2
        merge_sort(data, inicio, meio)
        merge_sort(data, meio, fim)
        merge(data, inicio, meio, fim)
    return data

def merge(data, inicio, meio, fim):
    left = data[inicio:meio]
    right = data[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            data[k] = right[j]
            j += 1
        elif j >= len(right):
            data[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1





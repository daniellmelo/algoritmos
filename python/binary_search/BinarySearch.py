def binary_search(lista: list, item, begin: int = 0, end: int = None) -> bool:
    if end is None:
        end = len(lista)-1
    if begin <= end:
        mid = (begin + end)//2
        if lista[mid] == item:
            return True
        if item < lista[mid]:
            return binary_search(lista, item, begin, mid-1)
        else:
            return binary_search(lista, item, mid+1, end)
    return False

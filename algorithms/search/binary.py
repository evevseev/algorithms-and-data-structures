def lower_bound(arr: list, key) -> int:
    l, r = 0, len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] < key:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(arr: list, ket) -> int:
    l, r = 0, len(arr)
    
    while l < r:
        m = (l + r) // 2
        if arr[m] <= key:
            l = m + 1
        else:
            r = m
    return l
    
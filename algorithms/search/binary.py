def lower_bound(arr: list[int], key: int) -> int:
    l, r = 0, len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] < key:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(arr: list[int], key: int) -> int:
    l, r = 0, len(arr)
    
    while l < r:
        m = (l + r) // 2
        if arr[m] <= key:
            l = m + 1
        else:
            r = m
    return l
    
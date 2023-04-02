def linear_search(arr: list[int], key: int) -> int:
    # or: for i in enumerate(arr)
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return len(arr)

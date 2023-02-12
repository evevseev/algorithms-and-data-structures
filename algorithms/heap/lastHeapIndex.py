def lastHeapIndex(arr: list) -> int:
    if not arr:
        return 0

    for i in range(1, len(arr)):
        parent = (i - 1) // 2
        if arr[i] > arr[parent]:
            return i - 1

    return len(arr) - 1

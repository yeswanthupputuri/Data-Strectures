def countingsort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for num in range(len(count)):
        for _ in range(count[num]):
            result.append(num)
    return result
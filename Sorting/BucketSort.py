def bucketsort(arr):
    if len(arr) <= 1:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    range = (max_val - min_val) / bucket_count
    if range == 0:
        return arr 
    buckets = [ [] for _ in range(bucket_count)]
    for num in arr:
        index = int((num - min_val) / range)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
    result = []
    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)
    return result
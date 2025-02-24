def find_pairs(arr, target):
    seen = set()
    pairs = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return len(pairs)

print(find_pairs([1, 5, 3, 7, 9], 10)) 

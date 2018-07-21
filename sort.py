def quicksort(a):
    if not a: return []
    key = a[0]
    left = [x for x in a[1:] if x<key]
    right = [x for x in a[1:] if x>=key]
    return quicksort(left) + [key] + quicksort(right)

print(quicksort([1,2,1]))
print(quicksort([]))
print(quicksort([4,3,5,2,1]))
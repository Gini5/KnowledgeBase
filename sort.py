def quicksort(a):
    # time: O(nlogn)~O(n^2)  space: O(nlogn)
    if not a: return []
    key = a[0]
    left = [x for x in a[1:] if x<key]
    right = [x for x in a[1:] if x>=key]
    return quicksort(left) + [key] + quicksort(right)

def mergesort(a):
    n = len(a)
    if n < 2: return a
    mid = n//2
    res = []
    l = mergesort(a[:mid])
    r = mergesort(a[mid:])

    while l and r:
        if l[0]<r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    while l:
        res.append(l.pop(0))
    while r:
        res.append(r.pop(0))

    return res

def insertsort(a):
    # time: O(n)~O(n^2) space: O(1)
    if not a: return a
    for i in range(1,len(a)):
        j = i-1
        tmp = a[i]
        while j>=0 and tmp<a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp
    return a

def shellsort(a):


print(mergesort([1,2,1]))
print(mergesort([1,2]))
print(mergesort([]))
print(mergesort([4,3,5,2,1]))
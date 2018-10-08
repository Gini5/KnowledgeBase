def quicksortrecurse(a):
    # time: O(nlogn)~O(n^2)  space: O(nlogn)
    if not a: return []
    key = a[0]
    left = [x for x in a[1:] if x<key]
    right = [x for x in a[1:] if x>=key]
    return quicksortrecurse(left) + [key] + quicksortrecurse(right)

def quicksort(a,low,high):
    if low>=high: return
    l, h = low, high
    key = a[low]
    while l<h:
        while l<h and a[h]>=key:
            h -= 1
        a[l] = a[h]
        while l<h and a[l]<=key:
            l += 1
        a[h] = a[l]
    a[l] = key      #at this point: l == h
    quicksort(a,low,l-1)
    quicksort(a,h+1,high)
    return a

def mergesort(a):
    # time: O(nlogn)  space: O(n) = O（n)+O(n/2)+O(n/4)+...
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

def bubblesort(a):
    # time: O(n^2)  space: O(1)
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def selectSort(relist):
    len_ = len(relist)
    for i in range(len_):
        min_index = i
        for j in range(i+1,len_):  # 这个循环会找到值比第i个索引所代表值小的索引
            if relist[j] < relist[min_index]:
                min_index = j
        relist[i] ,relist[min_index] = relist[min_index], relist[i]  # 互换两个索引位置
    return relist

def shell_sort(relist):
    n = len(relist)
    gap = n/2  # 初始步长
    while gap > 0:
        for i in range(gap, n):
            temp = relist[i]   # 每个步长进行插入排序
            j = i
            # 插入排序
            while j >= gap and relist[j - gap] > temp:
                relist[j] = relist[j - gap]
                j -= gap
            relist[j] = temp

        gap = gap/2  # 得到新的步长

    return relist
times = [1,4,6,8,10]
t = 11

# binary search, if not hit, return left element
l,r = 0, len(times)
while l<r:
    mid = (l+r)//2
    if times[mid] <= t:
        l = mid + 1
    else:
        r = mid
print(l-1)

# if not hit, return right element
l, r = 0, len(times)
while l<r:
    mid = (l+r)//2
    if times[mid]>=t:
        r = mid -1
    else:
        l = mid+1
print(r+1)
times = [1,4,6,8,10]
t = 11

# binary search, if not hit, return left element
l,r = 0, len(times)-1
while l<r:
    mid = (r+l)//2
    if times[mid] == t:
        break
    elif times[mid] < t:
        l = mid+1
        mid = l
    else:
        r = mid-1
        mid = r
if mid > 0 and times[mid] > t: mid -= 1
print(mid)
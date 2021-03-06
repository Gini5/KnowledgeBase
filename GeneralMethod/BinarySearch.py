times = [1,4,6,8,10]
t = 3

#typical binary search, nums sorted, if doesn't exsit, return -1
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            mid = nums[m]
            if mid == target:
                return m
            elif mid<target:
                l = m+1
            else:
                r = m-1
        return -1

# binary search, if not hit, return left element
# means to find the first > t, so if mid<=t, ignore
l,r = 0, len(times)
while l<r:
    mid = (l+r)//2
    if times[mid] <= t:
        l = mid + 1
    else:
        r = mid
print(l-1)

# if not hit, return right element
# means to find the first < t, so if mid>=t, ignore
# be careful to set mid as the right element, or in case [1,4] t = 5 will get endless loop
l, r = 0, len(times)
while l<r:
    mid = (l+r)//2+1
    if times[mid]>=t:
        r = mid -1
    else:
        l = mid
print(r+1)
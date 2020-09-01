#[1,10,3,2,5,4,1] [3,2][5,4]
# stack: [1,4,5]  [1,2,4,5]


def reversePair(arr):
    n = len(arr)
    res = 0
    stack = []
    for i in range(n-1,-1,-1):
        if not stack:
            stack.append(arr[i])
        else:
            l, r = 0, len(stack)
            while l<r:
                m = (l+r)//2
                if stack[m] > arr[i]:
                    r = m
                else:
                    l = m+1
            res += l
            if l == len(stack): stack.append(arr[i])
            else:
                stack = stack[:l] + arr[i] + stack[l:]
    return res
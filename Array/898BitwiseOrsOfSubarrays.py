def subarrayBitwiseORs(A):
    res, cur = set(), set()
    for i in A:
        cur2 = {i}
        for j in cur:
            cur2.add(i | j)
        cur = cur2
        res |= cur
    return len(res)

print(subarrayBitwiseORs([1,2,4]))
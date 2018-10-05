def subarrayBitwiseORs(A):
    res, cur = set(), set()
    for i in A:
        cur = { i|j for j in cur } | {i}
        res |= cur
    return len(res)

print(subarrayBitwiseORs([1,2,4]))
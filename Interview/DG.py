def PowerSetsRecursive2(items):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in items:
        result += [subset + [x] for subset in result]
    return result


print(PowerSetsRecursive2([1,2,3,4]))


def top2(l):
    if len(l)<2: return
    top1, top2 = l[0], l[1]
    if top1<top2: top1, top2 = top2, top1

    for item in l[2:]:
        if item>top1:
            if top1>top2: top2 = top1
            top1 = item
        elif item>top2:
            top2 = item
    return [top1,top2]

print(top2([1,3,2,4,7,5]))
print(top2([7,3,2,4,7,5]))
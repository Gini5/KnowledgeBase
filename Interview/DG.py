def PowerSetsRecursive2(items):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in items:
        result += [subset + [x] for subset in result]
    return result


print(PowerSetsRecursive2([1,2,3,4]))
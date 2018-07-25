def threesum(arr):
    #target is 0
    res = []
    n = len(arr)
    arr.sort()
    def twosum(low, high, target):
        while low<high:
            if arr[low]+arr[high] == target:
               res.append([arr[low],arr[high],-target])
               while low<high and arr[low] == arr[low+1]: low += 1
               while low<high and arr[high] == arr[high-1]: high -= 1
               low += 1
               high -= 1
            elif arr[low]+arr[high] < target: low += 1
            else: high -= 1

    for i in range(n-2):
        if i == 0 or i>0 and arr[i-1] != arr[i]:
            twosum(i+1, n-1, -arr[i])
    return res


def nsum(arr, target):
    #apply to n-sum with target
    res = []
    arr.sort()

    def ksum(nums, target, k, result, value):
        if k == 2:
            low, high = 0, len(nums) -1
            while low < high:
                if nums[low] + nums[high] == target:
                    result.append(value + [nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]: low += 1
                    while low < high and nums[high] == nums[high - 1]: high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1
        elif k > 2:
            for i in range(len(nums)-k+1):
                if target < nums[i] * k or target > nums[-1] * k:  # optimize redundant calculation
                    break
                if i == 0 or i>0 and nums[i-1] != nums[i]:
                    ksum(nums[i+1:], target-nums[i], k-1, result, value+[nums[i]])

    ksum(arr, target, 4, res, [])
    return res

print(nsum([1, 0, -1, 0, -2, 2], 0))
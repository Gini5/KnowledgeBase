def cal(SUM,N):
    dp = [[]]*(SUM+1)
    for i in range(SUM+1):
        result = []
        for j in range(1,i+1):
            if j<=N:
                if j == i:
                    result.append([j])
                else:
                    for item in dp[i-j]:
                        new = item+[j]
                        new.sort()
                        if new not in result: result.append(new)
            else: break
        dp[i] = result
    return dp

res = cal(10,5)
for item in res:
    print(item)
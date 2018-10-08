def spiral(N):
    m, n = int(N**0.5), int(N**0.5)
    move = 'r'
    a = [[0 for _ in range(n)] for _ in range(m)]
    s = 1
    L,R,U,D = 0, n-1, 0, m-1
    i,j = 0,0
    while s <= N:
        a[i][j] = s
        if move == 'r':
            if j<R:
                j += 1
            else:
                move = 'd'
                U += 1
                i += 1
        elif move == 'd':
            if i<D:
                i += 1
            else:
                move = 'l'
                R -= 1
                j -= 1
        elif move == 'l':
            if j>L:
                j -= 1
            else:
                move = 'u'
                D -= 1
                i -= 1
        elif move == 'u':
            if i>U:
                i -= 1
            else:
                move = 'r'
                L += 1
                j += 1
        s += 1
    return a

print(spiral(25))
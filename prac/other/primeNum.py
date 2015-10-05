def seive(n):
    arr = [None] * (n+1)
    i = 2
    for i in range(2,len(arr)):
        if arr[i] == None:
            j = i + i
            while j <= n:
                arr[j] = 0
                j += i
    for i in range(2,len(arr)):
        if arr[i] != 0:
            print i

seive(100)

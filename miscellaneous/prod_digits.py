def getNum(n):
    res = ""
    while n > 1:
        found = False
        for i in range(9, 1, -1):
            if n % i == 0:
                res = str(i) + res
                n = n // i
                found= True
                break
        if not found:
          return -1
    return int(res)
    
print(getNum(22))
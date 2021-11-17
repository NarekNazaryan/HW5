def Find(n):
    return list(set(range(1, len(n) + 1)) - set(n))

print(Find([4,3,2,7,8,2,3,1]))
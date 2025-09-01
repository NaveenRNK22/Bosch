lst = [1,2,3,4,5]
k = 2
k %= len(lst)
print(lst[-k:] + lst[:-k])
lst = [1,2,2,3,4,4,4,5]
freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
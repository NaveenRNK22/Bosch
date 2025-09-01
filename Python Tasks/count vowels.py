s = "Naveen Kumar R"
vowels = "aeiouAEIOU"
v = 0
c = 0
for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
print(v, c)

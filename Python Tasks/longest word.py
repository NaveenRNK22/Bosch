sentence = input("Enter String:")
words = sentence.split()
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)

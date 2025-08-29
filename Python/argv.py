import sys

print(len(sys.argv))
tot=0
print(sys.argv[0])
for i in range(1,len(sys.argv)):
    tot+=int(sys.argv[i])
print(tot)
a = [1,2,3,4,5]
x = 4
low, high = 0
while low <= high:
    mid = (low+high)//2
    if arr[mid] == x:
        print(mid)
        break
    elif arr[mid] < x:
        low = mid+1
    else:
        high = mid-1

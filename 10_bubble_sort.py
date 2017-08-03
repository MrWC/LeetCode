n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

totalSwap = 0
for i in range(n):
    thisRound = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            thisRound += 1
    if thisRound == 0:
        break
    else:
        totalSwap += thisRound
print("Array is sorted in {0} swaps.".format(totalSwap))
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[-1]))

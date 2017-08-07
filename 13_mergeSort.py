import sys

def mergeSort(alist):
    count = 0
    leftcount = 0
    rightcount = 0
    blist = [] 
    if len(alist) > 1:
       mid = len(alist) // 2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       leftcount, lefthalf = mergeSort(lefthalf)
       rightcount, righthalf = mergeSort(righthalf)

       i = 0
       j = 0

       while i < len(lefthalf) and j < len(righthalf):
         if lefthalf[i] <= righthalf[j]:
             blist.append(lefthalf[i])
             i += 1
         else:
             blist.append(righthalf[j])
             j += 1
             count += len(lefthalf[i:])

       if i < len(lefthalf):
          blist = blist + lefthalf[i:]

       if j < len(righthalf):
          blist = blist + righthalf[j:]
    else:
        blist = alist[:]
    # print(count,leftcount,rightcount, blist)
    return count + leftcount + rightcount, blist

def countInversions(arr):
    count, res = mergeSort(arr)
    return count

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)

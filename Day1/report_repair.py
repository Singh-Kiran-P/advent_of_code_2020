"""
  X = 2020
  - Sort the given array
    * Using Merge sort
      > O(nlog(n))

  - Find for every element (e) n times in the array the complement c = (X-e)
    * Using Binary search
      > O(log(n))

  Total cost:
    - O(n*log(n)) + O(n*log(n))
"""

"""
Merge sort
  - Merge two lists -> O(n)
  - Merge sort -> MergeLists + O(log(n))
  - Total cost ->O(n*log(n))
"""

def mergeLists(l1, l2):
    i = 0
    j = 0
    result = []

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    result += l1[i:]
    result += l2[j:]

    return result


def merge_sort(arr):
    if len(arr) <= 1:  # base case
        return arr
    else:
        mid = len(arr)//2
        leftMerge = merge_sort(arr[:mid])
        rightMerge = merge_sort(arr[mid:])

        return mergeLists(leftMerge, rightMerge)


"""
Binary search
  - Give the index of x in arr
  - O(log(n))
"""


def BS(arr, l, r, x):
    if l < r:
        mid = (l+r)//2

        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return BS(arr, l, mid-1, x)
        else:
            return BS(arr, mid+1, r, x)
    else:
        return -1


"""
Report repair
  - X = 2020
"""
def report_repair(arr, X):

    # sort array
    arr = merge_sort(arr)

    # loop through each element (e)
    for e in arr:
        complement = X-e

        entry1 = e

        # Find the complement in arr
        indexFoundResult = BS(arr, 0, len(arr), complement)

        if indexFoundResult != -1:
            entry2 = arr[indexFoundResult]
            return entry1 * entry2

    return -1


""" Input file -> Array """

f = open("Day1/input.txt", "r")
arr = []
X=2020

for x in f:
  arr.append(int(x))

import time

# starting time
start = time.time()

# Code
Out = report_repair(arr,X)

# end time
end = time.time()

# total time taken
print(f"Runtime of the program is {end - start}")

print(Out)

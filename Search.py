#Jump Search
import math

def jumpSearch(arr, x, n):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == x:
        return prev

    return -1

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]


arr = [4, 25, 30, 51, 54, 66, 72, 118, 122, 125, 144, 167, 247, 284]
x = 66
n = len(arr)
index = jumpSearch(arr, x, n)
print("Число ", x, "має індекс: ", "%.0f" % index)

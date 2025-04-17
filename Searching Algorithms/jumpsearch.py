import math

def jump(arr,target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev,min(step,n)):
        if arr[i] == target:
            return i

    return -1

# Test
arr = [2, 5, 8, 12, 15, 19, 23, 28, 31, 35, 39, 44]
x = 31
result = jump(arr, x)
print(f"Found at index: {result}")  # Output: Found at index: 8
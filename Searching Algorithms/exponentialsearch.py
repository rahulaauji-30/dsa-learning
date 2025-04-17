import math
def exponential_search(arr,key):
    k = 1
    b = int(math.pow(2,k)) #size of the block
    n = len(arr)

    if arr[0]== key:
        return 0
    while arr[b] <=key and b < n:
        k += 1
        b = int(math.pow(2,k))
        low = 0
        high = n - 1
        while low <= high:
            mid =( low + high ) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == "__main__":
    result = exponential_search([6, 11, 19, 24, 33, 54, 67, 81, 94, 99],81)
    print(result)

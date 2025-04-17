"""
It is the improved variant of the binary search.
It to work sorted array is required. following formula is used to calculate the middle int this algorithm.

mid = L + (H-L) * (X - A[L]) / (A[H] - A[L]
L = Lowest Index of the list
H = Highest index of the list
A = Array
X= key to be searched.

STEPS to implement interpolation search.
STEP 1: Start searching data from the middle of the list.
STEP 2: Compaire the key with the mid element if matched return the index.
STEP 3:If not matched probe position using the formula and find new mid
STEP 4: If data is greater than middle go to higher sub-array.
STEP 5: If data is less than middle go to the lower sub-array.
STEP 6: Repeat the process until element is found.
"""

def interpolation_searching(arr, low, high, X):
    if low <= high and arr[low] <= X <= arr[high]:
        if arr[high] == arr[low]:  # Prevent division by zero
            return low if arr[low] == X else -1

        mid = low + ((high - low) * (X - arr[low])) // (arr[high] - arr[low])

        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            return interpolation_searching(arr, mid + 1, high, X)
        else:
            return interpolation_searching(arr, low, mid - 1, X)
    return -1

def interpolation_search_new(a,low,high,x):
    if low <= high  and a[low] <= x <= a[high]:
        if a[low] == a[high]:
            return low if arr[low] == x else -1

        mid = low + (((high-low) * (x - a[low])) // a[high] - a[low])

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            return interpolation_search_new(a, mid + 1, high, x)
        else:
            return interpolation_search_new(a, low, mid - 1, x)
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print(interpolation_search_new(arr,0,len(arr) - 1,5))

"""
This algorithm is considered as the fastest algorithm as it have the time complexity of the O(log n).
for this algorithm to work the array should be in the sorted form.
This algorithm works on the divide and conquer principle.It divides the array in two halves before searching.
STEPS:
STEP 1: Compare the element to be searched with the middle element if both element are same return the index of
    the middlemost element.

STEP 2: If it is not the desired element divide the array into right and left subtree and check if the desired
    element is greater or less than the median.

STEP 3: If the element is less than median search in left sub array if not then in right sub array.

STEP 4: Repeat the step 1,2 & 3 until the size of the sub array becomes 1

STEP 5: If the desired element not found then return the unsuccessful search.

"""

def binary_search(arr,low,high,key):
    mid = (low + high) // 2 # low 0 high 3
    if low <= high:
        if arr[mid] == key: #2
            print(f"Key is present at index {mid}")
        elif arr[mid] < key:
            binary_search(arr,mid+1,high,key)
        elif arr[mid] > key:
            binary_search(arr,low,mid-1,key)
    if low > high:
        print("Search Unsuccessful.")

if __name__ == "__main__":
    a = [6, 12, 14, 18, 22, 39, 55, 182]
    binary_search(a, 0, len(a)-1, 22)
    binary_search(a, 0, len(a)-1, 54)
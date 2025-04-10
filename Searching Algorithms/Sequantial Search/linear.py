"""
In this algorithm the time complexity for the best case is O(1)
And the worst case is O(n).
It goes through  each element of the data structure and check for every element.
It doesn't need array to be in sorted form.
"""

def linear_search(arr,key):
    count = 0
    for i,item in enumerate(arr):
        if item == key:
            print(f"Key Found at index {i}")
            count = count + 1
            return
    print("Key Not found")


if __name__ == "__main__":
    linear_search([10,20,30],5)
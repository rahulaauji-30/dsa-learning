
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i] #Swapping
    print(arr)
    return arr

if __name__ == "__main__":
    selection_sort([64, 25, 12, 22, 11])

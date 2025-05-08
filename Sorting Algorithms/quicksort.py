def quick_sort(nums, start, end):
    def partition(nums, start, end):
        idx = start-1  # Tracks the actual postion of the pivot
        pivot = nums[end]
        for j in range(start,end):
            if nums[j] <= pivot:
                idx += 1
                nums[idx], nums[j] = nums[j], nums[idx]
        idx += 1
        nums[idx], nums[end] = nums[end], nums[idx]
        return idx

    if start < end:
        piv_idx = partition(nums, start, end)
        quick_sort(nums, start, piv_idx - 1)
        quick_sort(nums, piv_idx + 1, end)

if __name__ == "__main__":
    arr = [8, 4, 1, 5, 2]
    print("Sorted Array")
    quick_sort(arr,0,len(arr)-1)
    print(arr)
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
    return nums


def recursive_bubble_sort(nums, n=None):
    if n is None:
        n = len(nums)

    # Base case
    if n == 1:
        return

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    recursive_bubble_sort(nums, n - 1)


if __name__ == "__main__":
    nums = [5, 2, 3, 4, 1]
    recursive_bubble_sort(nums)
    print(nums)


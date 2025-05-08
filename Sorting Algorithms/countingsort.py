def counting_sort(arr):
    n = len(arr)
    k = max(arr) + 1
    count = [0]*k
    output = [0] * n

    #to build the frequency array of count
    for i in range(n):
        count[arr[i]] += 1

    #to calculate the indexs
    for i in range(1,k):
        count[i] += count[i-1]
    #sorting of elements
    #it is started from end to maintain the stability
    i = n-1
    while i >= 0:
        idx = arr[i]
        count[idx] -= 1
        output[count[idx]] = idx
        i-= 1

    for j in range(n):
        arr[j] = output[j]

    return arr

if __name__ == "__main__":
    a = [0,1,2,0,3,0,1,2,4,0,0,1,1,2]
    print(f'Sorted Array:- {counting_sort(a)}')
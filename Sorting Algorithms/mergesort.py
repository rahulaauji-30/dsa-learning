def merge(a,start,mid,end):
    temp = []
    i = start
    j = mid +1
    while i <= mid and j <= end:
        if a[i] < a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1

    while i <= mid:
        temp.append(a[i])
        i+=1

    while j<= end:
        temp.append(a[j])
        j+=1

    for idx in range(len(temp)):
        a[idx + start ] = temp[idx]


def mergeSort(a,start,end):
    if start >= end:
        return
    mid = start + ((end-start)//2)
    mergeSort(a,start,mid)
    mergeSort(a,mid+1,end)
    merge(a,start,mid,end)
    return a
if __name__ == "__main__":
    a = [8,4,1,6,78,3,12]
    sorted_arr = mergeSort(a,0,len(a)-1)
    print(sorted_arr)
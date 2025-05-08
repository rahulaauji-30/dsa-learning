
def count_sort(a,n,p):
    count = [0]*10
    b = [0] * n
    for i in range(n):
        idx = (a[i]//p) % 10
        count[idx] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i>=0:
        idx = (a[i]//p) % 10
        count[idx] -= 1
        b[count[idx]] = a[i]
        i -= 1
    for i in range(n):
        a[i] = b[i]


def radix_sort(arr,n):
    max_element = max(arr)

    pos = 1

    while max_element//pos > 0:
        count_sort(arr,n,pos)
        pos = pos * 10
    print(arr)

if __name__ == "__main__":
    a = [236, 15, 333, 27, 9, 108, 76, 498]
    radix_sort(a,len(a))
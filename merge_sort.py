comparisons = 0

def merge(arr, left, mid, right):
    global comparisons

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(L) and j < len(R):
        comparisons += 1

        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


n = int(input("Enter number of students: "))

marks = list(map(int, input("Enter marks: ").split()))

print("\nOriginal Marks:", marks)

merge_sort(marks, 0, n - 1)

print("Sorted Marks:", marks)

print("Number of comparisons:", comparisons)

print("\nTime Complexity:")
print("Best Case    : O(N log N)")
print("Average Case : O(N log N)")
print("Worst Case   : O(N log N)")
print("Space        : O(N)")

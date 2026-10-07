# Merge Sort Using Divide and Conquer

## Aim

To implement Merge Sort using the Divide-and-Conquer technique in Python, arrange student marks in ascending order, display the original and sorted marks, and count the number of comparisons performed.

## Description

Merge Sort is a sorting algorithm based on the Divide-and-Conquer technique.

### Steps

1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.
4. Count the comparisons performed during merging.

## Program

The Python implementation is available in [merge_sort.py](merge_sort.py).

## Sample Input

```text
Enter number of students: 8
Enter marks: 85 42 73 19 56 91 34 68
```

## Sample Output

```text
Original Marks: [85, 42, 73, 19, 56, 91, 34, 68]
Sorted Marks: [19, 34, 42, 56, 68, 73, 85, 91]
Number of comparisons: 16

Time Complexity:
Best Case    : O(N log N)
Average Case : O(N log N)
Worst Case   : O(N log N)
Space        : O(N)
```

## Complexity Analysis

| Case | Time Complexity |
|---|---|
| Best Case | O(N log N) |
| Average Case | O(N log N) |
| Worst Case | O(N log N) |

**Auxiliary Space:** O(N)

## Technology Used

- Python
- Merge Sort
- Divide and Conquer

## How to Run

```bash
python merge_sort.py
```

## Result

Merge Sort was successfully implemented using the Divide-and-Conquer technique to sort student marks in ascending order while counting the comparisons.

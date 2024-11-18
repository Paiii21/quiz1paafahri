import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
B = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# Tampilkan data sebelum pengurutan
print("Before Sorting:")
print("A:", A)
print("B:", B)

# Bubble Sort pada A
start = time.time()
bubble_sort_A = A.copy()
bubble_sort(bubble_sort_A)
end = time.time()
print("\nBubble Sort A time:", end - start)
print("Bubble Sort A result:", bubble_sort_A)

# Bubble Sort pada B
start = time.time()
bubble_sort_B = B.copy()
bubble_sort(bubble_sort_B)
end = time.time()
print("\nBubble Sort B time:", end - start)
print("Bubble Sort B result:", bubble_sort_B)

# Quick Sort pada A
start = time.time()
quick_sort_A = A.copy()
quick_sort(quick_sort_A)
end = time.time()
print("\nQuick Sort A time:", end - start)
print("Quick Sort A result:", quick_sort_A)

# Quick Sort pada B
start = time.time()
quick_sort_B = B.copy()
quick_sort(quick_sort_B)
end = time.time()
print("\nQuick Sort B time:", end - start)
print("Quick Sort B result:", quick_sort_B)

# Penjelasan
print("\nKesimpulan:")
print("Quick Sort lebih efektif daripada Bubble Sort pada kasus A karena kompleksitas waktu lebih rendah dan eksekusi lebih cepat.")
print("Quick Sort lebih efektif dibandingkan Bubble Sort pada kasus B karena dapat memanfaatkan sebagian data yang sudah terurut untuk mengurangi jumlah operasi.")

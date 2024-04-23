# chia de tri : quicksort
def partition(arr, left, right):
    pivot_index = (left + right) // 2
    pivot_value = arr[pivot_index]

    print("\nPivot value:", pivot_value)
    i, j = left, right

    while i <= j:
        while arr[i] < pivot_value:
            i += 1
        while arr[j] > pivot_value:
            j -= 1
        if i <= j:
            print(f"Swap a[{i}]({arr[i]}) a[{j}]({arr[j]}): ", end="")
            arr[i], arr[j] = arr[j], arr[i]
            print(" ".join(map(str, arr)))
            i += 1
            j -= 1

    return i

def quickSort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        print("[", end=" ")
        for i in range(left, pivot_index):
            print(arr[i], end=" ")
        print("] ", end="")
        print("[", end=" ")
        for i in range(pivot_index, right + 1):
            print(arr[i], end=" ")
        print("] ")
        quickSort(arr, left, pivot_index - 1)  # Sắp xếp nửa bên trái
        quickSort(arr, pivot_index, right)     # Sắp xếp nửa bên phải

if __name__ == "__main__":
    arr = [42, 23, 74, 11, 65, 58, 94, 36, 99, 87]
    print("Mảng chưa sắp xếp:", " ".join(map(str, arr)))
    quickSort(arr, 0, len(arr) - 1)
    print("Mảng đã sắp xếp:", " ".join(map(str, arr)))

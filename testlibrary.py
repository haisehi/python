def partition(arr, low, high, indices):
    i = low - 1  # chỉ số của phần tử nhỏ hơn hoặc bằng pivot
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # Nếu phần tử hiện tại nhỏ hơn hoặc bằng pivot
        if arr[j] <= pivot:
            # tăng chỉ số của phần tử nhỏ hơn hoặc bằng pivot
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            indices[i], indices[j] = indices[j], indices[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    indices[i + 1], indices[high] = indices[high], indices[i + 1]
    return i + 1

# hàm dùng để biểu diễn thuật toán quicksort
def quicksort(arr, low, high, indices, level=1, print_indices=True):
    if low < high:
        # p là chỉ số của pivot sau khi partition
        p = partition(arr, low, high, indices)

        print(f"Luot {level}: p[{indices[p] + 1}] = {arr[p]}")
        print(f"Left = {indices[p] + 2}; ", end="")
        print(f"k = {high - low + 1}; ", end="")
        print(f"swap(A[{indices[high] + 1}], A[{indices[p] + 1}]) = swap({arr[high]}, {arr[p]})")
        if print_indices:
            print("Chi so:", end=" ")
            for idx in range(low, high + 1):
                print(indices[idx] + 1, end=" ")
            print("\nDay ban dau:", end=" ")
            for idx in range(low, high + 1):
                print(arr[idx], end=" ")
            print()

        # Sắp xếp các phần tử trước và sau pivot
        quicksort(arr, low, p - 1, indices, level + 1, False)
        quicksort(arr, p + 1, high, indices, level + 1, False)

# Nhập mảng từ người dùng
print("Nhap mang cac so, cach nhau bang dau cach: ", end="")
input_str = input()
arr = list(map(int, input_str.split()))
indices = list(range(len(arr)))

# Sử dụng hàm quicksort để sắp xếp mảng
print("\nDay ban dau:", end=" ")
for i in arr:
    print(i, end=" ")
print("\nChi so:", end=" ")
for i in range(1, len(arr) + 1):
    print(i, end=" ")
print("\n")

quicksort(arr, 0, len(arr) - 1, indices)

# In mảng đã sắp xếp
print("\nMang da sap xep:")
for i in arr:
    print(i, end=" ")

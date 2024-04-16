def partition(arr, low, high):
    i = (low - 1)  # chỉ số của phần tử nhỏ hơn hoặc bằng pivot
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # Nếu phần tử hiện tại nhỏ hơn hoặc bằng pivot
        if arr[j] <= pivot:
            # tăng chỉ số của phần tử nhỏ hơn hoặc bằng pivot
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

#hàm dùng để biểu diễn thuật toán quicksort
def quicksort(arr, low, high, level=1):
    if low < high:
        # p là chỉ số của pivot sau khi partition
        p = partition(arr, low, high)
        
        print(f"Lượt {level}: p[{p + 1}] = {arr[p]}")
        print("Left =", p + 2, end="; ")
        print(f"k = {high - low + 1};", end=" ")
        print(f"swap(A[{p + 2}], A[{high + 1}]) = swap({arr[p + 1]}, {arr[high]})")
        print("nên ta được:")
        for idx in range(low, high + 1):
            print(arr[idx], end=" ")
        print()

        # Sắp xếp các phần tử trước và sau pivot
        quicksort(arr, low, p - 1, level + 1)
        quicksort(arr, p + 1, high, level + 1)

# Nhập mảng từ người dùng
arr = input("Nhập mảng các số, cách nhau bằng dấu cách: ").split()
arr = [int(x) for x in arr]  # chuyển đổi mỗi phần tử sang kiểu số nguyên

# Sử dụng hàm quicksort để sắp xếp mảng
n = len(arr)
print("Dãy ban đầu:", end=" ")
for i in range(n):
    print("%d" % arr[i], end=" ")
print("\nChỉ số ", end="")
for i in range(1, n + 1):
    print(i, end=" ")
print("\n")
quicksort(arr, 0, n - 1)
print("\nMảng đã sắp xếp:")
for i in range(n):
    print("%d" % arr[i], end=" ")

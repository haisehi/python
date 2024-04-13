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

def quicksort(arr, low, high):
    if low < high:
        # p là chỉ số của pivot sau khi partition
        p = partition(arr, low, high)

        # Sắp xếp các phần tử trước và sau pivot
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

# Nhập mảng từ người dùng
arr = input("Nhập mảng các số, cách nhau bằng dấu cách: ").split()
arr = [int(x) for x in arr]  # chuyển đổi mỗi phần tử sang kiểu số nguyên

# Sử dụng hàm quicksort để sắp xếp mảng
n = len(arr)
quicksort(arr, 0, n - 1)
print("Mảng đã sắp xếp:")
for i in range(n):
    print("%d" % arr[i]),

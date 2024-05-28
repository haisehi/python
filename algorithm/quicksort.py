def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    print("Chọn pivot:", pivot)

    for j in range(low, high):

        # Nếu phần tử hiện tại nhỏ hơn pivot
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print("Mảng sau khi so sánh và sắp xếp:", arr)
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print("Bước sắp xếp:", arr[low:high+1])

        # Sắp xếp các phần trước và sau phần chia
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Mảng ban đầu
arr = [9,-3,5,2,6,8,-6,1,3]
n = len(arr)

print("Mảng ban đầu là:")
for i in range(n):
    print("%d" % arr[i], end=" ")

# Sắp xếp mảng
print("\nCác bước sắp xếp:")
quickSort(arr, 0, n - 1)

print("\nMảng sau khi sắp xếp là:")
for i in range(n):
    print("%d" % arr[i], end=" ")

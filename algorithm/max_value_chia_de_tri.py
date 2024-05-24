def max_value(arr, step=0):
    print("Bước lặp {}: {}".format(step, arr))
    if len(arr) == 1:
        print("Kết quả từ bước so sánh {}: {}".format(step, arr[0]))
        return arr[0]
    else:
        mid = len(arr) // 2
        print("Chia {}: {} | {}".format(step, arr[:mid], arr[mid:]))
        left_max = max_value(arr[:mid], step + 1)
        right_max = max_value(arr[mid:], step + 1)
        print("So sánh {}: {} | {}".format(step, left_max, right_max))
        max_val = max(left_max, right_max)                                                                                                                                                                                                  
        print("Kết quả từ bước so sánh {}: {}".format(step, max_val))
        return max_val

# Ví dụ sử dụng
arr = [2, 5, 6, 4, 3, 7, 1, 9, 8]
print("Mảng ban đầu:", arr)
print("Giá trị lớn nhất trong mảng là:", max_value(arr))

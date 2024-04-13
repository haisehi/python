#Thuật toán tham lam cho bài toán thuê xe-balo

def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    if n != len(values) or capacity <= 0:
        return "Dữ liệu không hợp lệ"

    # Tính tỷ lệ giá trị trên khối lượng của từng món đồ
    value_density = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sắp xếp danh sách các món đồ theo tỷ lệ giá trị trên khối lượng
    value_density.sort(reverse=True)

    total_value = 0
    total_weight = 0
    items_taken = []

    print("Bước 1: Sắp xếp các món đồ theo tỷ lệ giá trị trên khối lượng")
    print("Tỷ lệ - Khối lượng - Giá trị")
    for density, weight, value in value_density:
        print(f"{density:.2f} - {weight} - {value}")

    for density, weight, value in value_density:
        if total_weight + weight <= capacity:
            items_taken.append((weight, value))
            total_weight += weight
            total_value += value
            print(f"Bước 2: Chọn món đồ có tỷ lệ giá trị trên khối lượng cao nhất: Khối lượng = {weight}, Giá trị = {value}, Tổng trọng lượng = {total_weight}, Tổng giá trị = {total_value}")
        else:
            print(f"Bước 2: Bỏ qua món đồ có tỷ lệ giá trị trên khối lượng cao nhất: Khối lượng = {weight}, Giá trị = {value}")

    return total_value, items_taken

# Hàm nhập danh sách khối lượng và giá trị của các món đồ
def input_items():
    weights = list(map(int, input("Nhập khối lượng của các món đồ (cách nhau bằng dấu cách): ").split()))
    values = list(map(int, input("Nhập giá trị tương ứng của các món đồ (cách nhau bằng dấu cách): ").split()))
    return weights, values

# Nhập dung lượng tối đa của xe-balo
capacity = int(input("Nhập dung lượng tối đa của xe-balo: "))

# Nhập và tính toán
weights, values = input_items()
max_value, items = knapsack_greedy(weights, values, capacity)

# In kết quả
print("Kết quả cuối cùng:")
print("Tổng giá trị lớn nhất có thể đạt được:", max_value)
print("Các món đồ được chọn:", items)

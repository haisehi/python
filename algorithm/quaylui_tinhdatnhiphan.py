def generate_binary_sequences(n):
    def backtrack(sequence, index):
        # Nếu sequence đã có đủ n bit, in ra sequence và kết thúc hàm
        if index == n:
            print("".join(str(bit) for bit in sequence))
            return
        # Quay lui với bit 0
        sequence[index] = 0
        backtrack(sequence, index + 1)
        # Quay lui với bit 1
        sequence[index] = 1
        backtrack(sequence, index + 1)

    # Khởi tạo mảng sequence với n bit, tất cả các bit đều là 0 ban đầu
    sequence = [0] * n
    # Bắt đầu quay lui từ bit đầu tiên (index = 0)
    backtrack(sequence, 0)

# Nhập số bit của dãy nhị phân từ người dùng
n = int(input("Nhập số bit của dãy nhị phân: "))
print("Các dãy nhị phân có độ dài", n, "là:")
generate_binary_sequences(n)

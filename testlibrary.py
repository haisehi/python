def max_profit(N, K, profits):
    # Khởi tạo mảng DP
    DP = [0] * (N + 1)

    # DP[i] sẽ lưu lợi nhuận lớn nhất có thể đạt được khi xem xét các dự án từ 1 đến i
    for i in range(1, N + 1):
        # Tính DP[i] bằng cách so sánh lợi nhuận có thể đạt được bằng cách bỏ qua dự án thứ i
        # và lợi nhuận có thể đạt được bằng cách chọn dự án thứ i và K - 1 dự án trước đó
        DP[i] = max(DP[i-1], DP[max(0, i - K)] + profits[i-1])

    # Trả về lợi nhuận lớn nhất có thể đạt được
    return DP[N]

# Đọc dữ liệu đầu vào
N, K = map(int, input().split())
profits = []
for _ in range(N):
    profits.append(int(input()))

# Gọi hàm để tính toán lợi nhuận lớn nhất có thể đạt được
result = max_profit(N, K, profits)

# In kết quả
print(result)

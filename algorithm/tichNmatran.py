import sys

# Hàm tính toán và trả về số lượng phép toán nhân tối thiểu cần thiết để nhân dãy ma trận
def minMatrixMultiplications(dims, bracket, dp):
    n = len(dims) - 1  # Số lượng ma trận

    # Duyệt qua độ dài của dãy ma trận từ 2 đến n
    for length in range(2, n + 1):
        # Duyệt qua từng đoạn con có độ dài length trong dãy ma trận
        for i in range(1, n - length + 2):
            print(f"Với d = {length - 1}, ", end="")
            j = i + length - 1
            dp[i][j] = sys.maxsize
            print(f"F[{i}, {j}] = min(", end="")
            # Duyệt qua từng điểm cắt k để tìm phép nhân tối thiểu
            tam = []
            for k in range(i, j):
                # Tính số phép toán nhân cho phép nhân 2 dãy con
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                tam.append(cost)
                print(f"F[{i}, {k}] + F[{k + 1}, {j}] + {dims[i - 1]} * {dims[k]} * {dims[j]}", end="")
                if k != j - 1:
                    print(", ", end="\n")
                else:
                    print(")", end="")
                # Cập nhật số phép toán nhân tối thiểu
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    bracket[i][j] = k  # Lưu vị trí của phép nhân tối ưu
            print(" = min(", end="")
            for idx, val in enumerate(tam):
                if idx == len(tam) - 1:
                    print(val, end="")
                else:
                    print(f"{val}, ", end="")
            print(f") = {dp[i][j]}\n")
    # Trả về số lượng phép toán nhân tối thiểu cần thiết
    return dp[1][n]

# Hàm in ra cách nhóm ma trận tối ưu
def printOptimalParenthesis(bracket, dims, i, j):
    if i == j:
        print(dims[i - 1], end="")
    else:
        print("(", end="")
        printOptimalParenthesis(bracket, dims, i, bracket[i][j])
        print(", ", end="")
        printOptimalParenthesis(bracket, dims, bracket[i][j] + 1, j)
        print(")", end="")

# Hàm in ra mảng số lượng phép toán tối thiểu
def printMinimumOperations(dp):
    n = len(dp) - 1
    print("Số lượng phép toán nhân tối thiểu cho các đoạn con:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i <= j:
                print(dp[i][j], end="\t")
            else:
                print("0", end="\t")
        print()

def printBracketMatrix(bracket, n):
    print("Ma trận bracket:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(bracket[i][j], end="\t")
        print()

def main():
    dims = [20, 2, 30, 12, 8]  # Kích thước của các ma trận
    n = len(dims) - 1  # Số lượng ma trận
    bracket = [[0] * (n + 1) for _ in range(n + 1)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    minOperations = minMatrixMultiplications(dims, bracket, dp)
    print("Số lượng phép toán nhân tối thiểu:", minOperations)

    printMinimumOperations(dp)
    printBracketMatrix(bracket, n)

    print("Cách nhóm ma trận tối ưu: ", end="")
    printOptimalParenthesis(bracket, dims, 1, n)
    print()

if __name__ == "__main__":
    main()

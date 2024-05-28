def print_table(L, X, Y):
    m = len(X)
    n = len(Y)
    
    # Print header
    print("   ", end="")
    for j in range(n + 1):
        if j == 0:
            print("  ", end="")
        else:
            print(Y[j - 1], end=" ")
    print()
    
    for i in range(m + 1):
        if i == 0:
            print(" ", end=" ")
        else:
            print(X[i - 1], end=" ")
        for j in range(n + 1):
            print(L[i][j], end=" ")
        print()
    print()

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Khởi tạo bảng lưu trữ
    L = [[0] * (n + 1) for _ in range(m + 1)]

    print("Bảng khởi tạo:")
    print_table(L, X, Y)

    # Xây dựng bảng L
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
        print(f"Bảng sau khi cập nhật hàng {i}:")
        print_table(L, X, Y)

    # Truy ngược lại để tìm LCS
    index = L[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""

    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs[:-1])

# Ví dụ sử dụng
X = "AGGTAB"
Y = "GXTXAYB"
print("Chuỗi X:", X)
print("Chuỗi Y:", Y)
print("Các bước thực hiện:\n")
lcs_result = lcs(X, Y)
print("Chuỗi con chung dài nhất là:", lcs_result)

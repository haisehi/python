def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    # dp[i][j] sẽ lưu độ dài của dãy con chung dài nhất giữa X[:i] và Y[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Tính độ dài của dãy con chung dài nhất
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # In ra ma trận dp
    print("   ", " ".join(Y))
    print_matrix([[" "] + [char for char in Y]] + [[X[i - 1]] + row[1:] for i, row in enumerate(dp)])
    
    # Truy vết để tìm dãy con chung
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Cập nhật điều kiện
            i -= 1
        else:
            j -= 1

    return ''.join(lcs[::-1])  # Lật ngược dãy để đảm bảo đúng thứ tự

# Ví dụ
X = "ABCBDAB"
Y = "BDCABA"
print("Chuỗi X:", X)
print("Chuỗi Y:", Y)
print("Dãy con chung dài nhất:", longest_common_subsequence(X, Y))
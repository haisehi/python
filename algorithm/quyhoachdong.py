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
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

# Ví dụ
#X = "ABCB DAB"
#Y = "BDCAB A"
print("Nhập chuỗi 1")
X = input()
print("nhập chuỗi 2")
Y = input()
print("Chuỗi X:", X)
print("Chuỗi Y:", Y)
print("Dãy con chung dài nhất:", longest_common_subsequence(X, Y))

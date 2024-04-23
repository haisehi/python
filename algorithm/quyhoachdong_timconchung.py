#quy hoach dong: tim day con chung
def find_all_LCS(s1, s2, m, n, L):
    result = []

    if m == 0 or n == 0:
        result.append("")  # Trường hợp cả hai chuỗi đều rỗng
        return result
    if s1[m - 1] == s2[n - 1]:
        temp = find_all_LCS(s1, s2, m - 1, n - 1, L)
        for string in temp:
            result.append(string + s1[m - 1])
    else:
        if L[m - 1][n] >= L[m][n - 1]:
            result = find_all_LCS(s1, s2, m - 1, n, L)
        if L[m][n - 1] >= L[m - 1][n]:
            temp = find_all_LCS(s1, s2, m, n - 1, L)
            result.extend(temp)

    return result


def find_LCS(s1, s2):
    m = len(s1)
    n = len(s2)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                print(max(L[i - 1][j - 1], L[0][0]) + 1, end=" ")
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                print(max(L[i - 1][j], L[i][j - 1]), end=" ")
        print()

    return find_all_LCS(s1, s2, m, n, L)


if __name__ == "__main__":
    s1 = input("Nhập xâu s1: ")
    s2 = input("Nhập xâu s2: ")

    result = find_LCS(s1, s2)

    print("Các xâu con chung dài nhất của s1 và s2 là:")
    for string in result:
        print(string)

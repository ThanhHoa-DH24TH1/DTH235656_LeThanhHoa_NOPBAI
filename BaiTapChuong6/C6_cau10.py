# Hàm nhập ma trận
def nhap_ma_tran(ten):
    m = int(input(f"Nhập số hàng của ma trận {ten}: "))
    n = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    M = []
    for i in range(m):
        hang = []
        for j in range(n):
            x = float(input(f"{ten}[{i}][{j}] = "))
            hang.append(x)
        M.append(hang)
    return M

# Hàm cộng 2 ma trận
def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = []
    for i in range(m):
        hang = []
        for j in range(n):
            hang.append(A[i][j] + B[i][j])
        C.append(hang)
    return C

# Hàm hoán vị ma trận
def hoan_vi(M):
    m = len(M)
    n = len(M[0])
    T = []
    for j in range(n):
        hang = []
        for i in range(m):
            hang.append(M[i][j])
        T.append(hang)
    return T

# Hàm in ma trận cho đẹp
def in_ma_tran(M, ten="Matrix"):
    print(f"\n{ten}:")
    for hang in M:
        print(hang)

# --- Chương trình chính ---
A = nhap_ma_tran("A")
B = nhap_ma_tran("B")

C = cong_ma_tran(A, B)
A_T = hoan_vi(A)
B_T = hoan_vi(B)

# Xuất kết quả
in_ma_tran(A, "Ma trận A")
in_ma_tran(B, "Ma trận B")
in_ma_tran(C, "A + B")
in_ma_tran(A_T, "A chuyển vị (Aᵀ)")
in_ma_tran(B_T, "B chuyển vị (Bᵀ)")
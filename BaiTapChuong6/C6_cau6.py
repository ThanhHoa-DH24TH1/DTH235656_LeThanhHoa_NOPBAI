import random

def TaoList(N):
    lst = random.sample(range(0, 1000), N)  # lấy N số ngẫu nhiên trong [0, 999] không trùng nhau
    return lst
print("Nhập số phần tử:")
n=int(input())
print("List sau khi tạo ngẫu nhiên là:")
print(TaoList(n))
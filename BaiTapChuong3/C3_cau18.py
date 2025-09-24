# Vẽ hình tam giác vuông cân bằng dấu *
n = int(input("Nhập chiều cao n: "))
for i in range(1, n+1):
    print("* " * i)
# Vẽ hình tam giác vuông cân ngược bằng dấu *
n = int(input("Nhập chiều cao n: "))
for i in range(n, 0, -1):
    print("* " * i)
# Vẽ hình tam giác cân bằng dấu *
n = int(input("Nhập chiều cao n: "))
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)
# Vẽ hình chữ nhật rỗng bằng dấu *
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
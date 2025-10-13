import math

# Yêu cầu người dùng nhập tọa độ của hai điểm A và B
print("--- Nhập tọa độ điểm A ---")
try:
    x_A = float(input("Nhập hoành độ (x_A): "))
    y_A = float(input("Nhập tung độ (y_A): "))
except ValueError:
    print("Lỗi: Vui lòng nhập giá trị số hợp lệ.")
    # Kết thúc chương trình nếu nhập không hợp lệ
    exit() 

print("\n--- Nhập tọa độ điểm B ---")
try:
    x_B = float(input("Nhập hoành độ (x_B): "))
    y_B = float(input("Nhập tung độ (y_B): "))
except ValueError:
    print("Lỗi: Vui lòng nhập giá trị số hợp lệ.")
    exit()

# Công thức tính độ dài đoạn thẳng AB:
# |AB| = sqrt((x_B - x_A)^2 + (y_B - y_A)^2)

# 1. Tính bình phương hiệu các hoành độ và tung độ
delta_x_squared = (x_B - x_A)**2
delta_y_squared = (y_B - y_A)**2

# 2. Tính tổng bình phương
sum_of_squares = delta_x_squared + delta_y_squared

# 3. Tính căn bậc hai để tìm độ dài (sử dụng math.sqrt)
do_dai_AB = math.sqrt(sum_of_squares)

# Xuất kết quả
print("\n-----------------------------")
print(f"Tọa độ điểm A: ({x_A}, {y_A})")
print(f"Tọa độ điểm B: ({x_B}, {y_B})")
print(f"Độ dài đoạn thẳng AB là: {do_dai_AB}")
print("-----------------------------")

# 1. Nhập một chuỗi:
name = input("Nhập tên của bạn: ")
print("Tên của bạn là:", name)

# 2. Nhập một số nguyên:
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn là:", age)

# 3. Nhập một số thực:
score = float(input("Nhập điểm số: "))
print("Điểm số là:", score)

# 4. Nhập nhiều giá trị trên một dòng (dùng split):
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
print("Số thứ nhất:", a)
print("Số thứ hai:", b)

# 5. Nhập nhiều số và chuyển sang kiểu số nguyên:
numbers = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
print("Danh sách số vừa nhập:", numbers)
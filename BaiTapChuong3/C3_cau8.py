a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
op = input("Nhập phép toán (+, -, *, /): ")

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = "Lỗi: Không thể chia cho 0"
else:
    result = "Phép toán không hợp lệ!"

print("Kết quả:", result)
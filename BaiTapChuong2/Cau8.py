# Các loại lỗi khi lập trình Python:
# 1. Lỗi cú pháp (SyntaxError): Vi phạm quy tắc cú pháp của Python.
#    Ví dụ: print("Hello'  # thiếu dấu ngoặc kép

# 2. Lỗi khi chạy (RuntimeError): Xảy ra khi chương trình đang thực thi.
#    Ví dụ: chia cho 0, truy cập phần tử không tồn tại trong danh sách.

# 3. Lỗi logic: Chương trình chạy nhưng cho kết quả sai do sai về mặt tư duy.

# Cách bắt lỗi trong Python: sử dụng khối try-except

try:
    # Đoạn mã có thể gây lỗi
    x = int(input("Nhập một số: "))
    y = 10 / x
    print("Kết quả:", y)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0.")
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên.")
except Exception as e:
    print("Lỗi khác:", e)
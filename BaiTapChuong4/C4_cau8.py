import math

def calculate_log_base_a(x, a):
    """
    Tính logarit cơ số a của x (log_a x) sử dụng công thức đổi cơ số:
    log_a x = ln(x) / ln(a)
    """
    
    # 1. Kiểm tra các điều kiện ràng buộc
    if x <= 0:
        return f"Lỗi: x phải lớn hơn 0 (x > 0). Giá trị x = {x} không hợp lệ."
    
    if a <= 0:
        return f"Lỗi: Cơ số a phải lớn hơn 0 (a > 0). Giá trị a = {a} không hợp lệ."
    
    if a == 1:
        return f"Lỗi: Cơ số a phải khác 1 (a != 1). Giá trị a = {a} không hợp lệ."

    # 2. Tính toán theo công thức đổi cơ số
    try:
        # math.log(x) tính logarit tự nhiên (ln x)
        ln_x = math.log(x)
        ln_a = math.log(a)
        
        result = ln_x / ln_a
        return result
        
    except Exception as e:
        # Xử lý các lỗi tính toán khác (ví dụ: lỗi chia cho 0, mặc dù đã được kiểm tra ở trên)
        return f"Đã xảy ra lỗi trong quá trình tính toán: {e}"

# --- Phần nhập liệu và xuất kết quả ---

print("--- Chương trình tính logarit cơ số a của x (log_a x) ---")

while True:
    try:
        # Nhập giá trị x
        x_input = float(input("Nhập giá trị x (số thực, x > 0): "))
        
        # Nhập cơ số a
        a_input = float(input("Nhập cơ số a (số thực, a > 0 và a != 1): "))
        
        # Gọi hàm tính toán
        ket_qua = calculate_log_base_a(x_input, a_input)
        
        # Xuất kết quả
        if isinstance(ket_qua, str):
            # Nếu kết quả là chuỗi (có nghĩa là có lỗi xảy ra)
            print(f"\nKẾT QUẢ: {ket_qua}")
        else:
            # Nếu kết quả là số
            print("\n-------------------------------------------")
            print(f"Giá trị tính được của log_{a_input} {x_input} là:")
            print(f"log_{a_input} {x_input} = {ket_qua}")
            print(f"(Làm tròn 4 chữ số thập phân: {ket_qua:.4f})")
            print("-------------------------------------------")
            
        break # Thoát vòng lặp nếu nhập liệu hợp lệ và tính toán xong

    except ValueError:
        print("\nLỗi nhập liệu: Vui lòng đảm bảo bạn nhập số thực hợp lệ cho x và a.")
        print("Vui lòng thử lại.\n")
    except Exception as e:
        print(f"\nĐã xảy ra lỗi không xác định: {e}")
        break
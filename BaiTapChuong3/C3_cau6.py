def read_number(n):
    # Danh sách các số đơn vị và chục
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    # Xử lý khi n là số có 2 chữ số
    if n < 10:
        return units[n]  # Nếu số là 1 chữ số (n = 0,1,...9)
    elif 10 <= n < 20:
        # Nếu số từ 10 đến 19, đặc biệt là "mười"
        if n == 10:
            return "mười"
        else:
            return "mười " + units[n % 10]  # Ví dụ: 15 -> mười năm
    else:
        tens_place = n // 10  # Lấy phần chục
        ones_place = n % 10   # Lấy phần đơn vị
        
        # Xử lý phần chục và phần đơn vị
        if ones_place == 0:
            return tens[tens_place]  # Nếu phần đơn vị là 0, chỉ cần phần chục
        else:
            return tens[tens_place] + " " + units[ones_place]  # Kết hợp phần chục và phần đơn vị

# Nhập số n từ người dùng
n = int(input("Nhập một số n có tối đa 2 chữ số: "))
print(f"Số {n} đọc là: {read_number(n)}")

def phan_tich_chuoi(chuoi):

    # Khởi tạo bộ đếm
    dem_in_hoa = 0
    dem_in_thuong = 0
    dem_chu_so = 0
    dem_khoang_trang = 0
    dem_nguyen_am = 0
    dem_phu_am = 0
    
    # Định nghĩa các tập hợp để kiểm tra Nguyên Âm và Phụ Âm nhanh chóng
    NGUYEN_AM = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    # Trong tiếng Việt có thêm các nguyên âm có dấu, tùy vào yêu cầu chi tiết 
    # ta có thể thêm vào, ví dụ: 'ă', 'â', 'ê', 'ô', 'ơ', 'ư',... 
    # Ở đây ta xét Nguyên Âm cơ bản (không dấu)
    
    # Duyệt qua từng ký tự trong chuỗi
    for ky_tu in chuoi:
        if ky_tu.isupper():
            dem_in_hoa += 1
            # Kiểm tra Nguyên Âm/Phụ Âm (chỉ xét chữ cái)
            if ky_tu in NGUYEN_AM:
                dem_nguyen_am += 1
            elif ky_tu.isalpha():
                dem_phu_am += 1

        elif ky_tu.islower():
            dem_in_thuong += 1
            # Kiểm tra Nguyên Âm/Phụ Âm (chỉ xét chữ cái)
            if ky_tu in NGUYEN_AM:
                dem_nguyen_am += 1
            elif ky_tu.isalpha():
                dem_phu_am += 1

        elif ky_tu.isdigit():
            dem_chu_so += 1
        
        elif ky_tu.isspace():
            dem_khoang_trang += 1
    
    # Tổng số ký tự
    tong_ky_tu = len(chuoi)
    # Tổng các ký tự đã đếm (Hoa, Thường, Số, Khoảng trắng)
    tong_da_dem = dem_in_hoa + dem_in_thuong + dem_chu_so + dem_khoang_trang
    # Ký tự đặc biệt = Tổng ký tự - Ký tự đã đếm (là chữ cái, số, hoặc khoảng trắng)
    dem_ky_tu_dac_biet = tong_ky_tu - tong_da_dem
    
    # Trả về kết quả dưới dạng từ điển
    ket_qua = {
        "IN HOA": dem_in_hoa,
        "IN THƯỜNG": dem_in_thuong,
        "CHỮ SỐ": dem_chu_so,
        "KHOẢNG TRẮNG": dem_khoang_trang,
        "KÝ TỰ ĐẶC BIỆT": dem_ky_tu_dac_biet,
        "NGUYÊN ÂM": dem_nguyen_am,
        "PHỤ ÂM": dem_phu_am,
    }
    return ket_qua

# --- Chương trình chính ---
print("--- CHƯƠNG TRÌNH PHÂN TÍCH CHUỖI ---")
# Nhập chuỗi từ người dùng
chuoi_dau_vao = input("Vui lòng nhập một chuỗi bất kỳ: ")

# Gọi hàm phân tích
ket_qua_phan_tich = phan_tich_chuoi(chuoi_dau_vao)

# Xuất kết quả
print("\n--- KẾT QUẢ PHÂN TÍCH CHUỖI ---")
print(f"Chuỗi đầu vào: \"{chuoi_dau_vao}\"")
print(f"Tổng số ký tự: {len(chuoi_dau_vao)}")
print("-" * 30)

# Xuất các kết quả đếm theo yêu cầu
print(f"Số chữ IN HOA:             {ket_qua_phan_tich['IN HOA']}")
print(f"Số chữ in thường:          {ket_qua_phan_tich['IN THƯỜNG']}")
print(f"Số chữ là chữ số:          {ket_qua_phan_tich['CHỮ SỐ']}")
print(f"Số chữ là khoảng trắng:    {ket_qua_phan_tich['KHOẢNG TRẮNG']}")
print(f"Số chữ là ký tự đặc biệt:  {ket_qua_phan_tich['KÝ TỰ ĐẶC BIỆT']}")
print("-" * 30)
print(f"Số chữ là Nguyên Âm:       {ket_qua_phan_tich['NGUYÊN ÂM']}")
print(f"Số chữ là Phụ âm:          {ket_qua_phan_tich['PHỤ ÂM']}")

#
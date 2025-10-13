def toi_uu_chuoi_danh_tu(chuoi_dau_vao):
    """
    Tối ưu chuỗi danh từ:
    1. Loại bỏ khoảng trắng dư thừa ở đầu và cuối (dùng .strip()).
    2. Đảm bảo các từ cách nhau bằng một khoảng trắng duy nhất (dùng .split() và ' '.join()).
    3. Viết hoa ký tự đầu tiên của mỗi từ (dùng .title()).
    """
    # 1. Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    # 2. Tách chuỗi thành danh sách các từ. .split() tự động xử lý nhiều khoảng trắng.
    danh_sach_tu = chuoi_dau_vao.strip().split()
    
    # 3. Nối các từ lại với một khoảng trắng duy nhất
    chuoi_da_noi = ' '.join(danh_sach_tu)
    
    # 4. Viết hoa ký tự đầu tiên của mỗi từ (chuyển sang Title Case)
    chuoi_toi_uu = chuoi_da_noi.title()
    
    return chuoi_toi_uu

# --- Chương trình chính ---
# Ví dụ 1: Input của bạn
input_1 = " lê THAnh      hòA"
output_1 = toi_uu_chuoi_danh_tu(input_1)

print(f"Input: \"{input_1}\"")
print(f"Output: \"{output_1}\"")
print("-" * 30)

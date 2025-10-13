import os

def lay_ten_tep_day_du(duong_dan_file):
    """
    Trích xuất tên tệp (ví dụ: 'muabui.mp3') từ đường dẫn đầy đủ.

    Tham số:
        duong_dan_file (str): Chuỗi đường dẫn tệp tin bất kỳ.

    Trả về:
        str: Tên tệp đầy đủ.
    """
    # os.path.basename() là phương pháp chuẩn, hoạt động trên mọi hệ điều hành.
    ten_tep_day_du = os.path.basename(duong_dan_file)
    return ten_tep_day_du

def lay_ten_tep_khong_mo_rong(duong_dan_file):
    """
    Trích xuất tên tệp (ví dụ: 'muabui') mà không có phần mở rộng.

    Tham số:
        duong_dan_file (str): Chuỗi đường dẫn tệp tin bất kỳ.

    Trả về:
        str: Tên tệp không có phần mở rộng.
    """
    # 1. Lấy tên tệp đầy đủ (ví dụ: 'muabui.mp3')
    ten_tep_day_du = os.path.basename(duong_dan_file)
    
    # 2. Tách tên tệp thành (tên_gốc, phần_mở_rộng). 
    #    os.path.splitext() trả về một tuple.
    ten_goc, _ = os.path.splitext(ten_tep_day_du)
    
    # Ta chỉ cần phần tên gốc (ten_goc), bỏ qua phần mở rộng (dấu gạch dưới '_').
    return ten_goc
# Ví dụ 1: Đường dẫn Windows
path_win = r"d:\music\nhac\WhatMakeYourBeautiful.mp3"

print(f"Đường dẫn 1: {path_win}")
print(f"  - Tên tệp đầy đủ: {lay_ten_tep_day_du(path_win)}")             # Output: muabui.mp3
print(f"  - Tên tệp không mở rộng: {lay_ten_tep_khong_mo_rong(path_win)}") # Output: muabui

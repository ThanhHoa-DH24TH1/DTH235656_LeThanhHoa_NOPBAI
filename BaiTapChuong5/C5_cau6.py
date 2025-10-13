import re

def NegativeNumberInStrings(chuoi_dau_vao):
    """
    Tìm và xuất ra tất cả các số nguyên âm có trong chuỗi.

    Tham số:
        chuoi_dau_vao (str): Chuỗi bất kỳ để tìm kiếm.

    Trả về:
        list: Một danh sách chứa các chuỗi số nguyên âm tìm được.
    """
    # Biểu thức chính quy để tìm số nguyên âm:
    # 1. Bắt đầu bằng dấu gạch ngang (-)
    # 2. Tiếp theo là ít nhất một chữ số (\d+)
    # 3. Đảm bảo số âm này KHÔNG phải là một phần của số dương
    #    (ví dụ: không lấy '-12' từ '5-12')
    #    Ta dùng negative lookbehind (?<!\d) để đảm bảo trước dấu '-' không phải là chữ số.
    #    Tuy nhiên, cách đơn giản và phổ biến hơn là tìm kiếm bất kỳ dấu '-' nào
    #    ngay lập tức theo sau là một chữ số.
    
    # Pattern: Tìm dấu '-' theo sau là một hoặc nhiều chữ số.
    pattern = r'-\d+'
    
    # re.findall() tìm tất cả các chuỗi con khớp với pattern và trả về dưới dạng list.
    cac_so_nguyen_am = re.findall(pattern, chuoi_dau_vao)
    
    return cac_so_nguyen_am

# --- Ví dụ minh họa ---
chuoi_test_1 = "abc-5xyz-12k9l--p"
chuoi_test_2 = "Giá trị: -99, Nhiệt độ: -3.5, Mã số: 100"
chuoi_test_3 = "Chỉ có -một dấu gạch ngang."

ket_qua_1 = NegativeNumberInStrings(chuoi_test_1)
ket_qua_2 = NegativeNumberInStrings(chuoi_test_2)
ket_qua_3 = NegativeNumberInStrings(chuoi_test_3)

print(f"Chuỗi: \"{chuoi_test_1}\"")
print(f"Các số nguyên âm: {ket_qua_1}")
# Expected Output: ['-5', '-12']

print("-" * 30)
print(f"Chuỗi: \"{chuoi_test_2}\"")
print(f"Các số nguyên âm: {ket_qua_2}")
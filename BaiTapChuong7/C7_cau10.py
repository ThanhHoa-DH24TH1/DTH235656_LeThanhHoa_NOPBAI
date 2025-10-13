import json

# =============================
# 🔹 1. Cấu trúc dữ liệu
# =============================

ds_lop = []
ds_sv = []

# =============================
# 🔹 2. Các hàm xử lý JSON
# =============================

def luu_file():
    data = {"lop": ds_lop, "sinhvien": ds_sv}
    with open("sinhvien.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("💾 Dữ liệu đã được lưu vào file sinhvien.json")

def doc_file():
    global ds_lop, ds_sv
    try:
        with open("sinhvien.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            ds_lop = data.get("lop", [])
            ds_sv = data.get("sinhvien", [])
        print("📂 Đọc dữ liệu thành công!")
    except FileNotFoundError:
        print("⚠️ Chưa có file dữ liệu. Sẽ tạo mới khi lưu.")

# =============================
# 🔹 3. Các chức năng chính
# =============================

def them_lop():
    ma = input("Nhập mã lớp: ")
    ten = input("Nhập tên lớp: ")
    ds_lop.append({"ma_lop": ma, "ten_lop": ten})
    print("✅ Đã thêm lớp thành công!")

def them_sv():
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    nam = input("Nhập năm sinh: ")
    ma_lop = input("Nhập mã lớp sinh viên thuộc về: ")
    ds_sv.append({"ma_sv": ma, "ten_sv": ten, "nam_sinh": nam, "ma_lop": ma_lop})
    print("✅ Đã thêm sinh viên thành công!")

def sua_sv():
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in ds_sv:
        if sv["ma_sv"] == ma:
            sv["ten_sv"] = input("Tên mới: ")
            sv["nam_sinh"] = input("Năm sinh mới: ")
            sv["ma_lop"] = input("Mã lớp mới: ")
            print("✏️ Đã cập nhật thông tin sinh viên!")
            return
    print("❌ Không tìm thấy sinh viên!")

def xoa_sv():
    ma = input("Nhập mã sinh viên cần xóa: ")
    for sv in ds_sv:
        if sv["ma_sv"] == ma:
            ds_sv.remove(sv)
            print("🗑️ Đã xóa sinh viên!")
            return
    print("❌ Không tìm thấy sinh viên!")

def tim_kiem():
    tu_khoa = input("Nhập tên sinh viên cần tìm: ").lower()
    kq = [sv for sv in ds_sv if tu_khoa in sv["ten_sv"].lower()]
    if kq:
        print("🔍 Kết quả tìm kiếm:")
        for sv in kq:
            print(f"{sv['ma_sv']} - {sv['ten_sv']} ({sv['nam_sinh']}) - Lớp: {sv['ma_lop']}")
    else:
        print("❌ Không tìm thấy sinh viên nào!")

def sap_xep():
    ds_sv.sort(key=lambda x: x["ten_sv"])
    print("📊 Đã sắp xếp danh sách sinh viên theo tên!")

def hien_thi():
    print("=== DANH SÁCH SINH VIÊN ===")
    for sv in ds_sv:
        print(f"{sv['ma_sv']} - {sv['ten_sv']} - {sv['nam_sinh']} - {sv['ma_lop']}")

# =============================
# 🔹 4. Menu chương trình
# =============================

def menu():
    doc_file()
    while True:
        print("\n=== QUẢN LÝ SINH VIÊN (JSON) ===")
        print("1. Thêm lớp")
        print("2. Thêm sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp sinh viên theo tên")
        print("7. Hiển thị danh sách sinh viên")
        print("8. Lưu file JSON")
        print("0. Thoát")

        chon = input("👉 Chọn chức năng: ")

        if chon == "1": them_lop()
        elif chon == "2": them_sv()
        elif chon == "3": sua_sv()
        elif chon == "4": xoa_sv()
        elif chon == "5": tim_kiem()
        elif chon == "6": sap_xep()
        elif chon == "7": hien_thi()
        elif chon == "8": luu_file()
        elif chon == "0":
            luu_file()
            print("👋 Thoát chương trình!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng nhập lại.")

# =============================
# 🔹 5. Gọi menu
# =============================
menu()

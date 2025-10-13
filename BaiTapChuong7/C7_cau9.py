import os

# =============================
# 1️ Khai báo lớp DanhMuc và SanPham
# =============================

class DanhMuc:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class SanPham:
    def __init__(self, ma, ten, don_gia, ma_danh_muc):
        self.ma = ma
        self.ten = ten
        self.don_gia = don_gia
        self.ma_danh_muc = ma_danh_muc


# =============================
# 2️ Dữ liệu lưu trong list
# =============================
danh_mucs = []
san_phams = []

# =============================
# 3️ Chức năng
# =============================

def them_danh_muc():
    ma = input("Nhập mã danh mục: ")
    ten = input("Nhập tên danh mục: ")
    danh_mucs.append(DanhMuc(ma, ten))
    print("✅ Đã thêm danh mục.")

def them_san_pham():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    don_gia = float(input("Nhập đơn giá: "))
    ma_dm = input("Nhập mã danh mục của sản phẩm: ")
    san_phams.append(SanPham(ma, ten, don_gia, ma_dm))
    print("✅ Đã thêm sản phẩm.")

def hien_thi():
    print("\n📋 DANH SÁCH SẢN PHẨM:")
    for sp in san_phams:
        dm = next((d.ten for d in danh_mucs if d.ma == sp.ma_danh_muc), "Không rõ")
        print(f"{sp.ma:10} | {sp.ten:20} | {sp.don_gia:10,.0f} | Danh mục: {dm}")

def sua_san_pham():
    ma = input("Nhập mã sản phẩm cần sửa: ")
    sp = next((s for s in san_phams if s.ma == ma), None)
    if sp:
        sp.ten = input("Tên mới: ") or sp.ten
        sp.don_gia = float(input("Đơn giá mới: ") or sp.don_gia)
        sp.ma_danh_muc = input("Mã danh mục mới: ") or sp.ma_danh_muc
        print("✅ Đã sửa thành công.")
    else:
        print("❌ Không tìm thấy sản phẩm.")

def xoa_san_pham():
    ma = input("Nhập mã sản phẩm cần xóa: ")
    global san_phams
    san_phams = [s for s in san_phams if s.ma != ma]
    print("✅ Đã xóa sản phẩm.")

def tim_kiem():
    tu_khoa = input("Nhập từ khóa tìm kiếm: ").lower()
    ket_qua = [s for s in san_phams if tu_khoa in s.ten.lower()]
    print(f"\n🔍 Kết quả tìm kiếm ({len(ket_qua)}):")
    for s in ket_qua:
        print(f"{s.ma} - {s.ten} - {s.don_gia}")

def sap_xep():
    san_phams.sort(key=lambda s: s.don_gia)
    print("✅ Đã sắp xếp sản phẩm theo đơn giá tăng dần.")

# =============================
# 4️ Lưu và đọc file
# =============================

def luu_file():
    with open("sanpham.txt", "w", encoding="utf-8") as f:
        for dm in danh_mucs:
            f.write(f"DANHMUC;{dm.ma};{dm.ten}\n")
        for sp in san_phams:
            f.write(f"SANPHAM;{sp.ma};{sp.ten};{sp.don_gia};{sp.ma_danh_muc}\n")
    print("💾 Đã lưu dữ liệu vào file sanpham.txt")

def doc_file():
    if not os.path.exists("sanpham.txt"):
        print("⚠️ Chưa có file dữ liệu.")
        return

    danh_mucs.clear()
    san_phams.clear()

    with open("sanpham.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if parts[0] == "DANHMUC":
                danh_mucs.append(DanhMuc(parts[1], parts[2]))
            elif parts[0] == "SANPHAM":
                san_phams.append(SanPham(parts[1], parts[2], float(parts[3]), parts[4]))
    print("Đã đọc dữ liệu từ file sanpham.txt")

# =============================
# 5️ Menu chính
# =============================

def menu():
    while True:
        print("\n===== QUẢN LÝ SẢN PHẨM =====")
        print("1. Thêm danh mục")
        print("2. Thêm sản phẩm")
        print("3. Hiển thị danh sách")
        print("4. Sửa sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Tìm kiếm sản phẩm")
        print("7. Sắp xếp theo đơn giá")
        print("8. Lưu file")
        print("9. Đọc file")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1": them_danh_muc()
        elif chon == "2": them_san_pham()
        elif chon == "3": hien_thi()
        elif chon == "4": sua_san_pham()
        elif chon == "5": xoa_san_pham()
        elif chon == "6": tim_kiem()
        elif chon == "7": sap_xep()
        elif chon == "8": luu_file()
        elif chon == "9": doc_file()
        elif chon == "0": 
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# =============================
# 6️ Chạy chương trình
# =============================
if __name__ == "__main__":
    menu()

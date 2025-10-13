import xml.etree.ElementTree as ET

# -----------------------------
# Đọc file XML nhóm thiết bị
# -----------------------------
def doc_nhom():
    tree = ET.parse("nhomthietbi.xml")
    root = tree.getroot()
    nhoms = []
    for nhom in root.findall("nhom"):
        ma = nhom.find("ma").text
        ten = nhom.find("ten").text
        nhoms.append({"ma": ma, "ten": ten})
    return nhoms

# -----------------------------
# Đọc file XML thiết bị
# -----------------------------
def doc_thietbi():
    tree = ET.parse("thietbi.xml")
    root = tree.getroot()
    thietbis = []
    for tb in root.findall("thietbi"):
        manhom = tb.get("manhom")
        ma = tb.find("ma").text
        ten = tb.find("ten").text
        thietbis.append({"manhom": manhom, "ma": ma, "ten": ten})
    return thietbis

# -----------------------------
# Hiển thị danh sách nhóm
# -----------------------------
def hien_thi_nhom():
    nhoms = doc_nhom()
    print("\n📂 DANH SÁCH NHÓM THIẾT BỊ:")
    for n in nhoms:
        print(f"- Mã: {n['ma']}, Tên: {n['ten']}")

# -----------------------------
# Hiển thị danh sách thiết bị
# -----------------------------
def hien_thi_thietbi():
    thietbis = doc_thietbi()
    print("\n🔧 DANH SÁCH THIẾT BỊ:")
    for tb in thietbis:
        print(f"- Mã: {tb['ma']}, Tên: {tb['ten']}, Nhóm: {tb['manhom']}")

# -----------------------------
# Lọc thiết bị theo nhóm
# -----------------------------
def loc_theo_nhom():
    manhom = input("👉 Nhập mã nhóm cần lọc (vd: n1, n2, n3): ")
    thietbis = doc_thietbi()
    print(f"\n🔎 Thiết bị thuộc nhóm {manhom}:")
    for tb in thietbis:
        if tb["manhom"] == manhom:
            print(f"- {tb['ma']}: {tb['ten']}")

# -----------------------------
# Tìm nhóm có nhiều thiết bị nhất
# -----------------------------
def nhom_nhieu_thietbi():
    nhoms = doc_nhom()
    thietbis = doc_thietbi()
    thongke = {}

    for tb in thietbis:
        thongke[tb["manhom"]] = thongke.get(tb["manhom"], 0) + 1

    max_so = max(thongke.values())
    print("\n🏆 NHÓM CÓ NHIỀU THIẾT BỊ NHẤT:")
    for ma, sl in thongke.items():
        if sl == max_so:
            ten_nhom = next((n["ten"] for n in nhoms if n["ma"] == ma), "")
            print(f"- {ten_nhom} ({ma}) có {sl} thiết bị")

# -----------------------------
# MENU CHÍNH
# -----------------------------
def menu():
    while True:
        print("\n=== QUẢN LÝ THIẾT BỊ (XML) ===")
        print("1. Hiển thị danh sách nhóm thiết bị")
        print("2. Hiển thị toàn bộ thiết bị")
        print("3. Lọc thiết bị theo nhóm")
        print("4. Tìm nhóm có nhiều thiết bị nhất")
        print("0. Thoát")

        chon = input("👉 Chọn chức năng: ")
        if chon == "1":
            hien_thi_nhom()
        elif chon == "2":
            hien_thi_thietbi()
        elif chon == "3":
            loc_theo_nhom()
        elif chon == "4":
            nhom_nhieu_thietbi()
        elif chon == "0":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# -----------------------------
if __name__ == "__main__":
    menu()

import csv
import random

FILE_NAME = "dulieu.csv"

# -----------------------------------------
# 1️⃣ Tạo file CSV chứa 10 dòng, mỗi dòng 10 số ngẫu nhiên
# -----------------------------------------
def tao_file_csv():
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        for _ in range(10):  # 10 dòng
            row = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(row)
    print(f"✅ Đã tạo file CSV '{FILE_NAME}' với 10 dòng dữ liệu ngẫu nhiên.")

# -----------------------------------------
# 2️⃣ Đọc file CSV và tính tổng các giá trị mỗi dòng
# -----------------------------------------
def doc_va_tinh_tong():
    with open(FILE_NAME, newline="") as f:
        reader = csv.reader(f, delimiter=";")
        print("\n📘 Tổng giá trị trên mỗi dòng:")
        dong = 1
        for row in reader:
            # Chuyển các phần tử từ chuỗi → số nguyên
            numbers = [int(x) for x in row if x.strip() != ""]
            tong = sum(numbers)
            print(f"Dòng {dong}: {numbers} → Tổng = {tong}")
            dong += 1

# -----------------------------------------
# 3️⃣ Chương trình chính
# -----------------------------------------
def main():
    while True:
        print("\n=== XỬ LÝ CSV FILE ===")
        print("1. Tạo file CSV ngẫu nhiên")
        print("2. Đọc file và tính tổng mỗi dòng")
        print("0. Thoát")
        chon = input("👉 Chọn chức năng: ")

        if chon == "1":
            tao_file_csv()
        elif chon == "2":
            doc_va_tinh_tong()
        elif chon == "0":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

# -----------------------------------------
if __name__ == "__main__":
    main()

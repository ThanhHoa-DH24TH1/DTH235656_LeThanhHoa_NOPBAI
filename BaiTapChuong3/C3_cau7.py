from datetime import datetime, timedelta

# Nhập ngày/tháng/năm
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

try:
    # Tạo đối tượng ngày
    today = datetime(year, month, day)
    # Cộng thêm 1 ngày
    next_day = today + timedelta(days=1)
    # In kết quả
    print("Ngày kế tiếp là: {}/{}/{}".format(next_day.day, next_day.month, next_day.year))
except ValueError:
    print("Ngày nhập không hợp lệ!")
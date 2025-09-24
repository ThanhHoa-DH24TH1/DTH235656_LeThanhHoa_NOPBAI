ranges = {
    "a": range(5),
    "b": range(5, 10),
    "c": range(5, 20, 3),
    "d": range(20, 5, -1),
    "e": range(20, 5, -3),
    "f": range(10, 5),
    "g": range(0),
    "h": range(10, 101, 10),
    "i": range(10, -1, -1),
    "j": range(-3, 4),
    "k": range(0, 10, 1)
}

for key, r in ranges.items():
    print(f"{key}: {list(r)}")

"""(a) range(5)

Chỉ truyền một số: mặc định start=0, step=1.

Giá trị: [0, 1, 2, 3, 4]

Bắt đầu từ 0, tăng 1, dừng trước 5.

(b) range(5, 10)

start=5, stop=10, step=1 mặc định.

Giá trị: [5, 6, 7, 8, 9]

(c) range(5, 20, 3)

Bắt đầu từ 5, tăng 3 mỗi bước, dừng trước 20.

Giá trị: [5, 8, 11, 14, 17]

(d) range(20, 5, -1)

Bắt đầu từ 20, giảm 1 mỗi bước, dừng trước 5.

Giá trị: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

(e) range(20, 5, -3)

Bắt đầu từ 20, giảm 3 mỗi bước, dừng trước 5.

Giá trị: [20, 17, 14, 11, 8]

(f) range(10, 5)

Mặc định step=1, nhưng start > stop nên không chạy được.

Giá trị: [] (rỗng)

(g) range(0)

Bắt đầu 0, stop=0, step=1.

Giá trị: [] (rỗng)

(h) range(10, 101, 10)

Bắt đầu 10, tăng 10 mỗi bước, dừng trước 101.

Giá trị: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

(i) range(10, -1, -1)

Bắt đầu 10, giảm 1 mỗi bước, dừng trước -1.

Giá trị: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

(j) range(-3, 4)

Bắt đầu -3, tăng 1 mỗi bước, dừng trước 4.

Giá trị: [-3, -2, -1, 0, 1, 2, 3]

(k) range(0, 10, 1)

Bắt đầu 0, tăng 1 mỗi bước, dừng trước 10.

Giá trị: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
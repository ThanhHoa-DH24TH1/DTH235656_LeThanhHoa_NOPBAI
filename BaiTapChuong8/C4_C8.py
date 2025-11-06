from tkinter import *

# ===== Hàm xử lý =====
def nhapAction(giatri):
    stringKQ.set(stringKQ.get() + str(giatri))

def tinhAction():
    try:
        kq = eval(stringKQ.get())
        stringKQ.set(str(kq))
    except:
        stringKQ.set("Lỗi")

def xoaAction():
    stringKQ.set("")

# ===== Giao diện =====
root = Tk()
root.title("Máy tính bỏ túi")

stringKQ = StringVar()

# Ô hiển thị
Entry(root, textvariable=stringKQ, font=('Arial', 18), justify='right', bd=5, relief=RIDGE).grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

# ===== Các nút =====

# Hàng 1: 1 2 3
for i, val in enumerate(["1", "2", "3"]):
    Button(root, text=val, font=('Arial', 15), relief=RAISED, bd=3, command=lambda v=val: nhapAction(v)).grid(row=1, column=i, sticky="nsew", padx=2, pady=2)

# Hàng 2: 4 5 6
for i, val in enumerate(["4", "5", "6"]):
    Button(root, text=val, font=('Arial', 15), relief=RAISED, bd=3, command=lambda v=val: nhapAction(v)).grid(row=2, column=i, sticky="nsew", padx=2, pady=2)

# Hàng 3: 7 8 9
for i, val in enumerate(["7", "8", "9"]):
    Button(root, text=val, font=('Arial', 15), relief=RAISED, bd=3, command=lambda v=val: nhapAction(v)).grid(row=3, column=i, sticky="nsew", padx=2, pady=2)

# Hàng 4: - 0 .
for i, val in enumerate(["-", "0", "."]):
    Button(root, text=val, font=('Arial', 15), relief=RAISED, bd=3, command=lambda v=val: nhapAction(v)).grid(row=4, column=i, sticky="nsew", padx=2, pady=2)

# Hàng 5: + - * / =
for i, val in enumerate(["+", "-", "*", "/", "="]):
    if val == "=":
        Button(root, text=val, font=('Arial', 15), bg="lightblue", relief=RAISED, bd=3, command=tinhAction).grid(row=5, column=i, sticky="nsew", padx=2, pady=2)
    else:
        Button(root, text=val, font=('Arial', 15), relief=RAISED, bd=3, command=lambda v=val: nhapAction(v)).grid(row=5, column=i, sticky="nsew", padx=2, pady=2)

# Hàng 6: Clr
Button(root, text="Clr", font=('Arial', 15), bg="lightcoral", relief=RAISED, bd=3, command=xoaAction).grid(row=6, column=0, columnspan=5, sticky="nsew", padx=2, pady=4)

# ===== Căn đều các cột & hàng =====
for i in range(5):  # 5 cột
    root.columnconfigure(i, weight=1)
for i in range(7):  # 7 hàng (0–6)
    root.rowconfigure(i, weight=1)

root.resizable(False, False)  # Không cho co kéo cửa sổ
root.mainloop()

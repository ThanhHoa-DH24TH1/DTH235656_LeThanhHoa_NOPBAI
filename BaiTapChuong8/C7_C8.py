from tkinter import *

# ======= Hàm xử lý chuyển đổi =======
def chuyen():
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

    try:
        nam_dl = int(entryNamDL.get())
        can_index = nam_dl % 10
        chi_index = nam_dl % 12
        nam_am = can[can_index] + " " + chi[chi_index]
        stringKQ.set(nam_am)
    except:
        stringKQ.set("Lỗi nhập liệu!")

# ======= Giao diện chính =======
root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")

# ======= Frame chính =======
frame = Frame(root, bg='yellow', padx=20, pady=15, relief="solid", bd=1)
frame.pack(padx=10, pady=10)

# ======= Khai báo biến =======
stringKQ = StringVar()

# ======= Nhập năm dương =======
Label(frame, text="Nhập năm dương:", font=('Arial', 12), bg='yellow').grid(row=0, column=0, sticky='w')
entryNamDL = Entry(frame, width=15, font=('Arial', 12))
entryNamDL.grid(row=0, column=1, padx=5)

Button(frame, text="Chuyển", width=8, font=('Arial', 11), bg='lightblue', command=chuyen).grid(row=1, column=1, padx=5)

# ======= Hiển thị kết quả =======
Label(frame, text="Năm âm:", font=('Arial', 12), bg='yellow').grid(row=2, column=0, pady=10, sticky='w')
Label(frame, textvariable=stringKQ, font=('Arial', 12), bg='yellow', fg='blue').grid(row=1, column=1, columnspan=2, sticky='w')

root.mainloop()

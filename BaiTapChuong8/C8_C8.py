from tkinter import *

# ======= Hàm xử lý =======
def chuyen():
    try:
        doF = float(entryF.get())
        doC = (doF - 32) * 5 / 9
        stringKQ.set(f"{doC:.2f}")
    except:
        stringKQ.set("Lỗi nhập liệu!")

# ======= Giao diện chính =======
root = Tk()
root.title("Chuyển độ F sang độ C")

# ======= Frame chính =======
frame = Frame(root, bg='yellow', padx=20, pady=15, relief="solid", bd=1)
frame.pack(padx=10, pady=10)

# ======= Biến lưu kết quả =======
stringKQ = StringVar()

# ======= Hàng 1: Nhập độ F =======
Label(frame, text="Nhập độ F", font=('Arial', 12), bg='yellow').grid(row=0, column=0, sticky='w')
entryF = Entry(frame, width=15, font=('Arial', 12), fg='red')
entryF.grid(row=0, column=1, padx=5)
Button(frame, text="Chuyển", width=8, font=('Arial', 11), bg='lightblue', command=chuyen).grid(row=1, column=1, padx=5)

# ======= Hàng 2: Hiển thị kết quả =======
Label(frame, text="Độ C", font=('Arial', 12), bg='yellow').grid(row=2, column=0, pady=10, sticky='w')
Label(frame, textvariable=stringKQ, font=('Arial', 12), bg='yellow', fg='blue').grid(row=2, column=1, columnspan=2, sticky='w')

root.mainloop()

from tkinter import *
from tkinter import messagebox

# ======= Hàm xử lý =======
def tinhBMI():
    try:
        cao = float(entryCao.get())
        nang = float(entryNang.get())
        bmi = nang / (cao * cao)
        stringBMI.set(f"{bmi:.1f}")

        # Xác định tình trạng
        if bmi < 18.5:
            tinhtrang = "Gầy"
            nguyco = "Thấp"
        elif bmi < 25:
            tinhtrang = "Bình thường"
            nguyco = "Trung bình"
        elif bmi < 30:
            tinhtrang = "Hơi Béo"
            nguyco = "Hơi hơi cao"
        else:
            tinhtrang = "Béo phì"
            nguyco = "Cao"

        stringTinhTrang.set(tinhtrang)
        stringNguyCo.set(nguyco)

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

def thoat():
    root.destroy()

# ======= Giao diện chính =======
root = Tk()
root.title("Phần mềm tính BMI")

# ======= Frame chính =======
frame = Frame(root, bg='yellow', padx=20, pady=15, relief="solid", bd=1)
frame.pack(padx=10, pady=10)

# ======= Khai báo biến =======
stringBMI = StringVar()
stringTinhTrang = StringVar()
stringNguyCo = StringVar()

# ======= Giao diện =======
Label(frame, text="Nhập chiều cao:", font=('Arial', 12), bg='yellow').grid(row=0, column=0, sticky='w')
entryCao = Entry(frame, width=15, font=('Arial', 12), fg='red')
entryCao.grid(row=0, column=1, pady=3)

Label(frame, text="Nhập cân nặng:", font=('Arial', 12), bg='yellow').grid(row=1, column=0, sticky='w')
entryNang = Entry(frame, width=15, font=('Arial', 12), fg='red')
entryNang.grid(row=1, column=1, pady=3)

Button(frame, text="Tính BMI", width=10, bg='lightblue', font=('Arial', 11), command=tinhBMI).grid(row=2, column=1, pady=5)

Label(frame, text="BMI của bạn:", font=('Arial', 12), bg='yellow').grid(row=3, column=0, sticky='w')
Entry(frame, textvariable=stringBMI, width=15, font=('Arial', 12)).grid(row=3, column=1, pady=3)

Label(frame, text="Tình trạng của bạn:", font=('Arial', 12), bg='yellow').grid(row=4, column=0, sticky='w')
Entry(frame, textvariable=stringTinhTrang, width=15, font=('Arial', 12), fg='red').grid(row=4, column=1, pady=3)

Label(frame, text="Nguy cơ\nphát triển bệnh", font=('Arial', 12), bg='yellow').grid(row=5, column=0, sticky='w')
Entry(frame, textvariable=stringNguyCo, width=15, font=('Arial', 12), fg='red').grid(row=5, column=1, pady=3)

Button(frame, text="Thoát", width=10, bg='lightblue', font=('Arial', 11), command=thoat).grid(row=6, column=1, pady=10)

root.mainloop()

from tkinter import *
from tkinter import messagebox

# ======= Hàm xử lý =======
def okAction():
    old_pw = entryOld.get()
    new_pw = entryNew.get()
    confirm_pw = entryConfirm.get()
    
    if new_pw == "" or confirm_pw == "" or old_pw == "":
        messagebox.showwarning("Warning", "Vui lòng nhập đầy đủ thông tin!")
    elif new_pw != confirm_pw:
        messagebox.showerror("Error", "Mật khẩu mới không trùng khớp!")
    else:
        messagebox.showinfo("Success", "Đổi mật khẩu thành công!")
        root.destroy()

def cancelAction():
    root.destroy()

# ======= Giao diện chính =======
root = Tk()
root.title("Enter New Password")
root.resizable(False, False)

# ======= Các thành phần =======
Label(root, text="Old Password:", font=('Arial', 10)).grid(row=0, column=0, padx=10, pady=6, sticky="e")
Label(root, text="New Password:", font=('Arial', 10)).grid(row=1, column=0, padx=10, pady=6, sticky="e")
Label(root, text="Enter New Password Again:", font=('Arial', 10)).grid(row=2, column=0, padx=10, pady=6, sticky="e")

entryOld = Entry(root, show="*", width=25, bd=2, relief=SUNKEN)
entryNew = Entry(root, show="*", width=25, bd=2, relief=SUNKEN)
entryConfirm = Entry(root, show="*", width=25, bd=2, relief=SUNKEN)

entryOld.grid(row=0, column=1, padx=10, pady=6)
entryNew.grid(row=1, column=1, padx=10, pady=6)
entryConfirm.grid(row=2, column=1, padx=10, pady=6)

# ======= Nút =======
btnOK = Button(root, text="OK", width=10, command=okAction)
btnCancel = Button(root, text="Cancel", width=10, command=cancelAction)

btnOK.grid(row=3, column=0, pady=10)
btnCancel.grid(row=3, column=1, pady=10)

# ======= Chạy =======
root.mainloop()

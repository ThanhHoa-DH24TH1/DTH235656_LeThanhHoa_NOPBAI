from tkinter import *

root = Tk()
root.title("frame 2")

# ====== Tạo Frame chính ======
frame = Frame(root, padx=10, pady=10)
frame.pack()

# ====== Danh sách style và độ dày viền ======
reliefs = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

for bw in range(5):  # borderwidth từ 0 đến 4
    # Dòng nhãn borderwidth
    Label(frame, text="borderwidth = " + str(bw), width=15, anchor='w').grid(row=bw, column=0, padx=5, pady=5)
    
    # Các nút hiển thị style
    for j, style in enumerate(reliefs):
        Button(frame, text=style, width=8, borderwidth=bw, relief=style).grid(row=bw, column=j+1, padx=5, pady=5)

root.mainloop()

print("Chương trình kiểm tra năm nhuần")
year=int(input("Mời bạn nhập vào 1 năm:"))
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
 print("Năm ", year, " là năm nhuần")
else:
 print("Năm ", year, " không nhuần")
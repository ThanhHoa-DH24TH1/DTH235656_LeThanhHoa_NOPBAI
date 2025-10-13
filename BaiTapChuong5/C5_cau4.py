"""
Một số hàm xử lý chuỗi trong Python:
1.Thay Đổi Trường Hợp Chữ:
.lower()	        Chuyển toàn bộ chuỗi thành chữ thường.	'HELLO'.lower() → 'hello'
.upper()	        Chuyển toàn bộ chuỗi thành chữ hoa.	'hello'.upper() → 'HELLO'
.title()	        Chuyển đổi thành dạng viết hoa đầu mỗi từ (Title Case).	'xin chao the gioi'.title() → 'Xin Chao The Gioi'
.capitalize()	    Chuyển ký tự đầu tiên của chuỗi thành chữ hoa, còn lại là chữ thường.	'thử nghiệm'.capitalize() → 'Thử nghiệm'

2.Tìm Kiếm và Kiểm Tra:
.strip()	        Loại bỏ khoảng trắng (hoặc ký tự chỉ định) ở đầu và cuối chuỗi.	' xin chao '.strip() → 'xin chao'
.startswith(prefix)	Kiểm tra xem chuỗi có bắt đầu bằng chuỗi con đã cho không (→ True/False).	'Python'.startswith('P') → True
.endswith(suffix)	Kiểm tra xem chuỗi có kết thúc bằng chuỗi con đã cho không (→ True/False).	'file.txt'.endswith('.txt') → True
.find(sub)	        Trả về chỉ mục (index) của lần xuất hiện đầu tiên của chuỗi con. Trả về -1 nếu không tìm thấy.	'abcabc'.find('b') → 1
.count(sub)	        Trả về số lần chuỗi con xuất hiện trong chuỗi.	'abcabc'.count('a') → 2
.isalnum()	        Kiểm tra xem chuỗi có chỉ chứa ký tự chữ và số (a-z, A-Z, 0-9) hay không.	'Py3'.isalnum() → True

3. Chia Tách và Nối Chuỗi:
.split(sep)	        Chia chuỗi thành một danh sách (list) các chuỗi con, dựa trên ký tự phân tách (sep) được cung cấp (mặc định là khoảng trắng).	'a,b,c'.split(',') → ['a', 'b', 'c']
.join(iterable)	    Nối các phần tử của một iterable (như list) thành một chuỗi duy nhất, sử dụng chuỗi hiện tại làm ký tự phân tách.	'-'.join(['1', '2', '3']) → '1-2-3'
.splitlines()	    Chia chuỗi tại các ký tự xuống dòng (\n, \r, v.v.) và trả về một list.	'dòng 1\ndòng 2'.splitlines() → ['dòng 1', 'dòng 2']

4. Thay Thế:
.replace(old, new, count)	Thay thế tất cả (hoặc giới hạn bằng count) chuỗi con cũ bằng chuỗi con mới.	'cat dog cat'.replace('cat', 'bird') → 'bird dog bird'

5.Hàm Tích Hợp:
len(s)	            Trả về độ dài của chuỗi (số lượng ký tự).	len('Python') → 6
str(object)	        Chuyển đổi đối tượng bất kỳ thành biểu diễn chuỗi của nó.	str(123) → '123'
f-strings	        Không phải là hàm, mà là cú pháp (f"...") để định dạng chuỗi hiệu quả và dễ đọc.	name = 'Alice'; f"Hi, {name}" → 'Hi, Alice'
"""
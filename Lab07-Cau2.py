## Bài 4: Điều chỉnh chữ „Xin chao!‟ và điều chuyển về trang Đại học Văn Lang
from flask import Flask, render_template
from flask import abort, redirect, url_for
ungdung = Flask(__name__)
@ungdung.route('/')
def hello():
    tentruong = 'Dai hoc Van Lang'
    lienket = '<a href="https://www.vanlanguni.edu.vn">' +tentruong+' </a> <br>'
    chuoi = lienket
    import datetime
    nam = datetime.date.today().year
    chuoi = chuoi + ' <b>Xin <i>chao</i> Tan sinh vien nam ' + str(nam) + '!</b> '
    return chuoi

#### Bài 5: Thay đổi cổng web và thêm định tuyến trang con
@ungdung.route('/monhoc')
def learn():
    chuoi = 'Day la trang mon hoc'
    return chuoi

### Bài 6: Định tuyến đến một môn học
@ungdung.route('/monhoc/<tenmon>')
def subject(tenmon):
    chuoi = 'Day la trang mon hoc'
    monhoc = str(tenmon).upper()
    if monhoc == " ":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi
@ungdung.route('/sinhvien')
def student():
    chuoi = 'Day la trang cac khoa hoc !'
    return chuoi

@ungdung.route('/sinhvien/<int:namhoc>')
def school_year(namhoc):
    chuoi = 'Day la nam hoc'
    nam = str(namhoc).upper()
    if nam == " ":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + nam
    return chuoi

### Bài 7: Web templating: truyền biến đơn 
### Bài 8: Web templating: Truyền biến kiểu danh sách
app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
    languages.append({'STT':4, 'ten': ".NET" })
    languages.append({'STT':5, 'ten': "Matlab" })
    return render_template('hello.html', hoten = name, ngon_ngu = languages)

###Bài 10: Định tuyến nội bộ url_for
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    abort(401)
if __name__ =="__main__":
    ungdung.run( port= 5050)


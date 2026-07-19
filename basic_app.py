from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
students = []
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/register',methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        student = {
            "name": name,
            "age": age,
            "course": course
        }
        students.append(student)
        return render_template('success.html',
                           name=name,
                           age=age,
                           course=course
        )
@app.route('/success')
def success():
    return render_template('success.html')
@app.route('/students')
def view_students():
    return render_template("students.html", students=students)
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    students = session.get('students', {})
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form.get('name')
    grade = float(request.form.get('grade'))
    
    if 'students' not in session:
        session['students'] = {}
    
    session['students'][name] = grade
    session.modified = True  # Ensure changes are reflected in the session
    return redirect(url_for('index'))

@app.route('/average', methods=['GET'])
def average_grade():
    students = session.get('students', {})
    if not students:
        return render_template('index.html', error_message="No students available to calculate the average.")
    
    total = sum(students.values())
    average = total / len(students)
    
    return render_template('index.html', students=students, average_grade=round(average, 2))

@app.route('/clear', methods=['GET'])
def clear_data():
    session.pop('students', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

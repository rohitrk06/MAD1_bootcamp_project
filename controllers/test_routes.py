from app import app
from flask import render_template

@app.route('/')
def hello_world():
    return f'Hello, World! {6} + {7} = {6 + 7}'


# /hello/john

@app.route('/hello/<int:age>')
def hello(age):
    list_students = [
        {'name': 'John', 'age': 20},
        {'name': 'Jane', 'age': 22},
        {'name': 'Bob', 'age': 19},
        {'name': 'Alice', 'age': 21},
        {'name': 'Charlie', 'age': 23},
        {'name': 'David', 'age': 24},
        {'name': 'Eve', 'age': 25},
        {'name': 'Frank', 'age': 26},
        {'name': 'Grace', 'age': 27},
        {'name': 'Heidi', 'age': 28}
    ]
    search_result =[]
    for student in list_students:
        if student['age'] > age:
            search_result.append(student)

    return render_template('home.html', students = search_result)



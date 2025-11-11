from flask import Flask, redirect , render_template , request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

from sqlalchemy import desc

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "todo.db")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Todo(db.Model):
    Sr_No = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.Sr_No} - {self.title}"

@app.route('/', methods=['GET'])
def index():
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

@app.route('/submit', methods=['POST'])
def submit():
    title = request.form.get('todo-title', ' ').strip()
    desc = request.form.get('todo-desc', ' ').strip()

    if title and desc:
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        
    return redirect(url_for('index'))

@app.route('/delete/<int:Sr_No>')
def delete(Sr_No):
    # One Method
    # allTodo = Todo.query.filter_by(Sr_No=Sr_No).first()
    # db.session.delete(allTodo)

    #another method
    Todo.query.filter_by(Sr_No=Sr_No).delete()

    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:Sr_No>', methods= ['GET','POST'])
def update(Sr_No):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(Sr_No=Sr_No).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('index'))
        
    todo = Todo.query.filter_by(Sr_No=Sr_No).first()
    return render_template('update.html', todo=todo)

@app.route('/about')
def about():
    return render_template('about.html')    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True , port=8000)
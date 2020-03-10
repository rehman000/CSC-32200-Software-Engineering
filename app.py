from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)       # __name__ is referencing the name of this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sql:///test.db'            # the 3 /// slashes refer to a relative path, 4 //// would mean an absolute path.
db = SQLAlchemy(app)        # To initialize our DataBase we need to pass in our app

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')             # This is how we create URL routes in Python-Flask
def index():                # This is the function for that route
    return render_template('index.html')  



@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True) 
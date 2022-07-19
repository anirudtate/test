from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/user/<username>')
def profile(username):
   if username=="anirud":
       return "This is a admin page"
   else:
       return f"This is {username}'s page"

todos = []
@app.route("/todos", methods=['GET', 'POST'])
def todolist():
    todo = ""
    if request.method == 'POST':
        todo = request.form['todo']
        todos.insert(0,todo)
    return render_template("todo.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)

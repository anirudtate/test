from flask import Flask,render_template, request

app = Flask(__name__)

todos = []
@app.route("/", methods=['GET', 'POST'])
def index():
    todo = ""
    if request.method == 'POST':
        todo = request.form['todo']
        todos.append(todo)
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)

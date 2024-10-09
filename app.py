from flask import Flask,render_template, request,redirect

app = Flask(__name__)

tasks = []
@app.route("/")
def hello_world():
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods =["POST"])
def add():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append(task)
        return render_template('index.html', tasks = tasks)


@app.route('/delete/<int:index>', methods=["GET"])
def delete(index):
    if request.method == "GET":
        print(index)
        del tasks[index]
        return redirect('/')

@app.route('/edit/<int:index>', methods=["GET"])
def edit(index):
    if request.method == "GET":
        task = tasks[index]
        return render_template('edit.html', task=task, index=index)
    
@app.route('/edit/<int:index>', methods=["POST"])
def edit_post(index):
    if request.method == "POST":
        new_task = request.form.get("task")
        tasks[index] = new_task
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template, request, redirect

app = Flask(__name__)
members = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        members.append({'name': name, 'email': email})
        return redirect('/')
    return render_template('join.html')

@app.route('/members')
def show_members():
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)

from database import init_db, query_db, add_blog, close_db
from flask import Flask, render_template, url_for, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto a una clave secreta real

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/blogs')
def blogs():
    if session.get('alreadyLogued'):
        return redirect(url_for("blogsLogued"))
    else:
        return render_template('blogs.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = request.args.get('username')
    password = request.args.get('password')
    
    if user == "juancho" and password == "123":
        session['alreadyLogued'] = True
        return redirect(url_for('page'))
    else:
        return render_template('login.html', error="Credenciales incorrectas")

@app.route('/planes')
def planes():
    if session.get('alreadyLogued'):
        return redirect(url_for("planesLoged"))
    else:
        return render_template('planes.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    user = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    
    if user is not None and password is not None and email is not None:
        session['alreadyLogued'] = True
        return redirect(url_for('page'))
    else:
        return render_template('registro.html', error="Credenciales incorrectas")

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/listado')
def index():
    blogs = query_db('SELECT * FROM blogs ORDER BY id DESC')
    return render_template('blogs.html', blogs=blogs)

@app.route('/add', methods=['POST'])
def add_blogs():
    add_blog(request.form['title'], request.form['image'], request.form['description'], request.form['author'])
    return redirect(url_for('index'))

@app.teardown_appcontext
def teardown_db(exception):
    close_db(exception)

@app.route("/blogsLogued")
def blogsLogued():
    return render_template("blogsLoged.html")

@app.route("/planesLoged")
def planesLoged():
    return render_template("planesLoged.html")

@app.route("/logout")
def logout():
    session.pop('alreadyLogued', None)  # Elimina la sesión del usuario
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db(app)  # Inicializar la base de datos
    app.run(debug=True)

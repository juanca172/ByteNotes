import sqlite3
from flask import Flask, render_template, url_for ,request, redirect, flash


app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('app_data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('home'))
        else:
            flash('Credenciales incorrectas, intente nuevamente.')
    
    return render_template('login.html')

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('app_data.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
            flash('Registro exitoso, ahora puede iniciar sesión.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('El correo ya está registrado.')
        finally:
            conn.close()

    return render_template('registro.html')

    
@app.route('/page',)
def page():
    return render_template('page.html')

def init_sqlite_db():
    conn = sqlite3.connect('app_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_sqlite_db()

if __name__ == '__main__':
    app.run(debug=True)

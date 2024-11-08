from flask import Flask, render_template, url_for ,request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('principal.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/login')
def login():
    user = request.args.get('username')     # Obtiene el valor de 'username'
    password = request.args.get('password') # Obtiene el valor de 'password'
    
    # Compara el usuario y la contraseña (asegúrate de que password sea string)
    if user == "juancho" and password == "123":
        # Redirige a la página principal (puedes cambiar 'home' por otra ruta)
        return redirect(url_for('page'))
    else:
        # Si los datos son incorrectos, muestra el formulario de login
        return render_template('login.html', error="Credenciales incorrectas")

@app.route('/planes')
def planes():
    return render_template('planes.html')

@app.route('/registro')
def registro():
    user = request.args.get('username')
    password = request.args.get('password')
    email = request.args.get('email')
    print(user)
    
    if user != None and password != None and email != None:
        # Redirige a la página principal (puedes cambiar 'home' por otra ruta)
        return redirect(url_for('page'))
    else:
        # Si los datos son incorrectos, muestra el formulario de login
        return render_template('registro.html', error="Credenciales incorrectas")

    
@app.route('/page')
def page():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)

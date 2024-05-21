from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import funciones
from flask import flash


app = Flask(__name__,template_folder="../templates")
app.secret_key = "123abdd"

@app.route("/")
def index():
    return render_template("index.html")





@app.route("/registro")
def registro():
    return render_template("registrar_usuarios.html")

@app.route("/registro_login", methods = ["POST", "GET"])
def registro_log():
    if request.method  == 'POST':
        usuario = request.form["usuario"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        try:
            funciones.registrar_usuario(usuario,email,password)
        except:
            flash("el correo electronico ingresado ya se encuentra registrado","error")
            return render_template("registrar_usuarios.html")
        finally:
            return render_template("registrar_usuarios.html")
    
        
        
@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method =="POST" and "email" in request.form and "password" in request.form:
        email= request.form["email"]
        password = request.form["password"]
        registros = funciones.inicio_sesion(email)
        if registros:
            if check_password_hash(registros[3],password):
                session["login"] = True
                session["id"] = registros[0]
                flash("session iniciada con exito","ini_session")
                return render_template("inicio_session.html", registros=registros)
            else:
                return render_template("index.html")
        else:
            return render_template("index.html")
   


@app.route("/logout")        
def logout_sesion():
    session.clear()
    return redirect((url_for('inicio')))











if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
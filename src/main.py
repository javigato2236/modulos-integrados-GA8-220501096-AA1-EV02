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
            flash("registro exitoso","registro_exito")
            return render_template("index.html")
        except:
            flash("el correo electronico ingresado ya se encuentra registrado","error")
            return render_template("registrar_usuarios.html")
        finally:
            pass


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
                flash("sesion iniciada con exito","ini_session")
                return render_template("inicio_session.html", registros=registros)
            else:
                flash("correo electronico o contraseña incorrectos","no_inicio_session")
                return render_template("index.html")
        else:
            flash("correo electronico o contraseña incorrectos","no_inicio_session")
            return render_template("index.html")
        






@app.route("/ver_registros")
def registro_estudi():
    return render_template("registros.html")

@app.route("/ini_sesion")
def inicio_sesion():
    return render_template("inicio_session.html")

@app.route("/registro_estudiantes", methods = ["POST", "GET"])
def registro_de_estudiantes():
    if request.method == 'POST':
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        edad = request.form["edad"]
        materia = request.form["materia"]
        calificacion = request.form["calificacion"]
        funciones.registrar_estudiantes(nombres, apellidos, edad, materia, calificacion)
        flash("Registro agregado con exito", "registro exitoso")
        return render_template("inicio_session.html")
    
@app.route("/eliminar", methods = ["POST"])
def eliminar_registro_estudiantes():
    funciones.borrar_registro(request.form["id"])
    flash("registro eliminado con exito","eliminar registro")
    return redirect("/ver_regis")

@app.route("/edit_datos/<int:id>")
def editar_datos(id):
    registro = funciones.obtener_datos(id)
    return render_template("actualizar_registro.html", registros = registro)

@app.route("/actualiza_datos" , methods=["POST", "GET"])
def actualizar_datos():
    id = request.form["id"]
    nombres = request.form["nombres"]
    apellidos =request.form["apellidos"]
    edad = request.form["edad"]
    materia = request.form["materia"]
    calificacion = request.form["calificacion"]
    funciones.actualizar(id,nombres,apellidos,edad,materia,calificacion)
    return redirect('/ver_regis')



   
@app.route("/ver_regis")  
def ver_registros():
    registros = funciones.enviar_registro()
    return render_template("registros.html", registros = registros)








@app.route("/logout")        
def logout_sesion():
    session.clear()
    flash("sesion cerrada con exito","cerrar sesion")
    return redirect((url_for('index')))











if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
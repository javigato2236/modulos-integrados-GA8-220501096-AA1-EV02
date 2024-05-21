from coneccionbd import iniciar_conexion

def registrar_usuario(usuario,email,password):
    conexion = iniciar_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(usuario, correo_electronico, password) VALUES (%s,%s,%s)",(usuario,email,password)) 
        conexion.commit()
        conexion.close()

def registrar_estudiantes(nombres, apellidos, edad, materia, calificacion):
    conexion = iniciar_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO estudiantes(nombres, apellidos, edad, materia, calificacion) VALUES (%s,%s,%s,%s,%s)",(nombres, apellidos, edad, materia, calificacion)) 
        conexion.commit()
        conexion.close()

def enviar_registro():
    conexion = iniciar_conexion()
    registros = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombres, apellidos, edad, materia, calificacion FROM estudiantes")
        registros = cursor.fetchall()
    conexion.close()
    return registros






def inicio_sesion(email):
    conexion = iniciar_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT *FROM usuarios WHERE correo_electronico=%s",(email))
        registros = cursor.fetchone()
        return registros
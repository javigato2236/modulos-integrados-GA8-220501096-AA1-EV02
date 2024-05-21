from coneccionbd import iniciar_conexion

def registrar_usuario(usuario,email,password):
    conexion = iniciar_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(usuario, correo_electronico, password) VALUES (%s,%s,%s)",(usuario,email,password)) 
        conexion.commit()
        conexion.close()

def inicio_sesion(email):
    conexion = iniciar_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT *FROM usuarios WHERE correo_electronico=%s",(email))
        registros = cursor.fetchone()
        return registros
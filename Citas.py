import sqlite3

#Conectar a la base de datos 
conexion = sqlite3.connect("Database/Personas.sqlite3")

#Seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

#Codigo sql para mostrar todos los datos de la tabla
sql = "SELECT * FROM personas"

#Ejecutar la consulta de consulta de datos
if(consulta.execute(sql)): 
    filas = consulta.fetchall()
    for fila in filas:
        print(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5], fila[6], fila[7], fila[8], fila[9])
else:
    print("Error al agregar datos")

#Terminando la consulta
consulta.close()

#Guardar cambios en la base de datos
conexion.commit()

#Cerrar conexion a la base de datos
conexion.close()
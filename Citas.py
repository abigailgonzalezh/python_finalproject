import sqlite3

#Preguntar al usuario datos de su posible cita
edadMinima=int(input("Cual es la edad minima que deseas que tenga tu cita? "))
edadMaxima=int(input("Cual es la edad maxima que deseas que tenga tu cita? "))
genero=input("Que genero estas buscando? ")
signo=input("Que signo estas buscando? ")
sexualidad=input("Que sexualidad buscas? ")
colorOjos=input("Que color de ojos buscas? ")
colorPiel=input("Que color de piel buscas? ")
#ingreso=float(input("Que ingreso buscas? "))

#Conectar a la base de datos 
conexion = sqlite3.connect("Database/Personas.sqlite3")

#Seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

#Codigo sql para mostrar todos los datos de la tabla
sql = "SELECT * FROM personas WHERE edad BETWEEN ? AND ? AND genero=? AND signo=? AND sexualidad=? AND color_ojos=? AND color_piel=?" 
datos = (edadMinima, edadMaxima, genero, signo, sexualidad, colorOjos, colorPiel)

#Ejecutar la consulta de consulta de datos
if(consulta.execute(sql,datos)): 
    filas = consulta.fetchall()
    if len(filas)>0:
        for fila in filas:
            print(fila[0], fila[1], fila[2], fila[3], fila[4],fila[5], fila[6], fila[7], fila[8], fila[9])
    else:
        print("Ninguna persona coincide con tu criterio de busqueda")
else:
    print("Error al agregar datos")

#Terminando la consulta
consulta.close()

#Guardar cambios en la base de datos
conexion.commit()

#Cerrar conexion a la base de datos
conexion.close()
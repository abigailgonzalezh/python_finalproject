import sqlite3

#Conectar a la base de datos 
conexion = sqlite3.connect("Database/Personas.sqlite3")

#Seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

#Codigo sql para crear la tabla personas
sql = """
CREATE TABLE personas (
  id INT NOT NULL,
  nombre VARCHAR(45) NULL,
  edad INT NULL,
  estatura FLOAT NULL,
  genero VARCHAR(45) NULL,
  signo VARCHAR(45) NULL,
  sexualidad VARCHAR(45) NULL,
  color_ojos VARCHAR(45) NULL,
  color_piel VARCHAR(45) NULL,
  ingreso FLOAT NULL,
  PRIMARY KEY (id))
"""

#Ejecutar la consulta de creacion de tabla
if(consulta.execute(sql)): 
    print("Tabla creada con exito")
else:
    print("Error al crear la tabla")

#Terminando la consulta
consulta.close()

#Guardar cambios en la base de datos
conexion.commit()

#Cerrar conexion a la base de datos
conexion.close()
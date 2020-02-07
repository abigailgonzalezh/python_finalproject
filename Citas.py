import sqlite3
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Citas app")
window.geometry('700x400')

#Pedir nombre 
lbl = Label(window, text="¿Cuál es tu nombre?")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

#Pedir edad minima
lbl1 = Label(window, text="¿Cuál es la edad minima que deseas que tenga tu cita?")
lbl1.grid(column=0, row=2)
txtEdadMinima = Entry(window,width=10)
txtEdadMinima.grid(column=1, row=2)

#Pedir edad Maxima
lbl2 = Label(window, text="¿Cuál es la edad maxima que deseas que tenga tu cita?")
lbl2.grid(column=0, row=3)
txtEdadMaxima = Entry(window,width=10)
txtEdadMaxima.grid(column=1, row=3)

#Pedir genero
lbl3 = Label(window, text="¿Qué genero deseas que tenga tu cita?")
lbl3.grid(column=0, row=4)
combo = Combobox(window)
combo['values']= ("Masculino", "Femenino", "Otro")
combo.current(0) #Seleccionar el valor que se mostrara
combo.grid(column=1, row=4)

#Pedir signo zodiacal
lbl4 = Label(window, text="¿Qué signo zodiacal deseas que tenga tu cita?")
lbl4.grid(column=0, row=5)
combo1 = Combobox(window)
combo1['values']= ("Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Acuario", "Piscis")
combo1.current(0) #Seleccionar el valor que se mostrara
combo1.grid(column=1, row=5)

#Pedir sexualidad
lbl5 = Label(window, text="¿Qué sexualidad deseas que tenga tu cita?")
lbl5.grid(column=0, row=6)
combo2 = Combobox(window)
combo2['values']= ("Heterosexual", "Homosexual", "Asexual", "Pansexual")
combo2.current(0) #Seleccionar el valor que se mostrara
combo2.grid(column=1, row=6)

#Color de ojos
lbl6 = Label(window, text="¿Qué color de ojos deseas que tenga tu cita?")
lbl6.grid(column=0, row=7)
combo2 = Combobox(window)
combo2['values']= ("Negros", "Cafe oscuro", "Cafe claro", "Verdes", "Azules",)
combo2.current(0) #Seleccionar el valor que se mostrara
combo2.grid(column=1, row=7)

#Color de piel
lbl7 = Label(window, text="¿Qué color de piel deseas que tenga tu cita?")
lbl7.grid(column=0, row=8)
combo3 = Combobox(window)
combo3['values']= ("Clara", "Morena", "Blanca", "Negra")
combo3.current(0) #Seleccionar el valor que se mostrara
combo3.grid(column=1, row=8)

#Boton aceptar con funcion que guarda los datos al dar aceptar
def clicked():

    res = "Bienvenido " + txt.get()
    lbl.configure(text= res)
 
btn = Button(window, text="Aceptar", command=clicked)
btn.grid(column=0, row=9)
 
window.mainloop()

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
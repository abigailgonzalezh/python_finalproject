import sqlite3
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Citas app")
window.geometry('1000x400')

#Pedir nombre 
lbl = Label(window, text="¿Cuál es tu nombre?", font=("Century Gothic", 12))
lbl.grid(column=0, row=0, padx = 10, pady = 10)
txt = Entry(window, width=20, justify = CENTER, font=("Century Gothic", 12))
txt.grid(column=1, row=0, padx = 10, pady = 10)

#Pedir edad minima
lbl1 = Label(window, text="¿Cuál es la edad mínima que deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl1.grid(column=0, row=2, padx = 10, pady = 10)
txtEdadMinima = Entry(window, width=20, justify = CENTER, font=("Century Gothic", 12))
txtEdadMinima.grid(column=1, row=2, padx = 10, pady = 10)

#Pedir edad Maxima
lbl2 = Label(window, text="¿Cuál es la edad máxima que deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl2.grid(column=0, row=3, padx = 10, pady = 10)
txtEdadMaxima = Entry(window, width=20, justify = CENTER, font=("Century Gothic", 12))
txtEdadMaxima.grid(column=1, row=3, padx = 10, pady = 10)

#Pedir genero
lbl3 = Label(window, text="¿Qué género deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl3.grid(column=0, row=4, padx = 10, pady = 10)
combo = Combobox(window, state='readonly', font=("Century Gothic", 12))
combo['values']= ("Masculino", "Femenino", "Otro")
combo.current(0) #Seleccionar el valor que se mostrara
combo.grid(column=1, row=4, padx = 10, pady = 10)

#Pedir signo zodiacal
lbl4 = Label(window, text="¿Qué signo zodiacal deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl4.grid(column=0, row=5, padx = 10, pady = 10)
combo1 = Combobox(window, state='readonly', font=("Century Gothic", 12))
combo1['values']= ("Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Acuario", "Piscis")
combo1.current(0) #Seleccionar el valor que se mostrara
combo1.grid(column=1, row=5, padx = 10, pady = 10)

#Pedir sexualidad
lbl5 = Label(window, text="¿Qué sexualidad deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl5.grid(column=0, row=6, padx = 10, pady = 10)

combo2 = Combobox(window, state='readonly', font=("Century Gothic", 12))
combo2['values']= ("Heterosexual", "Homosexual", "Asexual", "Pansexual")
combo2.current(0) #Seleccionar el valor que se mostrara
combo2.grid(column=1, row=6, padx = 10, pady = 10)

#Color de ojos
lbl6 = Label(window, text="¿Qué color de ojos deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl6.grid(column=0, row=7, padx = 10, pady = 10)
combo3 = Combobox(window, state='readonly', font=("Century Gothic", 12))
combo3['values']= ("Negros", "Cafe oscuro", "Cafe claro", "Verdes", "Azules",)
combo3.current(0) #Seleccionar el valor que se mostrara
combo3.grid(column=1, row=7, padx = 10, pady = 10)

#Color de piel
lbl7 = Label(window, text="¿Qué color de piel deseas que tenga tu cita?", font=("Century Gothic", 12))
lbl7.grid(column=0, row=8, padx = 10, pady = 10)
combo4 = Combobox(window, state='readonly', font=("Century Gothic", 12))
combo4['values']= ("Clara", "Morena", "Blanca", "Negra")
combo4.current(0) #Seleccionar el valor que se mostrara
combo4.grid(column=1, row=8, padx = 10, pady = 10)

#Boton aceptar con funcion que guarda los datos al dar aceptar
def clicked():
    res = "Bienvenido " + txt.get()
    edadMinima = txtEdadMinima.get()
    edadMaxima = txtEdadMaxima.get()
    genero = combo.get()
    signo = combo1.get()
    sexualidad = combo2.get()
    colorOjos = combo3.get()
    colorPiel = combo4.get()
    datos=(edadMinima,edadMaxima,genero,signo,sexualidad,colorOjos,colorPiel)

    #Conectar a la base de datos 
    conexion = sqlite3.connect("Database/Personas.sqlite3")

    #Seleccionar el cursor para realizar la consulta
    consulta = conexion.cursor()

    #Codigo sql para mostrar todos los datos de la tabla
    sql = "SELECT * FROM personas WHERE edad BETWEEN ? AND ? AND genero=? AND signo=? AND sexualidad=? AND color_ojos=? AND color_piel=?" 
    
    #print(datos)

    #Ejecutar la consulta de consulta de datos
    if(consulta.execute(sql,datos)): 
        filas = consulta.fetchall()
        if len(filas)>0:
            i=0
            lbl8 = Label(window, text="Felicidades. Hiciste match con alguien!!", font=("Century Gothic", 12))
            lbl8.grid(column=4, row=0, padx = 10, pady = 10)
            for fila in filas:
                lbl9 = Label(window, text="Nombre: "+ str(fila[1]), font=("Century Gothic", 12))
                lbl9.grid(column=4, row=1+1, padx = 10, pady = 10)
        else:
            print("Lo siento, no haces match con nadie")
    else:
        print("Error")

    #Terminando la consulta
    consulta.close()

    #Guardar cambios en la base de datos
    conexion.commit()

    #Cerrar conexion a la base de datos
    conexion.close()

style = Style()
style.configure('W.TButton', font=("Century Gothic", 12)) #Le agrega estilo al boton
    
btn = Button(window, text="Aceptar", command=clicked, style = 'W.TButton')
btn.grid(column=0, row=9, padx = 10, pady = 10)    

window.mainloop()

#Preguntar al usuario datos de su posible cita
#edadMinima=int(input("Cual es la edad minima que deseas que tenga tu cita? "))
#edadMaxima=int(input("Cual es la edad maxima que deseas que tenga tu cita? "))
#genero=input("Que genero estas buscando? ")
#signo=input("Que signo estas buscando? ")
#sexualidad=input("Que sexualidad buscas? ")
#colorOjos=input("Que color de ojos buscas? ")
#colorPiel=input("Que color de piel buscas? ")
#ingreso=float(input("Que ingreso buscas? "))

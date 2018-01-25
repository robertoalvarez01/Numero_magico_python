from tkinter import *
from tkinter import messagebox
import random
import os

# Función para determinar el número magico
def numero_magico():
	num = random.randrange(0,101)
	return num

# Función que debera ejecutar el Botón
def verificar():
	global numero_secreto
	try:
		num = int(num_user.get())
	except:
		messagebox.showinfo("Error", "Solo puede ingresar numeros enteros del 1 al 100")
		borrar()
	else:
		if num > 100 or num < 1:
			messagebox.showinfo("Error", "Solo puede ingresar numeros enteros del 1 al 100")
			borrar()
		elif num != numero_secreto:

			if num > numero_secreto:
				mayor()
				borrar()

			elif num < numero_secreto:
				menor()
				borrar()

		elif numero_secreto == num:
			correcto()

# Funcion si el número ingresado es mayor al número mágico
def mayor():
	messagebox.showinfo("Numero muy alto", "El numero que ingresaste es mayor al número mágico")

# Funcion si el número ingresado es menor al número mágico
def menor():
	messagebox.showinfo("Numero muy bajo", "El numero que ingresaste es menor al número mágico")

# Funcion si aciertas al numero
def correcto():
	messagebox.showinfo("Acertaste!!!", "El numero que ingresaste es el número mágico, felicitaciones")
	os.startfile("numero_magico.py")
	root.quit()

# Funcion para borrar el contenido del TextBox
def borrar():
	num_user.set("")

# Creamos el número que debera ser adivinado
numero_secreto = numero_magico()

# Creamos raíz de la ejecución
root = Tk()
root.title("Número Mágico")
root.resizable(0,0)

# Definimos la variable utilizada para el usuario
num_user = StringVar()

# Colocamos en la raíz el label de la consigna
consigna = Label(root, text="Ingrese el número mágico")
consigna.config(font=("Verdana", 15))
consigna.grid(row=0, column=0, padx=5, pady=5)

# Colocamos el TextBox para leer el numero indicado por el usuario
numero = Entry(root, textvariable=num_user)
numero.config(font=("Verdana", 15), justify="center")
numero.grid(row=1, column=0, padx=5, pady=5)

# Colocamos un separador para alinear bien el contenido
separador = Label(root, text="\n")
separador.config(font=("Verdana", 15))
separador.grid(row=2, column=0, padx=5, pady=5)

# Colocamos el botón para ejecutar la accion
boton = Button(root, text="Verificar", command=verificar)
boton.config(font=("Verdana", 15))
boton.grid(row=3, column=0, padx=5, pady=5)


# Fin del programa
root.mainloop()

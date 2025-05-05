from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Temporizador")
frame = Frame(root)
frame.pack()

# Variables para el tiempo restante y estado del temporizador
tiempo_restante = 0
temporizador_activo = False

# Función para iniciar el temporizador
def iniciar():
    global tiempo_restante, temporizador_activo
    if not temporizador_activo:
        try:
            # Toma el tiempo ingresado por el usuario
            tiempo_restante = int(pantalla.get())
            if tiempo_restante > 0:
                temporizador_activo = True
                actualizar_temporizador()
        except ValueError:
            pantalla.delete(0, END)
            pantalla.insert(0, "Ingrese un número válido")

# Función para detener el temporizador
def detener():
    global temporizador_activo
    temporizador_activo = False

# Función para actualizar el tiempo en pantalla
def actualizar_temporizador():
    global tiempo_restante
    if temporizador_activo and tiempo_restante > 0:
        tiempo_restante -= 1
        tiempoRestante.delete(0, END)
        tiempoRestante.insert(0, str(tiempo_restante))
        
        # Llama a la función nuevamente después de 1 segundo
        root.after(1000, actualizar_temporizador)
    else:
        detener()  # Detiene el temporizador al llegar a 0

# Entrada para que el usuario ingrese el tiempo en segundos
pantalla = Entry(frame, font=("Arial", 14), justify="center")
pantalla.grid(row=1, column=1)

# Pantalla para mostrar el tiempo restante
tiempoRestante = Entry(frame, font=("Arial", 14), justify="center")
tiempoRestante.grid(row=1, column=2)

# Botón para iniciar el temporizador
botonInicio = Button(frame, text="Iniciar", command=iniciar)
botonInicio.grid(row=2, column=1)

# Botón para detener el temporizador
botonDetener = Button(frame, text="Detener", command=detener)
botonDetener.grid(row=2, column=2)

# Etiquetas para indicar la función de cada cuadro de texto
label1 = Label(frame, text="Introduzca el tiempo (segundos)")
label1.grid(row=0, column=1)

label2 = Label(frame, text="Tiempo restante")
label2.grid(row=0, column=2)

root.mainloop()

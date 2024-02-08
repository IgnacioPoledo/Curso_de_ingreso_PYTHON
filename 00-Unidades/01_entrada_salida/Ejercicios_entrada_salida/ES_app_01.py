import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

#TIPOS DE DATOS: string entre "", boolean es True o False, None, float, entero.
#El = es el operador de asignación 
#edad = 23   
#SIEMPRE escribir las variables en snake case
#edad_promedio = 23.2 
#Alert Question Prompt

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        
        alert("Mensaje", "Esto no anda, funciona")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

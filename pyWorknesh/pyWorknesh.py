from tkinter import ttk 
from tkinter import *

import sqlite3

class Persona:
    # connection dir property
    db_name = 'worknesh.db'

    def __init__(self, window):
        #initializations
        self.wind = window
        self.wind.title('Registro de Worknesh')

        #creating a frame container
        frame = LabelFrame(self.wind, text = 'Registrar Datos')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Name input 
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1)



        
if __name__ == '__main__':
    window = Tk()
    application = Persona(window)
    window.mainloop()



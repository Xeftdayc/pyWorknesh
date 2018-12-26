from tkinter import ttk 
from tkinter import *
import tkinter as tk
import sqlite3

class Persona:
    # connection dir property
    db_name = 'dbworknesh.db'

    def __init__(self, window):
        #initializations
        self.wind = window
        self.wind.title('Registro de Worknesh')

        # Creating a frame container
        frame = LabelFrame(self.wind, text = 'Registrar Datos')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # DNI Input
        Label(frame, text = 'DNI: ').grid(row = 1, column = 0)
        self.DNI = Entry(frame)
        self.DNI.focus()
        self.DNI.grid(row = 1, column = 1)
        
        # Name Input
        Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.Nombre = Entry(frame)
        self.Nombre.grid(row = 2, column = 1)

        # Apellidos input
        Label(frame, text = 'Apellidos: ').grid(row = 3, column = 0)
        self.Apellidos = Entry(frame)
        self.Apellidos.grid(row = 3, column = 1)

        # Sexo input
        Label(frame, text = 'Sexo: ').grid(row = 4, column = 0)
        self.Sexo = Entry(frame)
        self.Sexo.grid(row = 4, column = 1)

        # Direccion input 
        Label(frame, text = 'Direccion: ').grid(row = 5, column = 0)
        self.Direccion = Entry(frame)
        self.Direccion.grid(row = 5, column = 1)

        # FechaN input 
        Label(frame, text = 'Fecha Nacimiento: ').grid(row = 6, column = 0)
        self.FechaN = Entry(frame)
        self.FechaN.grid(row = 6, column = 1)

        # Email input 
        Label(frame, text = 'Email: ').grid(row = 7, column = 0)
        self.Email = Entry(frame)
        self.Email.grid(row = 7, column = 1)

        # Movil Input
        Label(frame, text = 'Numero Movil: ').grid(row = 8, column = 0)
        self.Nromovil = Entry(frame)
        self.Nromovil.grid(row = 8, column = 1)

        # Button add Persona
        ttk.Button(frame,text = 'Guardar Datos', command = self.add_persona).grid(row = 9,columnspan = 2, sticky = W + E)

        # Output Messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W+E)
        
        # Table
        self.tree = ttk.Treeview(height = 10, columns = ('1','2','3','4','5','6','7','8','9'), show="headings")
        self.tree.grid(row = 9, column = 0, columnspan = 2)
        self.tree.heading('1', text ='ID')
        self.tree.column('1', width=30, anchor = 'center')
        self.tree.heading('2', text ='DNI')
        self.tree.column('2', width=80, anchor = 'center')
        self.tree.heading('3', text ='Nombre')
        self.tree.column('3', width=100, anchor = 'center')
        self.tree.heading('4', text ='Apellidos')
        self.tree.column('4', width=100, anchor = 'center')
        self.tree.heading('5', text ='Sexo')
        self.tree.column('5', width=40, anchor = 'center')
        self.tree.heading('6', text ='Direccion')
        self.tree.column('6', width=100, anchor = 'center')
        self.tree.heading('7', text ='F. Nacimiento')
        self.tree.column('7', width=100, anchor = 'center')
        self.tree.heading('8', text ='Email')
        self.tree.column('8', width=100, anchor = 'center')
        self.tree.heading('9', text ='Numero Movil')
        self.tree.column('9', width=100, anchor = 'center')

        ttk.Style().configure("Treeview", font = ('', 11), background="#383838", foreground="white")

        # Buttons
        ttk.Button(text = 'ELIMINAR').grid(row = 10, column = 0, stick = W + E)
        ttk.Button(text = 'EDITAR').grid(row = 10, column = 1, stick = W + E)

        # Filling the rows
        self.get_persona()

    # Function to execute database querys
    def run_query(self,query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result
    # Get persona from database
    def get_persona(self):
        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Gettin data
        query = 'SELECT * FROM tDatos ORDER BY nombre DESC'
        db_rows = self.run_query(query)
        # Filling data
        for row in db_rows:
            self.tree.insert("", tk.END, values=row)
            print(row)


    # User input validation 
    def validation(self):
        return len(self.DNI.get()) !=0 and len(self.Nombre.get()) !=0 and len(self.Apellidos.get()) !=0 and len(self.Sexo.get()) !=0 \
        and len(self.Direccion.get()) !=0 and len(self.FechaN.get()) !=0 and len(self.Email.get()) !=0 and len(self.Nromovil.get()) !=0

    def add_persona(self):
        if self.validation():
            query = 'INSERT INTO tDatos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.DNI.get(), self.Nombre.get(), self.Apellidos.get(), self.Sexo.get(), self.Direccion.get(), self.FechaN.get(), self.Email.get(), self.Nromovil.get() )
            self.run_query(query, parameters)
            self.message['text'] = 'Registro de Persona {} added Successfully'.format(self.DNI.get())
            self.DNI.delete(0,END)
            self.Nombre.delete(0,END)
            self.Apellidos.delete(0,END)
            self.Sexo.delete(0,END)
            self.Direccion.delete(0,END) 
            self.FechaN.delete(0,END)
            self.Email.delete(0,END)
            self.Nromovil.delete(0,END)
        else:
            self.message['text'] = 'Datos input is Required'
        self.get_persona()



if __name__ == '__main__':
    window = Tk()
    application = Persona(window)
    window.mainloop()



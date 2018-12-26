from tkinter import ttk 
from tkinter import *

import sqlite3

class Persona:
    # connection dir property
    db_name = 'dbworknesh.db'

    def __init__(self, window):
        #initializations
        self.wind = window
        self.wind.title('Registro de Worknesh')

        #creating a frame container
        frame = LabelFrame(self.wind, text = 'Registrar Datos')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Name input 
        Label(frame, text = 'DNI: ').grid(row = 1, column = 0)
        self.DNI = Entry(frame)
        self.DNI.focus()
        self.DNI.grid(row = 1, column = 1)       
        
        #Name input 
        Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row = 2, column = 1)

        #Name input
        Label(frame, text = 'Apellidos: ').grid(row = 3, column = 0)
        self.Apellidos = Entry(frame)
        self.Apellidos.focus()
        self.Apellidos.grid(row = 3, column = 1)

        #Name input
        Label(frame, text = 'Sexo: ').grid(row = 4, column = 0)
        self.Apellidos = Entry(frame)
        self.Apellidos.focus()
        self.Apellidos.grid(row = 3, column = 1)

        #Name input 
        Label(frame, text = 'Direccion: ').grid(row = 5, column = 0)
        self.Direccion = Entry(frame)
        self.Direccion.focus()
        self.Direccion.grid(row = 4, column = 1)

        #Name input 
        Label(frame, text = 'Fecha Nacimiento: ').grid(row = 6, column = 0)
        self.FechaN = Entry(frame)
        self.FechaN.focus()
        self.FechaN.grid(row = 5, column = 1)

        #Name input 
        Label(frame, text = 'Email: ').grid(row = 7, column = 0)
        self.Email = Entry(frame)
        self.Email.focus()
        self.Email.grid(row = 6, column = 1)

        #Name input 
        Label(frame, text = 'Numero Movil: ').grid(row = 8, column = 0)
        self.Nromovil = Entry(frame)
        self.Nromovil.focus()
        self.Nromovil.grid(row = 7, column = 1)

        #Button add Persona
        ttk.Button(frame,text = 'Guardar Datos').grid(row = 9,columnspan = 2, sticky = W + E)

        #Table

        #--- Nueva ventana---
        #root = Tk()
        self.tree = ttk.Treeview(selectmode="extended", height = 10, columns = ("A","B","C","D","E","F","G"))
        
        self.tree.grid(row = 9, column = 0, columnspan = 2)
        self.tree.heading('#0', text ='DNI', anchor = CENTER)
        self.tree.column('#0', width=100)
        self.tree.heading('A', text ='Nombre', anchor = CENTER)
        self.tree.column('A', width=100)
        self.tree.heading('B', text ='Apellidos', anchor = CENTER)
        self.tree.column('B', width=100)
        self.tree.heading('C', text ='Sexo', anchor = CENTER)
        self.tree.column('C', width=100)
        self.tree.heading('D', text ='Direccion', anchor = CENTER)
        self.tree.column('D', width=100)
        self.tree.heading('E', text ='Fecha Nacimiento', anchor = CENTER)
        self.tree.column('E', width=100)
        self.tree.heading('F', text ='Email', anchor = CENTER)
        self.tree.column('F', width=100)
        self.tree.heading('G', text ='Numero Movil', anchor = CENTER)
        self.tree.column('G', width=100)

        #Buttons
        ttk.Button(text = 'ELIMINAR').grid(row = 10, column = 0, stick = W + E)
        ttk.Button(text = 'EDITAR').grid(row = 10, column = 1, stick = W + E)

        # Filling the rows
        self.get_persona()

    # function to execute database querys
    def run_query(self,query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result
    #get persona from database
    def get_persona(self):
        #cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # gettin data 
        query = 'SELECT * FROM tDatos ORDER BY nombre DESC'
        db_rows = self.run_query(query)
        #filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])
            #print(row)


    #user input validation 
    def validation(self):
        return len(self.name.get()) !=0 and len(self.price.get()) !=0

    def add_persona(self):
        if self.validation():
            query = 'INSERT INTO tDatos VALUES(NULL,?,?,?,?,?,?)'
            parameters = (self.DNI.get(), self.Nombre.get(), self.Apellidos.get(), self.Sexo.get(), self.Direccion.get(), self.FechaN.get(), self.Email.get(), self.Nromovil.get() )
            self.run_query(query, parameters)
            self.message['text'] = 'persona {} added Successfully'.format(self.DNI.get())
            self.DNI.delete(0,END)
            self.Nombre.delete(0,END)
            self.Apellidos.delete(0,END)
            self.Sexo.delete(0,END)
            self.Direccion.delete(0,END) 
            self.FechaN.delete(0,END)
            self.Email.delete(0,END)
            self.Nromovil.delete(0,END)
        else:
            self.message['text'] = 'DNI and Nombre and Apellidos and Direccion and FechaN and Email and Nromovil is Required'
        self.get_persona()



if __name__ == '__main__':
    window = Tk()
    application = Persona(window)
    window.mainloop()



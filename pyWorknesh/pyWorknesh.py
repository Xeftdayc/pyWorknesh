from tkinter import ttk 
from tkinter import *
import sqlite3

root = Tk()
root.title("Worknesh: Modulo de Ingreso")

foto = PhotoImage(file="LOGO.png")
Label(root, image=foto).pack()

width = 600
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("dbworknesh.db")
    cursor = conn.cursor()
    #cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    #cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    #if cursor.fetchone() is None:
     #   cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
      #  conn.commit()
    
def Login(event=None):
    Database()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `tUser` WHERE `user` = ? AND `pswd` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            Dashboard()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

def Dashboard():
    global gDash
    root.withdraw()
    gDash = Toplevel()
    gDash.title("Worknes: Dashboard - Panel Administrativo")
    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()
    width = 1280
    height = 700
    screen_height = root.winfo_screenwidth()
    screen_width = root.winfo_screenheight()
    x = (screen_width/1) - (width/1.7)
    y = (screen_height/15) - (height/15)
    gDash.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #root.resizable(0, 0)

    #btnLogout = Button(gDash, text='Cerrar Seccion', command=Back).pack(pady=20, fill=X)

    # Variables

    # Frame o Grid
    Top = Frame(gDash, bd=2, relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Bottom = Frame(gDash, bd=2, relief=RIDGE)
    Bottom.pack(side=BOTTOM, fill=X)
    Form = Frame(gDash, height=200)
    Form.pack(side=TOP, pady=20)

    #tFrame = Frame(gDash, bg='cyan', width=450, height=50, pady=3, relief=RIDGE)
    #tFrame.pack(fill=X).grid(row = 0, columnspan = 3)

    #tFrame2 = Frame(gDash, bg='red', width=250, height=150, pady=3, relief=RIDGE)
    #tFrame2.pack(side=BOTTOM).grid(row = 1, columnspan = 3)


    # Labels
    lbTitle = Label(Top, text="Worknesh: Bienvenido al Panel de Administracion", font=('arial black', 18))
    lbTitle.pack(fill=X)
    btnLogout = Button(gDash, text='Cerrar Seccion', command=Back).pack(pady=20, fill=X)
    btnRegistro = Button(gDash, text='Modulo Registro', command=modRegistro).pack(pady=20, fill=X)
    btnVaca = Button(gDash, text='Modulo Vacaciones', command=modVaca).pack(pady=20, fill=X)
    btnAsistencia = Button(gDash, text='Modulo Asistencia', command=modAsistencia).pack(pady=20, fill=X)
    Label(gDash, text="Successfully Login!", font=('times new roman', 20)).pack()

    # Buttons
    #btnAdd = Button(Form, text="Agregar Ventana", width=80, command=modRegistro)
    #btnAdd.grid(pady=25, row=3, columnspan=2).pack(pady=20, fill=X)
    

def modRegistro():
    global gRegistro
    #gDash.withdraw()
    gRegistro = Toplevel()
    gRegistro.title("Worknes: Dashboard - Modulo de Registro")
    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()
    width = 1280
    height = 700
    screen_height = root.winfo_screenwidth()
    screen_width = root.winfo_screenheight()
    x = (screen_width/1) - (width/1.7)
    y = (screen_height/15) - (height/15)
    gRegistro.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #Dashboard.resizable(0, 0)

    # Variables
    tbBusqueda = StringVar()
    tbCodigo = StringVar()
    tbNombre = StringVar()
    tbPaterno = StringVar()
    tbMaterno = StringVar()
    tbFInicio = StringVar()
    tbPeriodoT = StringVar()

    # Frame o Grid
    Top = Frame(gRegistro, bd=3, relief=RIDGE, width=1280, height=700)
    Top.pack(side=TOP, fill=X)
    Form = Frame(gRegistro, width=1280, height=700)
    Form.pack(side=TOP, pady=10)

    # Labels
    lbTitle = Label(Top, text="Worknesh: Panel de Registro", font=('arial black', 18))
    lbTitle.pack(fill=X)
    lbBusqueda = Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
    lbBusqueda.grid(row=0, sticky="e")
    lbCodigo = Label(Form, text = "Codigo:", font=('arial', 14), bd=15)
    lbCodigo.grid(row=1, sticky="e",column=1)
    lbNombre = Label(Form, text = "Nombre:", font=('arial', 14), bd=15)
    lbNombre.grid(row=2, sticky="e",column=1)
    lbPaterno = Label(Form, text = "Apellido Paterno:", font=('arial', 14), bd=15)
    lbPaterno.grid(row=3, sticky="e",column=1)
    lbMaterno = Label(Form, text = "Apellido Materno:", font=('arial', 14), bd=15)
    lbMaterno.grid(row=1, sticky="e",column=3)
    lbFInicio = Label(Form, text = "Fecha de inicio:", font=('arial', 14), bd=15)
    lbFInicio.grid(row=2, sticky="e",column=3)
    lbPeriodoT = Label(Form, text = "Periodo de trabajo:", font=('arial', 14), bd=15)
    lbPeriodoT.grid(row=3, sticky="e",column=3)
    lbl_text = Label(Form)
    lbl_text.grid(row=4, columnspan=3)

    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()

    # Text o Entrys
    tbBusqueda = Entry(Form, textvariable=tbBusqueda, font=(14))
    tbBusqueda.grid(row=0, column=1)
    tbCodigo = Entry(Form, textvariable=tbCodigo, font=(14))
    tbCodigo.grid(row=1, column=2)
    tbNombre = Entry(Form, textvariable=tbNombre, font=(14))
    tbNombre.grid(row=2, column=2)
    tbPaterno = Entry(Form, textvariable=tbPaterno, font=(14))
    tbPaterno.grid(row=3, column=2)
    tbMaterno = Entry(Form, textvariable=tbMaterno, font=(14))
    tbMaterno.grid(row=1, column=4)
    tbFInicio = Entry(Form, textvariable=tbFInicio, font=(14))
    tbFInicio.grid(row=2, column=4)
    tbPeriodoT = Entry(Form, textvariable=tbPeriodoT, font=(14))
    tbPeriodoT.grid(row=3, column=4)

    # Buttons
    btnAdd = Button(Form, text="Agregar Registro", width=80)
    btnAdd.grid(pady=25, row=4, columnspan=3)


def modVaca():
    global modVaca
    #gDash.withdraw()
    modVaca = Toplevel()
    modVaca.title("Worknes: Dashboard - Modulo de Vaca")
    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()
    width = 1280
    height = 700
    screen_height = root.winfo_screenwidth()
    screen_width = root.winfo_screenheight()
    x = (screen_width/1) - (width/1.7)
    y = (screen_height/15) - (height/15)
    modVaca.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #Dashboard.resizable(0, 0)

    # Variables
    tbTipo = StringVar()
    tbPeriodo = StringVar()
    tbAsistencia = StringVar()
    tbVacaciones= StringVar()
    tbDetalle = StringVar()

    # Frame o Grid
    Top = Frame(modVaca, bd=3, relief=RIDGE, width=1280, height=700)
    Top.pack(side=TOP, fill=X)
    Form = Frame(modVaca, width=1280, height=700)
    Form.pack(side=TOP, pady=10)

    # Labels
    lbTitle = Label(Top, text="Worknesh: Panel de Vacaciones", font=('arial black', 18))
    lbTitle.pack(fill=X)
    lbTipo = Label(Form, text = "Tipo:", font=('arial', 14), bd=15)
    lbTipo.grid(row=0, sticky="e")
    lbPeriodo = Label(Form, text = "Periodo:", font=('arial', 14), bd=15)
    lbPeriodo.grid(row=1, sticky="e",column=1)
    lbAsistencia = Label(Form, text = "Asistencia:", font=('arial', 14), bd=15)
    lbAsistencia.grid(row=2, sticky="e",column=1)
    lbVacaciones = Label(Form, text = "Vacaciones:", font=('arial', 14), bd=15)
    lbVacaciones.grid(row=1, sticky="e",column=3)
    lbDetalle = Label(Form, text = "Detalle:", font=('arial', 14), bd=15)
    lbDetalle.grid(row=2, sticky="e",column=3)
   
    lbl_text = Label(Form)
    lbl_text.grid(row=4, columnspan=3)

    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()

    # Text o Entrys
    tbTipo = Entry(Form, textvariable=tbTipo, font=(14))
    tbTipo.grid(row=0, column=1)
    tbPeriodo = Entry(Form, textvariable=tbPeriodo, font=(14))
    tbPeriodo.grid(row=1, column=2)
    tbAsistencia = Entry(Form, textvariable=tbAsistencia, font=(14))
    tbAsistencia.grid(row=2, column=2)
    tbVacaciones = Entry(Form, textvariable=tbVacaciones, font=(14))
    tbVacaciones.grid(row=1, column=4)
    tbDetalle = Entry(Form, textvariable=tbDetalle, font=(14))
    tbDetalle.grid(row=2, column=4)
   

    # Buttons
    btnAdd = Button(Form, text="Agregar Registro", width=80)
    btnAdd.grid(pady=25, row=4, columnspan=3)

  
def modAsistencia():
    global gAsistencia
    #gDash.withdraw()
    gAsistencia = Toplevel()
    gAsistencia.title("Worknes: Dashboard - Modulo de Asistencia")
    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()
    width = 1280
    height = 700
    screen_height = root.winfo_screenwidth()
    screen_width = root.winfo_screenheight()
    x = (screen_width/1) - (width/1.7)
    y = (screen_height/15) - (height/15)
    gAsistencia.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #Dashboard.resizable(0, 0)

    # Variables
    tbBusqueda = StringVar()
    tbCodigo = StringVar()
    tbNombre = StringVar()
    tbPaterno = StringVar()
    tbMaterno = StringVar()
    tbFechaActual = StringVar()
    tbPeriodoT = StringVar()

    # Frame o Grid
    Top = Frame(gAsistencia, bd=3, relief=RIDGE, width=1280, height=700)
    Top.pack(side=TOP, fill=X)
    Form = Frame(gAsistencia, width=1280, height=700)
    Form.pack(side=TOP, pady=10)

    # Labels
    lbTitle = Label(Top, text="Worknesh: Panel de Asistencia", font=('arial black', 18))
    lbTitle.pack(fill=X)
    lbBusqueda = Label(Form, text = "Busqueda:", font=('arial', 14), bd=15)
    lbBusqueda.grid(row=0, sticky="e")
    lbCodigo = Label(Form, text = "Codigo:", font=('arial', 14), bd=15)
    lbCodigo.grid(row=1, sticky="e",column=1)
    lbNombre = Label(Form, text = "Nombre:", font=('arial', 14), bd=15)
    lbNombre.grid(row=2, sticky="e",column=1)
    lbPaterno = Label(Form, text = "Apellido Paterno:", font=('arial', 14), bd=15)
    lbPaterno.grid(row=3, sticky="e",column=1)
    lbMaterno = Label(Form, text = "Apellido Materno:", font=('arial', 14), bd=15)
    lbMaterno.grid(row=1, sticky="e",column=3)
    lbFInicio = Label(Form, text = "Fecha Actual:", font=('arial', 14), bd=15)
    lbFInicio.grid(row=2, sticky="e",column=3)
    lbPeriodoT = Label(Form, text = "Periodo de trabajo:", font=('arial', 14), bd=15)
    lbPeriodoT.grid(row=3, sticky="e",column=3)
    lbl_text = Label(Form)
    lbl_text.grid(row=4, columnspan=3)

    foto = PhotoImage(file="LOGO.png")
    Label(root, image=foto).pack()

    # Text o Entrys
    tbBusqueda = Entry(Form, textvariable=tbBusqueda, font=(14))
    tbBusqueda.grid(row=0, column=1)
    tbCodigo = Entry(Form, textvariable=tbCodigo, font=(14))
    tbCodigo.grid(row=1, column=2)
    tbNombre = Entry(Form, textvariable=tbNombre, font=(14))
    tbNombre.grid(row=2, column=2)
    tbPaterno = Entry(Form, textvariable=tbPaterno, font=(14))
    tbPaterno.grid(row=3, column=2)
    tbMaterno = Entry(Form, textvariable=tbMaterno, font=(14))
    tbMaterno.grid(row=1, column=4)
    tbFInicio = Entry(Form, textvariable=tbFInicio, font=(14))
    tbFInicio.grid(row=2, column=4)
    tbPeriodoT = Entry(Form, textvariable=tbPeriodoT, font=(14))
    tbPeriodoT.grid(row=3, column=4)

    # Buttons
    btnAdd = Button(Form, text="Agregar Registro", width=80)
    btnAdd.grid(pady=25, row=4, columnspan=3)

def Back():
    gDash.destroy()
    root.deiconify()
    
#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
tbBusqueda = StringVar()
tbCodigo = StringVar()
tbNombre = StringVar()
tbApellido_paterno = StringVar()
tbApellido_materno = StringVar()
tbFecha_de_inicio = StringVar()
tbPerido_de_trabajo = StringVar()

#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#==============================LABELS=========================================
lbl_title = Label(Top, text = "Worknesh: Sistema de Login", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('times new roman', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('times new roman', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

root.mainloop()
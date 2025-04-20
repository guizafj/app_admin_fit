import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from app.cliente_dao import ClienteDAO
from app.cliente import Cliente

class App(tk.Tk):
    COLOR_VENTANA = "#1D2D44"

    def __init__(self): 
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        self.title("Sistema de Zona Fit")
        self.geometry("900x500")
        self.configure(background= App.COLOR_VENTANA)
        # aplicamos estilos a la ventana    
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') # Se preparan los estilos para el modo oscuro
        self.estilos.configure(self, background = App.COLOR_VENTANA, foreground='white', filebackground='black')
        self.estilos.configure('TEntry', foreground='white', fieldbackground='black')

    def configurar_grid(self):
        # Configuración del grid de la ventana
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)', font=('Arial', 20), background=  App.COLOR_VENTANA, foreground='white' )
        etiqueta.grid(row=0,column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_formulario = ttk.Frame(self)
        # nombre    
        nombre_l = ttk.Label(self.frame_formulario, text='nombre:') # se define la etiqueta nombre
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=20, padx=5) # se  asigna al grid para que se muestre
        self.nombre_t = ttk.Entry(self.frame_formulario) # se define el campo de texto
        self.nombre_t.grid(row=0, column=1, sticky=tk.W, pady=20, padx=5) # se asigna al grid para que se muestre
        # apellido
        apellido_l = ttk.Label(self.frame_formulario, text='Apellido:')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=20, padx=5)
        self.apellido_t = ttk.Entry(self.frame_formulario)
        self.apellido_t.grid(row=1, column=1, sticky=tk.W, pady=20, padx=5)
        # membresia
        membresia_l = ttk.Label(self.frame_formulario, text='Membresia')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=20, padx=5)
        self.membresia_t = ttk.Entry(self.frame_formulario)
        self.membresia_t.grid(row=2, column=1, sticky=tk.W, pady=20, padx=5)


        # publicar el frame del formulario
        self.frame_formulario.grid(row=1, column=0, padx=20)

    def cargar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        # definir los estilos de la tabla
        self.estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=25)
        # definir las columnas
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
        # crear el objeto tabla
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')
        # agregar encabezados a las columnas
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresia', anchor=tk.W)
        # Definir las columnas
        self.tabla.column('Id', width=50, anchor=tk.CENTER)
        self.tabla.column('Nombre', width=150, anchor=tk.W)
        self.tabla.column('Apellido', width=150, anchor=tk.W)
        self.tabla.column('Membresia', width=150, anchor=tk.W)

        # Asociar el evento select a la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)

        # agregar datos a la tabla  desde la base de datos
        clientes = ClienteDAO().seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.nombre, cliente.apellido, cliente.membresia))

        # agregar barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1, sticky='ns')

        #mostrar la tabla
        self.tabla.grid(row=0, column=0)
        #mostrar el frame de la tabla
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame(self)
        # boton agregar
        boton_agregar = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        boton_agregar.grid(row=0, column=0, pady=10, padx=30)

        # boton eliminar
        boton_eliminar  = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente)
        boton_eliminar.grid(row=0, column=1, pady=10, padx=30)
        
        # boton actualizar
        boton_limpiar = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar_datos)
        boton_limpiar.grid(row=0, column=2, pady=10, padx=30)

        # Aplicar estilos a los botones
        self.estilos.configure('TButton', background='#005f73', foreground='white')
        self.estilos.map('TButton', background=[('active', '#0a9396')], foreground=[('active', 'white')])

        # publicar el boton
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)
        
    def validar_cliente(self):
        # validar los campos
        if(self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atención', message='El campo membresia debe ser un numero')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus()
        else:
            showerror(title='Atención', message='Todos los campos son obligatorios')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except ValueError:
            return False

    def guardar_cliente(self):
        # recuperar los datos del formulario
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        # validar si el cliente ya existe
        if self.id_cliente is None:
            # crear el objeto cliente
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            # guardar el cliente en la base de datos
            ClienteDAO.insertar(cliente)
            showinfo(title='Atención', message='Cliente guardado correctamente')
            # Volver a mostar los datos y limpiar los campos
           
        else:
            cliente = Cliente(id=self.id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
            # actualizar el cliente en la base de datos
            ClienteDAO.actualizar(cliente)
            showinfo(title='Atención', message='Cliente actualizado correctamente')
        # recargar los datos
        self.recargar_datos()
        
    def cargar_cliente(self, event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values'] # tupla de valores del cliente seleccionado
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        # limpiar el formulario
        self.limpiar_formulario()
        # cargar los datos en el formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    def recargar_datos(self):
        self.cargar_tabla()
        self.limpiar_datos()

    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atención', message='Seleccione un cliente para eliminar')
        else:
            # eliminar el cliente de la base de datos
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Atención', message='Cliente eliminado correctamente')
            # recargar los datos
            self.recargar_datos()
    
    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None
        

    def limpiar_formulario(self):
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)
        

if __name__== '__main__':
    app = App()
    app.mainloop()
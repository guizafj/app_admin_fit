"""
Módulo app_zona_fit.py

Este módulo define la clase App, que implementa la interfaz gráfica de usuario (GUI) para el sistema
de gestión de clientes del gimnasio Zona Fit (GYM). Permite realizar operaciones CRUD sobre los clientes
a través de una interfaz intuitiva desarrollada con tkinter.

Autor: Francisco Javier Diaz Guiza
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from app.cliente_dao import ClienteDAO
from app.cliente import Cliente

class App(tk.Tk):
    """
    Clase principal de la aplicación GUI para Zona Fit (GYM).

    Hereda de tk.Tk y gestiona la ventana principal, los formularios, la tabla de clientes y los botones de acción.
    """

    COLOR_VENTANA = "#1D2D44"

    def __init__(self):
        """
        Inicializa la ventana principal y todos los componentes de la interfaz.
        """
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()

    def configurar_ventana(self):
        """
        Configura las propiedades de la ventana principal y los estilos generales.
        """
        self.title("Sistema de Zona Fit")
        self.geometry("900x500")
        self.configure(background=App.COLOR_VENTANA)
        # Estilos para modo oscuro
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam')
        self.estilos.configure(self, background=App.COLOR_VENTANA, foreground='white', filebackground='black')
        self.estilos.configure('TEntry', foreground='white', fieldbackground='black')

    def configurar_grid(self):
        """
        Configura el grid de la ventana principal para una mejor distribución de los widgets.
        """
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        """
        Muestra el título principal de la aplicación en la ventana.
        """
        etiqueta = ttk.Label(
            self,
            text='Zona Fit (GYM)',
            font=('Arial', 20),
            background=App.COLOR_VENTANA,
            foreground='white'
        )
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        """
        Muestra el formulario para ingresar o editar datos de un cliente.
        """
        self.frame_formulario = ttk.Frame(self)
        # Campo nombre
        nombre_l = ttk.Label(self.frame_formulario, text='Nombre:')
        nombre_l.grid(row=0, column=0, sticky=tk.W, pady=20, padx=5)
        self.nombre_t = ttk.Entry(self.frame_formulario)
        self.nombre_t.grid(row=0, column=1, sticky=tk.W, pady=20, padx=5)
        # Campo apellido
        apellido_l = ttk.Label(self.frame_formulario, text='Apellido:')
        apellido_l.grid(row=1, column=0, sticky=tk.W, pady=20, padx=5)
        self.apellido_t = ttk.Entry(self.frame_formulario)
        self.apellido_t.grid(row=1, column=1, sticky=tk.W, pady=20, padx=5)
        # Campo membresía
        membresia_l = ttk.Label(self.frame_formulario, text='Membresia:')
        membresia_l.grid(row=2, column=0, sticky=tk.W, pady=20, padx=5)
        self.membresia_t = ttk.Entry(self.frame_formulario)
        self.membresia_t.grid(row=2, column=1, sticky=tk.W, pady=20, padx=5)
        # Publicar el frame del formulario
        self.frame_formulario.grid(row=1, column=0, padx=20)

    def cargar_tabla(self):
        """
        Carga y muestra la tabla de clientes, obteniendo los datos desde la base de datos.
        """
        self.frame_tabla = ttk.Frame(self)
        # Estilos de la tabla
        self.estilos.configure('Treeview', background='black', foreground='white', fieldbackground='black', rowheight=25)
        # Definir columnas
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')
        # Encabezados
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresia', anchor=tk.W)
        # Definir ancho y alineación de columnas
        self.tabla.column('Id', width=50, anchor=tk.CENTER)
        self.tabla.column('Nombre', width=150, anchor=tk.W)
        self.tabla.column('Apellido', width=150, anchor=tk.W)
        self.tabla.column('Membresia', width=150, anchor=tk.W)
        # Evento de selección
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)
        # Insertar datos desde la base de datos
        clientes = ClienteDAO().seleccionar()
        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.nombre, cliente.apellido, cliente.membresia))
        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        # Mostrar tabla y frame
        self.tabla.grid(row=0, column=0)
        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        """
        Muestra los botones de acción (Guardar, Eliminar, Limpiar) y aplica estilos.
        """
        self.frame_botones = ttk.Frame(self)
        # Botón Guardar
        boton_agregar = ttk.Button(self.frame_botones, text='Guardar', command=self.validar_cliente)
        boton_agregar.grid(row=0, column=0, pady=10, padx=30)
        # Botón Eliminar
        boton_eliminar = ttk.Button(self.frame_botones, text='Eliminar', command=self.eliminar_cliente)
        boton_eliminar.grid(row=0, column=1, pady=10, padx=30)
        # Botón Limpiar
        boton_limpiar = ttk.Button(self.frame_botones, text='Limpiar', command=self.limpiar_datos)
        boton_limpiar.grid(row=0, column=2, pady=10, padx=30)
        # Estilos de botones
        self.estilos.configure('TButton', background='#005f73', foreground='white')
        self.estilos.map('TButton', background=[('active', '#0a9396')], foreground=[('active', 'white')])
        # Publicar el frame de botones
        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def validar_cliente(self):
        """
        Valida los campos del formulario antes de guardar o actualizar un cliente.
        """
        if self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get():
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atención', message='El campo membresia debe ser un número')
                self.membresia_t.delete(0, tk.END)
                self.membresia_t.focus()
        else:
            showerror(title='Atención', message='Todos los campos son obligatorios')
            self.nombre_t.focus_set()

    def validar_membresia(self):
        """
        Verifica que el campo membresía sea un número entero.

        Returns:
            bool: True si es un número, False en caso contrario.
        """
        try:
            int(self.membresia_t.get())
            return True
        except ValueError:
            return False

    def guardar_cliente(self):
        """
        Guarda un nuevo cliente o actualiza uno existente en la base de datos.
        """
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()
        if self.id_cliente is None:
            cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Atención', message='Cliente guardado correctamente')
        else:
            cliente = Cliente(id=self.id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Atención', message='Cliente actualizado correctamente')
        self.recargar_datos()

    def cargar_cliente(self, event):
        """
        Carga los datos del cliente seleccionado en la tabla al formulario para edición.

        Args:
            event: Evento de selección de la tabla.
        """
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values']
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]
        self.limpiar_formulario()
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    def recargar_datos(self):
        """
        Recarga los datos de la tabla y limpia el formulario.
        """
        self.cargar_tabla()
        self.limpiar_datos()

    def eliminar_cliente(self):
        """
        Elimina el cliente seleccionado de la base de datos.
        """
        if self.id_cliente is None:
            showerror(title='Atención', message='Seleccione un cliente para eliminar')
        else:
            cliente = Cliente(id=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Atención', message='Cliente eliminado correctamente')
            self.recargar_datos()

    def limpiar_datos(self):
        """
        Limpia el formulario y reinicia el identificador de cliente seleccionado.
        """
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        """
        Limpia los campos del formulario de entrada.
        """
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)

if __name__ == '__main__':
    app = App()
    app.mainloop()
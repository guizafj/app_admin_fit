"""
Módulo cliente.py

Define la clase Cliente, que representa la entidad cliente del sistema Zona Fit (GYM).
Incluye atributos privados, propiedades para acceso controlado y un método especial para
representación en cadena.

Autor: Francisco Javier Diaz Guiza
Fecha: 2025
"""


class Cliente:
    """
    Clase que representa un cliente del gimnasio.

    Atributos:
        id (int): Identificador único del cliente.
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        membresia (int): Tipo o número de membresía del cliente.
    """

    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        """
        Inicializa un nuevo objeto Cliente.

        Args:
            id (int, opcional): Identificador del cliente.
            nombre (str, opcional): Nombre del cliente.
            apellido (str, opcional): Apellido del cliente.
            membresia (int, opcional): Membresía del cliente.
        """
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__membresia = membresia

    @property
    def id(self):
        """int: Obtiene o establece el ID del cliente."""
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        """str: Obtiene o establece el nombre del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        """str: Obtiene o establece el apellido del cliente."""
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @property
    def membresia(self):
        """int: Obtiene o establece la membresía del cliente."""
        return self.__membresia

    @membresia.setter
    def membresia(self, membresia):
        self.__membresia = membresia

    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Cliente.

        Returns:
            str: Representación legible del cliente.
        """
        return (f'ID: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')
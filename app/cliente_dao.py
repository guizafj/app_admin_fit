"""
Módulo cliente_dao.py

Este módulo define la clase ClienteDAO, que implementa el patrón Data Access Object (DAO)
para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la tabla 'clientes'
en la base de datos. Utiliza la clase Conexion para gestionar la conexión y la clase Cliente
como modelo de datos.

Autor: Francisco Javier Diaz Guiza
Fecha: 2025
"""

from app.conexion import Conexion
from app.cliente import Cliente


class ClienteDAO:
    """
    Clase DAO para la entidad Cliente.
    Permite realizar operaciones CRUD sobre la tabla 'clientes'.
    """
    SELECCIONAR = "SELECT * FROM clientes ORDER BY id"
    INSERT = "INSERT INTO clientes (nombre, apellido, membresia) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM clientes WHERE id=%s"

    def __init__(self):
        """Constructor vacío (no se requiere inicialización especial)."""
        pass

    @classmethod
    def seleccionar(cls):
        """
        Recupera todos los registros de la tabla 'clientes' y los retorna como una lista de objetos Cliente.

        Returns:
            list[Cliente]: Lista de clientes recuperados de la base de datos.
        """
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Ocurrió un error al seleccionar los clientes: {e}")
            return []
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        """
        Inserta un nuevo cliente en la base de datos.

        Args:
            cliente (Cliente): Objeto Cliente a insertar.

        Returns:
            int: Número de filas afectadas (1 si la inserción fue exitosa).
        """
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al insertar el cliente: {e}")
            return 0
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        """
        Actualiza los datos de un cliente existente en la base de datos.

        Args:
            cliente (Cliente): Objeto Cliente con los datos actualizados.

        Returns:
            int: Número de filas afectadas (1 si la actualización fue exitosa).
        """
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al actualizar el cliente: {e}")
            return 0
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        """
        Elimina un cliente de la base de datos.

        Args:
            cliente (Cliente): Objeto Cliente a eliminar (se utiliza el atributo id).

        Returns:
            int: Número de filas afectadas (1 si la eliminación fue exitosa).
        """
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Ocurrió un error al eliminar el cliente: {e}")
            return 0
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)


"""
Módulo conexion.py

Este módulo define la clase Conexion, que gestiona el pool de conexiones a la base de datos MySQL
utilizando variables de entorno para la configuración. Permite obtener y liberar conexiones de manera eficiente.

Autor: Francisco Javier Diaz Guiza
Fecha: 2025
"""

from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os

class Conexion:
    """
    Clase para gestionar el pool de conexiones a la base de datos MySQL.
    Utiliza variables de entorno para la configuración y el patrón Singleton para el pool.
    """
    # Cargar variables de entorno al cargar la clase
    load_dotenv()
    DATABASE = os.getenv('DATABASE')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    DB_PORT = int(os.getenv('DB_PORT'))
    HOST = os.getenv('HOST')
    POOL_SIZE = int(os.getenv('POOL_SIZE'))
    POOL_NAME = os.getenv('POOL_NAME')
    pool = None

    @classmethod
    def obtener_pool(cls):
        """
        Obtiene el pool de conexiones. Si no existe, lo crea.

        Returns:
            MySQLConnectionPool: Pool de conexiones a la base de datos.

        Raises:
            Exception: Si ocurre un error al crear el pool.
        """
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                raise Exception(f"Error al obtener el pool de conexiones: {e}")
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        """
        Obtiene una conexión del pool.

        Returns:
            MySQLConnection: Conexión activa a la base de datos.
        """
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        """
        Libera una conexión, devolviéndola al pool.

        Args:
            conexion (MySQLConnection): Conexión a liberar.
        """
        conexion.close()


if __name__ == '__main__':
    # Prueba de conexión y pool
    pool = Conexion.obtener_pool()
    print(f'Se obtuvo la conexión: {pool}')
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print('Se ha liberado el objeto conexion1')

    # Mostrar configuración cargada
    print(f"DATABASE: {Conexion.DATABASE}")
    print(f"USERNAME: {Conexion.USERNAME}")
    print(f"PASSWORD: {Conexion.PASSWORD}")
    print(f"DB_PORT: {Conexion.DB_PORT}")
    print(f"HOST: {Conexion.HOST}")
    print(f"POOL_SIZE: {Conexion.POOL_SIZE}")
    print(f"POOL_NAME: {Conexion.POOL_NAME}")
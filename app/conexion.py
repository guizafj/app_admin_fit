from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os

class Conexion:
    # Cargar variables de entorno
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
        if cls.pool is None:  # Se crea el objeto pool
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
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print('Se ha liberado el objeto conexion1')

    print(f"DATABASE: {Conexion.DATABASE}")
    print(f"USERNAME: {Conexion.USERNAME}")
    print(f"PASSWORD: {Conexion.PASSWORD}")
    print(f"DB_PORT: {Conexion.DB_PORT}")
    print(f"HOST: {Conexion.HOST}")
    print(f"POOL_SIZE: {Conexion.POOL_SIZE}")
    print(f"POOL_NAME: {Conexion.POOL_NAME}")
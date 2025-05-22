# 🏋️‍♂️ Sistema de Gestión Zona Fit (GYM)

Zona Fit es una aplicación de escritorio desarrollada en Python utilizando Tkinter como interfaz gráfica. Permite gestionar clientes y sus membresías en un gimnasio de manera sencilla y eficiente. Este proyecto fue creado como parte de los laboratorios de formación en Python, y está diseñado para demostrar habilidades en desarrollo de software, manejo de bases de datos y creación de interfaces gráficas.

## 🚀 Características Principales

- **👥 Gestión de Clientes**: Registro, edición y eliminación de información de clientes.
- **📅 Control de Membresías**: Seguimiento de membresías activas, fechas de vencimiento y renovaciones. (O-D)
- **📋 Listado de Clientes**: Visualización de todos los clientes registrados en una tabla interactiva.
- **🔍 Búsqueda y Filtros**:  Funcionalidades para buscar y filtrar clientes según diferentes criterios.(O-D)
- **🎨 Interfaz Intuitiva**: Diseñada con `tkinter` para una experiencia de usuario sencilla y funcional. (P-M)

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.8+
- **Base de datos**: MySQL
- **Control de Versiones**: Git
- **Librerías**:
  - `tkinter`: Para la interfaz gráfica.
  - `mysql-connector-python`: Para la conexión con la base de datos.
  - `python-dotenv`: Para la gestión de variables de entorno.

## 📋 Requisitos

- Python 3.8 o superior.
- MySQL Server instalado y configurado.
- Las dependencias del proyecto (ver `requirements.txt`).

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/guizafj/app_admin_fit.git
   cd app_admin_fit
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno en un archivo `.env`:
   ```plaintext
   DATABASE=zona_fit_db
   USERNAME=tu_usuario
   PASSWORD=tu_contraseña
   DB_PORT=3306
   HOST=localhost
   POOL_SIZE=5
   POOL_NAME=zona_fit_pool
   ```

4. Crea la base de datos y la tabla necesaria:
   ```sql
   CREATE DATABASE zona_fit_db;

   USE zona_fit_db;

   CREATE TABLE clientes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nombre VARCHAR(100) NOT NULL,
       apellido VARCHAR(100) NOT NULL,
       membresia INT NOT NULL
   );
   ```

5. Ejecuta la aplicación:
   ```bash
   python app_zona_fit.py
   ```

## 📈 Futuras Mejoras

Este proyecto está en constante desarrollo. Algunas de las mejoras planeadas incluyen:

- **Validación de datos**: Implementar validaciones más robustas en los formularios.
- **Reportes**: Generar reportes en PDF o Excel con los datos de los clientes.
- **Soporte para múltiples usuarios**: Añadir autenticación y roles de usuario.
- **Diseño responsivo**: Mejorar la interfaz gráfica para adaptarse a diferentes resoluciones.
- **Internacionalización**: Soporte para múltiples idiomas.

## 📂 Estructura del Proyecto

```
app_admin_fit/
├── app/
│   ├── __init__.py
│   ├── cliente.py          # Clase Cliente
│   ├── cliente_dao.py      # Acceso a datos para Cliente
│   └── conexion.py         # Manejo de la conexión a la base de datos
├── app_zona_fit.py         # Archivo principal de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno (no se sube a GitHub)
├── README.md               # Documentación del proyecto
├── .gitignore              # Archivos y carpetas a ignorar en Git
```
## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar:

    Haz un fork del repositorio.

    Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

    Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').

    Sube tus cambios a tu fork (git push origin feature/nueva-funcionalidad).

    Abre un Pull Request describiendo tus cambios.



## 🧑‍💻 Autor

Este proyecto fue desarrollado por **[Francisco Javier Diaz Guiza](https://github.com/guizafj)** como parte de los laboratorios de formación en Python. Puedes encontrar más información sobre mí en mi [perfil de GitHub](https://github.com/guizafj).

## 📬 Contacto
   Correo: contacto@dguiza.dev

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por visitar este proyecto! Si tienes alguna sugerencia o deseas contribuir, no dudes en abrir un issue o enviar un pull request.
Requerimientos de instalación:
------------------------------------------------------------------------------------------------------------

1-Requisitos previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

Python 3.8 o superior
Puedes verificar tu versión de Python con el siguiente comando en la terminal o consola:
/python --version/
Si aparece algo como Python 3.10.8, significa que ya está instalado correctamente.

------------------------------------------------------------------------------------------------------------

2-Crear un entorno virtual (opcional pero recomendado)

Un entorno virtual te permite instalar las librerías necesarias sin afectar otros proyectos que tengas en tu computadora.
Para crear uno, ejecuta en la terminal (dentro de la carpeta del proyecto) el siguiente codigo
python -m venv venv

Luego lo activas con este codigo 
venv\Scripts\activate

------------------------------------------------------------------------------------------------------------

3-Instalar las librerías necesarias

Este proyecto utiliza la librería PrettyTable, que permite mostrar tablas formateadas en la consola.
Puedes instalarla de dos formas:

------------------------------------------------------------------------------------------------------------

Opción A: Instalar directamente con pip

Ejecuta el siguiente comando:
pip install prettytable
Esto descargará e instalará automáticamente la librería desde el repositorio oficial de Python (PyPI).

------------------------------------------------------------------------------------------------------------

Opción B: Usar el archivo requirements.txt

También puedes crear un archivo llamado requirements.txt dentro de tu proyecto, con el siguiente contenido:
prettytable
Luego, instala todas las dependencias listadas en ese archivo ejecutando:
pip install -r requirements.txt
Esto es muy útil cuando otros usuarios quieren clonar o ejecutar tu proyecto, ya que solo necesitan 
correr un comando para instalar todo lo necesario.

------------------------------------------------------------------------------------------------------------

4-Verificación de la instalación

Una vez completada la instalación, puedes verificar que la librería se haya instalado correctamente ejecutando en la terminal:
pip show prettytable
Si la instalación fue exitosa, verás información similar a:
Name: prettytable
Version: 3.10.0
Summary: A simple Python library for easily displaying tabular data in a visually appealing ASCII table format.

------------------------------------------------------------------------------------------------------------

5-Ejecución del programa

Cuando todas las librerías estén instaladas, simplemente ejecuta el programa con:
python codigo.py
o ejecutandolo de la forma tradicionaly te tendria que apareces una tabla bien diseñada como tu la quieras.

------------------------------------------------------------------------------------------------------------

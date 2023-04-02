Más idiomas: <kbd>[<img title="Leer en inglés" alt="Leer en inglés" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/gb.svg" height="15">](translations/README.en.md)</kbd>  &emsp;
Seguime en <kbd>[<img title="Mi perfil en LinkedIn" alt="Mi perfil en LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="15">](https://www.linkedin.com/in/martinezjesusfl/)</kbd>

# Script de descarga de datasets de Uknown Datasets

**Tecnologías usadas:**  
<img title="Python" alt="Python" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" height="20"> &emsp;
<img title="HTML" alt="HTML" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" height="20"> &emsp;

## Descripción
Este proyecto se encarga de descargar automáticamente los datasets subidos a la página de [Unknown Datasets](https://linktr.ee/unknow.datasets) y redirigirte a su Cafecito para que les des tu apoyo!  
Esta versión inicial tiene solo el script de Python. A medida que pase el tiempo (y en la medida de mi tiempo disponible xD) vamos a convertirlo en un proceso más robusto.  
Por el momento descarto la idea de que tenga una interfaz porque para eso ya está la propia página de [Unknown Datasets](https://linktr.ee/unknow.datasets). Pero podemos orquestar esta automatización con [Prefect](https://www.prefect.io/). 

## Inventario
En este repositorio se encuentran los siguientes archivos:
- ```requirements.txt``` para instalar las librerías que usa el script
- ```exportar_unknown_datasets.py``` para correr el script
- ```exportar_unknown_datasets.ipynb``` es el jupyter notebook con las notas del proceso de desarrollo
- ```.gitignore``` para dejar fuera del repositorio los archivos generados y el entorno virtual

## Instrucciones
1. Preparamos el entorno de trabajo:  
``````powershell
python -m venv unknown_datasets_env
``````

2. Instalamos las librerías
``````powershell
pip install -r requirements.txt
``````

3. Corremos el script
``````powershell
python exportar_unknown_datasets.py
``````

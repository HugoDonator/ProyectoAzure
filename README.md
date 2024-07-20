# Proyecto Azure

Este proyecto tiene como objetivo automatizar la clasificación de imágenes de devolución de calzado utilizando Azure Custom Vision. La aplicación proporciona una interfaz gráfica para gestionar imágenes de calzado y clasificarlas utilizando un modelo entrenado en Azure Custom Vision. Además, se conecta a una base de datos local en SQL Server para almacenar y recuperar información sobre las imágenes procesadas.

## Descripción

La aplicación permite a los usuarios cargar imágenes de calzado, clasificarlas y almacenar los resultados en una base de datos SQL Server. La interfaz gráfica está desarrollada con `customtkinter` y utiliza `PIL` para manejar las imágenes. Los resultados de la clasificación se muestran en la interfaz y se almacenan en la base de datos para su posterior análisis.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Requisitos

Para ejecutar este proyecto, necesitarás las siguientes dependencias:

- Python 3.8 o superior
- `customtkinter`
- `tkinter`
- `PIL` (Pillow)
- `requests`
- `pyodbc`

Estas dependencias están listadas en el archivo `requirements.txt`.

## Instalación

Sigue estos pasos para instalar y configurar el proyecto en tu entorno local:

1. **Clona el Repositorio**

   Clona el repositorio usando el siguiente comando:

   ```sh
   git clone https://github.com/HugoDonator/ProyectoAzure.git

2.**Crea y Activa un Entorno Virtual**

    Navega al directorio del proyecto y crea un entorno virtual:

   cd ProyectoAzure
   python -m venv venv

2.**Instala las Dependencias**

    Con el entorno virtual activado, instala las dependencias desde el archivo requirements.txt:

   pip install -r requirements.txt

**Uso**
 Para ejecutar la aplicación:

 ..Prepara las Imágenes

 Asegúrate de tener los archivos de imagen necesarios (zapatoej.webp, tacosej.webp, etc.) en el directorio del proyecto.


# Configuración de la Base de Datos para Proyecto Azure

Este documento proporciona instrucciones sobre cómo configurar y gestionar la base de datos SQL Server utilizada por la aplicación en el proyecto **Proyecto Azure**.

## Descripción

La base de datos **devolucion** se utiliza para almacenar información sobre las solicitudes de devolución de calzado y los tipos de calzado. La base de datos contiene las tablas `TiposCalzado` y `SolicitudesDevolucion`.

## Configuración de SQL Server

### 1. Crear la Base de Datos

Ejecuta el siguiente script en SQL Server Management Studio (SSMS) para crear la base de datos y las tablas necesarias:

```sql
-- Crear la base de datos 'devolucion'
CREATE DATABASE devolucion;
GO

-- Usar la base de datos 'devolucion'
USE devolucion;
GO

-- Crear la tabla 'TiposCalzado'
CREATE TABLE TiposCalzado (
    TipoCalzadoID INT PRIMARY KEY IDENTITY(1,1),
    Descripcion NVARCHAR(50) UNIQUE
);

-- Crear la tabla 'SolicitudesDevolucion'
CREATE TABLE SolicitudesDevolucion (
    SolicitudID INT PRIMARY KEY IDENTITY(1,1),
    TipoCalzadoIndicadoID INT FOREIGN KEY REFERENCES TiposCalzado(TipoCalzadoID),
    Imagen NVARCHAR(255), -- Ruta o nombre de archivo de la imagen
    FechaSolicitud DATETIME DEFAULT GETDATE()
);

-- Insertar datos iniciales en la tabla 'TiposCalzado'
INSERT INTO TiposCalzado (Descripcion) VALUES ('sandalias');
INSERT INTO TiposCalzado (Descripcion) VALUES ('tenis');
INSERT INTO TiposCalzado (Descripcion) VALUES ('zapatos');
INSERT INTO TiposCalzado (Descripcion) VALUES ('tacones');
INSERT INTO TiposCalzado (Descripcion) VALUES ('botas');

-- Consultar datos de las tablas
SELECT 
    s.SolicitudID,
    t.Descripcion AS TipoCalzado,
    s.Imagen,
    s.FechaSolicitud
FROM 
    SolicitudesDevolucion s
JOIN 
    TiposCalzado t
ON 
    s.TipoCalzadoIndicadoID = t.TipoCalzadoID;

# Configurar la Conexión en el Código

**Asegúrate de actualizar el archivo ProyectoAzure.py con la cadena de conexión correcta para tu base de datos. Aquí hay un ejemplo de cómo podría verse la cadena de conexión:

 r"DRIVER={SQL Server};"
 r"SERVER=nombre_del_servidor;;"
 r"DATABASE=devolucion;"
 r"Trusted_Connection=yes;
  


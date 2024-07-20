CREATE DATABASE devolucion;
GO

-- Usar la base de datos 'devolucion'
USE devolucion;
GO


CREATE TABLE TiposCalzado (
    TipoCalzadoID INT PRIMARY KEY IDENTITY(1,1),
    Descripcion NVARCHAR(50) UNIQUE
);

CREATE TABLE SolicitudesDevolucion (
    SolicitudID INT PRIMARY KEY IDENTITY(1,1),
    TipoCalzadoIndicadoID INT FOREIGN KEY REFERENCES TiposCalzado(TipoCalzadoID),
    Imagen NVARCHAR(255), -- Ruta o nombre de archivo de la imagen
    FechaSolicitud DATETIME DEFAULT GETDATE()
);

INSERT INTO TiposCalzado (Descripcion) VALUES ('sandalias');
INSERT INTO TiposCalzado (Descripcion) VALUES ('tenis');
INSERT INTO TiposCalzado (Descripcion) VALUES ('zapatos');
INSERT INTO TiposCalzado (Descripcion) VALUES ('tacones');
INSERT INTO TiposCalzado (Descripcion) VALUES ('botas');

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


delete from SolicitudesDevolucion
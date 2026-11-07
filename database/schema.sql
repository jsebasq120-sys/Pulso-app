CREATE DATABASE pulso_db;
GO

USE pulso_db;
GO

CREATE TABLE USUARIO (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL
);

CREATE TABLE JUGADOR (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    posicion VARCHAR(50),
    edad INT,
    numero_camiseta INT,
    usuario_id INT FOREIGN KEY REFERENCES USUARIO(id)
);

CREATE TABLE MEDICION (
    id INT IDENTITY(1,1) PRIMARY KEY,
    jugador_id INT FOREIGN KEY REFERENCES JUGADOR(id),
    frecuencia_cardiaca INT,
    fatiga_nivel INT,
    velocidad_maxima FLOAT,
    fecha_registro DATETIME DEFAULT GETDATE()
);

CREATE TABLE PRUEBA_FISICA (
    id INT IDENTITY(1,1) PRIMARY KEY,
    jugador_id INT FOREIGN KEY REFERENCES JUGADOR(id),
    tipo_prueba VARCHAR(100),
    resultado FLOAT,
    fecha DATETIME DEFAULT GETDATE()
);

CREATE TABLE ANOTACION (
    id INT IDENTITY(1,1) PRIMARY KEY,
    jugador_id INT FOREIGN KEY REFERENCES JUGADOR(id),
    partido VARCHAR(100),
    minuto INT,
    descripcion TEXT
);
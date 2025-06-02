CREATE DATABASE IF NOT EXISTS municipalidad_yau_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE municipalidad_yau_db;

CREATE TABLE ciudadano (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dni VARCHAR(12) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL
);

CREATE TABLE tramite (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ciudadano_id INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    descripcion TEXT,
    urgente BOOLEAN DEFAULT FALSE,
    fecha_creacion DATETIME NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE',
    FOREIGN KEY (ciudadano_id) REFERENCES ciudadano(id)
);

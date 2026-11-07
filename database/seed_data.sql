USE pulso_db;
GO

INSERT INTO USUARIO (nombre, email, password, rol) 
VALUES ('Profe Carlos', 'carlos@pulso.com', '123456', 'Entrenador');

INSERT INTO JUGADOR (nombre, posicion, edad, numero_camiseta, usuario_id) 
VALUES 
('Juan Quintero', 'Mediocampista', 20, 10, 1),
('Mateo Uribe', 'Volante', 22, 8, 1),
('David Ospina', 'Arquero', 25, 1, 1);

INSERT INTO MEDICION (jugador_id, frecuencia_cardiaca, fatiga_nivel, velocidad_maxima) 
VALUES 
(1, 165, 3, 28.5),
(2, 172, 4, 31.2),
(3, 150, 2, 24.0);

INSERT INTO PRUEBA_FISICA (jugador_id, tipo_prueba, resultado) 
VALUES 
(1, 'Test de Cooper (Metros)', 2800),
(2, 'Salto Vertical (cm)', 55.5),
(3, 'Sprint 30 metros (Segundos)', 4.12);
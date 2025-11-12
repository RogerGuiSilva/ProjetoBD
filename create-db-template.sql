CREATE DATABASE todolist


CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

INSERT INTO tarefas (name, description) VALUES
('estudar python', 'estudar python'),
('programar css', 'to estudando css'),
('Aprender JavaScript', 'Aprender JS para ser feliz');





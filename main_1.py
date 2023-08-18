import sqlite3

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("Drop table Estudantes")
conn.commit()
# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automaticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    "Ano de Ingresso" INTEGER
);
""")

estudantes = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, "Ano de Ingresso")
VALUES (?, ?, ?);
""", estudantes)

conn.commit()

# cursor.execute("SELECT * FROM Estudantes WHERE [Ano de Ingresso] > 2019 AND Curso = 'Computação'")
# print(cursor.fetchall())
# conn.commit()


cursor.execute("UPDATE Estudantes SET 'Ano de Ingresso' = ? WHERE ID = ?", (2020, 2))
print(cursor.fetchall())
conn.commit()

# cursor.execute("SELECT * FROM Estudantes WHERE [Ano de Ingresso] = 2020")
# print(cursor.fetchall())
# conn.commit()

# cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (1,))
# print(cursor.fetchall())
# conn.commit()

# cursor.execute("SELECT * FROM Estudantes")
# # O método fetchall() recupera todos os registros resultantes da consulta.
# print(cursor.fetchall())

# cursor.execute("UPDATE Estudantes SET 'Ano de Ingresso' = ? WHERE Curso = ?", (2018, "Computação"))
# print(cursor.fetchall())
# conn.commit()

cursor.execute("SELECT * FROM Estudantes")
# O método fetchall() recupera todos os registros resultantes da consulta.
print(cursor.fetchall())
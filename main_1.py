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

# --------------------------------------------------------------------------------------------------------
('''Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive)
 e exiba no console. Use o comando WHERE para realizar essa filtragem.''')
cursor.execute("SELECT * FROM Estudantes WHERE [Ano de Ingresso] >= 2019 AND [Ano de Ingresso] <= 2020")
print(cursor.fetchall())
conn.commit()

# --------------------------------------------------------------------------------------------------------
('''Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019.''')
cursor.execute("SELECT * FROM Estudantes WHERE [Ano de Ingresso] > 2019 AND Curso = 'Computação'")
print(cursor.fetchall())
conn.commit()

# --------------------------------------------------------------------------------------------------------
('''Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.''')
cursor.execute("UPDATE Estudantes SET 'Ano de Ingresso' = ? WHERE ID = ?", (2020, 2))
conn.commit()

cursor.execute("SELECT * FROM Estudantes WHERE [Ano de Ingresso] = 2020")
print(cursor.fetchall())
conn.commit()

# --------------------------------------------------------------------------------------------------------
('''Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.''')
cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (1,))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

# --------------------------------------------------------------------------------------------------------
('''Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.''')
cursor.execute("SELECT * FROM Estudantes WHERE [Ano de Ingresso] > 2019 AND curso = 'Computação' ")
print(cursor.fetchall())
conn.commit()

# --------------------------------------------------------------------------------------------------------
('''
Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, 
crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. 
Mostre por todos estudantes novamente
''')
cursor.execute("UPDATE Estudantes SET 'Ano de Ingresso' = ? WHERE Curso = ?", (2018, "Computação"))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())
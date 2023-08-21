from db.db_utils import *

nome_tabela = "Estudantes"
dados = [
    ("Ana Silva", "Computação", 2019),
    ("Pedro Mendes", "Física", 2021),
    ("Carla Souza", "Computação", 2020),
    ("João Alves", "Matemática", 2018),
    ("Maria Oliveira", "Química", 2022)
]
informacoes = ["Nome", "Curso", "Ano_de_Ingresso"]
conn, cursor = create_table(informacoes, nome_tabela, dados)

#Mostrar a tabela
# cursor.execute("SELECT * FROM Estudantes")
# print(cursor.fetchall())

#Filtra usando select
# filtro = "Ano_de_Ingresso > 2019 AND Curso = 'Computação'"
# select(conn, cursor, filtro)

filtro = " 'Ano_de_Ingresso' = ? WHERE ID = ?", (2020, 2) "
update(conn, cursor, filtro, nome_tabela)
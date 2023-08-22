from db.db_utils import *


"""
 Crie uma tabela chamada "Estudantes" com os seguintes campos:

# - **ID (chave primária)**
# - **Nome**
# - **Curso**
# - **Ano de Ingresso**

# Insira 5 registros de estudantes na tabela. Inclua os seguintes estudantes fictícios como parte desses registros:
 """

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

# --------------------------------------------------------------------------
"""
**Selecione e mostre todos os registros da tabela no console.**
"""
# Mostrar a tabela
cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

# --------------------------------------------------------------------------
'''
- Filtre e mostre os estudantes que ingressaram entre 2019 e 2020 (inclusive) e exiba no console. 
Use o comando WHERE para realizar essa filtragem.
'''
#Filtra usando select
filtro = "Ano_de_Ingresso >= 2019"
select(conn, cursor, filtro, nome_tabela)

# ----------------------------------------------------------------------------
'''
- Atualize o "Ano de Ingresso" de um estudante específico. Mostre por todos estudantes novamente.
'''
# Altera um valor
valor_alterado = "Ano_de_Ingresso"
where = "ID"
valores = (2020, 2)
update(conn, cursor, valores, nome_tabela, valor_alterado, where)

# ----------------------------------------------------------------------------
'''
- Delete um registro da tabela usando o ID do estudante. Mostre por todos estudantes novamente.
'''
# Delete
filtro = "ID"
valor = (1,)
delete(conn, cursor, nome_tabela, filtro, valor)

# -----------------------------------------------------------------------------
'''
- Filtre e mostre os estudantes do Curso de Computação que ingressaram após 2019. Mostre o resultado.
'''
filtro = "Ano_de_Ingresso > 2019 AND curso = 'Computação'"
select(conn, cursor, filtro, nome_tabela)

# ------------------------------------------------------------------------------

'''
- Imagine que alguém errou nos registros de ingresso de todos os alunos do curso de Computação, 
crie uma query que altere todos os registros dos alunos de Computação, campo ingresso para 2018. 
Mostre por todos estudantes novamente.
'''

valor_alterado = "Ano_de_Ingresso"
where = "Curso"
valores = (2018, "Computação")
update(conn, cursor, valores, nome_tabela, valor_alterado, where)


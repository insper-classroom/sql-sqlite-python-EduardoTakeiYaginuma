import sqlite3

def create_table(informacoes,nome_tabela, dados):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()

    cursor.execute(f"Drop table {nome_tabela}")
    conn.commit()

    cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {nome_tabela} (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    {informacoes[0]} TEXT NOT NULL,
    {informacoes[1]} TEXT NOT NULL,
    {informacoes[2]} INTEGER
);
""")

    cursor.executemany(f"""
INSERT INTO {nome_tabela} ({informacoes[0]}, {informacoes[1]}, {informacoes[2]})
VALUES (?, ?, ?);
""", dados)

    conn.commit()
    return conn,cursor


def select(conn, cursor, filtro):
    cursor.execute(f"SELECT * FROM Estudantes WHERE {filtro}")
    print(cursor.fetchall())
    conn.commit()



def update(conn, cursor, filtro, nome_tabela):
    cursor.execute(f"UPDATE {nome_tabela} SET {filtro}")
    print(cursor.fetchall())
    conn.commit()




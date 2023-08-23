import sqlite3

def mostra_tabela(conn, cursor, nome_tabela):
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    print(cursor.fetchall())
    conn.commit()

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


def select(conn, cursor, filtro, nome_tabela):
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE {filtro}")
    print(cursor.fetchall())
    conn.commit()



def update(conn, cursor, valores, nome_tabela, valor_alterado, identificacao_where):
    query = f"UPDATE {nome_tabela} SET {valor_alterado} = ? WHERE {identificacao_where} = ?"
    cursor.execute(query, valores)
    mostra_tabela(conn, cursor, nome_tabela)




def delete(conn, cursor, nome_tabela,filtro, valor):
    query = (f"DELETE FROM {nome_tabela} WHERE {filtro} = ?")
    cursor.execute(query, valor)
    mostra_tabela(conn, cursor, nome_tabela)


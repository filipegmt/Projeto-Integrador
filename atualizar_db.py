import sqlite3

def adicionar_tabelas_autenticacao():
    conn = sqlite3.connect('app_reservas.db')
    cursor = conn.cursor()

    # Cria a tabela de Utilizadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilizadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Cria a tabela de Reservas 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            restaurante_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            num_pessoas INTEGER NOT NULL,
            status TEXT DEFAULT 'Confirmada',
            FOREIGN KEY (user_id) REFERENCES utilizadores (id),
            FOREIGN KEY (restaurante_id) REFERENCES restaurantes (id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Estrutura da base de dados atualizada com sucesso!")

if __name__ == "__main__":
    adicionar_tabelas_autenticacao()
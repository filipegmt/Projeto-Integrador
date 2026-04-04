import json
from bs4 import BeautifulSoup
import sqlite3

# 1. Lista com os nomes dos ficheiros gravados na pasta
ficheiros_cidades = [
    'dados_lisboa.html', 
    'dados_porto.html', 
    'dados_setubal.html', 
    'dados_faro.html'
]

conexao = sqlite3.connect('restaurantes.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE, 
        morada TEXT,
        cidade TEXT,
        preco TEXT,
        avaliacao TEXT,
        cozinhas TEXT
    )
''')

# 2. O Python percorre cada ficheiro da lista
for nome_ficheiro in ficheiros_cidades:
    print(f"\nA iniciar a leitura do ficheiro: {nome_ficheiro}...")
    
    try:
        # Abre o ficheiro correspondente
        with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
            html = ficheiro.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        script_jsonld = soup.find('script', id='restaurant_jsonld')
        
        if script_jsonld:
            dados_json = json.loads(script_jsonld.string)
            lista_restaurantes = dados_json.get("itemListElement", [])
            
            print(f"Sucesso! A inserir {len(lista_restaurantes)} restaurantes...")
            
            for elemento in lista_restaurantes:
                try:
                    restaurante = elemento["item"]
                    nome = restaurante.get("name", "Nome indisponível")
                    morada = restaurante["address"].get("streetAddress", "Morada indisponível")
                    cidade = restaurante["address"].get("addressLocality", "")
                    preco = restaurante.get("priceRange", "Preço indisponível")
                    
                    nota = "Sem avaliação"
                    if "aggregateRating" in restaurante:
                        nota = restaurante["aggregateRating"].get("ratingValue", "Sem avaliação")
                    
                    cozinhas = "Não especificado"
                    if "servesCuisine" in restaurante:
                        if isinstance(restaurante["servesCuisine"], list):
                            cozinhas = ", ".join(restaurante["servesCuisine"])
                        else:
                            cozinhas = restaurante["servesCuisine"]

                    # O INSERT OR IGNORE garante que, se um restaurante de Lisboa voltar a aparecer, ele não duplica
                    cursor.execute('''
                        INSERT OR IGNORE INTO restaurantes (nome, morada, cidade, preco, avaliacao, cozinhas)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (nome, morada, cidade, preco, nota, cozinhas))
                    
                except KeyError:
                    pass
        else:
            print("Aviso: Bloco JSON-LD não existe neste ficheiro.")
            
    except FileNotFoundError:
        # Se te esqueceres de criar um ficheiro, o script não bloqueia. Dá apenas um aviso.
        print(f"Aviso: O ficheiro '{nome_ficheiro}' ainda não foi criado na pasta. O script vai passar ao próximo.")

conexao.commit()
conexao.close()
print("\nProcesso concluído! A tua base de dados tem restaurantes de várias cidades e está pronta para o n8n.")
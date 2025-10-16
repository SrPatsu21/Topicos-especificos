import psycopg2

# Dados de conexão (ajuste conforme seu docker-compose)
conn = psycopg2.connect(
    dbname="meubanco",
    user="usuario",
    password="senha",
    host="postgres-db",  # nome do serviço no docker-compose
    port="5432"
)

cur = conn.cursor()

# Exemplo: criar tabela e inserir dados
cur.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100),
        curso VARCHAR(100)
    );
""")
cur.execute("""
    INSERT INTO alunos (nome, curso) VALUES
    ('Ana', 'Computação'),
    ('Bruno', 'Computação');
""")
conn.commit()

# Consulta SQL
cur.execute("SELECT * FROM alunos;")
resultados = cur.fetchall()

for linha in resultados:
    print(linha)

cur.close()
conn.close()

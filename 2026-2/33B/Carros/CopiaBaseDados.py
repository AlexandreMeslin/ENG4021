#!/usr/bin/env python
import sqlite3
from typing import List, Tuple

# --- Configurações ---
DB_ORIGEM = 'mtcars.sqlite3'
DB_DESTINO = 'db.sqlite3'
NOME_TABELA = 'MTCars'

# Colunas (excluindo 'id', que é Autoincremento e será gerado no destino)
COLUNAS = [
    'NAME', 'MPG', 'CYL', 'DISP', 'HP', 'WT', 'QSEC', 'VS', 'AM', 'GEAR'
]

# A string de colunas para o SQL (ex: NAME, MPG, CYL, ...)
COLUNAS_SQL = ', '.join(COLUNAS) 

# A string de placeholders para o SQL de inserção (ex: ?, ?, ?, ...)
PLACEHOLDERS_SQL = ', '.join(['?'] * len(COLUNAS))

def ler_dados_origem(db_origem: str, tabela: str, colunas: List[str]) -> List[Tuple]:
    """
    Conecta ao banco de dados de origem e lê todos os registros da tabela MTCars.
    Retorna uma lista de tuplas com os dados lidos.
    :param db_origem: Caminho para o banco de dados de origem.
    :param tabela: Nome da tabela a ser lida.
    :param colunas: Lista de colunas a serem lidas.
    :return: Lista de tuplas com os dados lidos.
    """
    print(f"Conectando ao banco de origem: {db_origem}...")
    try:
        conn_origem = sqlite3.connect(db_origem)
        cursor = conn_origem.cursor()
        
        # Seleciona todas as colunas necessárias
        sql_select = f"SELECT {COLUNAS_SQL} FROM {tabela}"
        
        cursor.execute(sql_select)
        dados = cursor.fetchall()
        
        conn_origem.close()
        print(f"Leitura concluída. {len(dados)} registros lidos.")
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao ler do banco de dados de origem: {e}")
        return []

def inserir_dados_destino(db_destino: str, tabela: str, colunas: List[str], dados: List[Tuple]):
    """
    Conecta ao banco de dados de destino e insere os registros lidos.
    :param db_destino: Caminho para o banco de dados de destino.
    :param tabela: Nome da tabela onde os dados serão inseridos.
    :param colunas: Lista de colunas onde os dados serão inseridos.
    :param dados: Lista de tuplas com os dados a serem inseridos.
    :return: None
    """
    if not dados:
        print("Nenhum dado para inserir. Abortando.")
        return
        
    print(f"Conectando ao banco de destino: {db_destino}...")
    try:
        conn_destino = sqlite3.connect(db_destino)
        cursor = conn_destino.cursor()

        # SQL de inserção (note que não incluímos o 'id', pois ele é AutoField)
        sql_insert = f"""
            INSERT INTO {tabela} ({COLUNAS_SQL})
            VALUES ({PLACEHOLDERS_SQL})
        """
        
        # Executa a inserção de múltiplos registros de uma vez (executemany)
        cursor.executemany(sql_insert, dados)
        
        # Confirma as mudanças
        conn_destino.commit()
        conn_destino.close()
        
        print(f"Inserção concluída! {cursor.rowcount} registros copiados para '{db_destino}'.")
        
    except sqlite3.Error as e:
        print(f"Erro ao inserir no banco de dados de destino: {e}")
        # Se ocorrer um erro, pode ser útil desfazer o commit
        if conn_destino:
            conn_destino.rollback()

def main():
    """
    Função principal para coordenar a cópia de dados.
    :return: None
    """
    print("--- INICIANDO CÓPIA DE DADOS MTCars ---")
    
    # 1. Ler os dados do arquivo de origem
    registros = ler_dados_origem(DB_ORIGEM, NOME_TABELA, COLUNAS)
    
    # 2. Inserir os dados no arquivo de destino
    inserir_dados_destino(DB_DESTINO, NOME_TABELA, COLUNAS, registros)

    print("--- PROCESSO CONCLUÍDO ---")

if __name__ == "__main__":
    main()
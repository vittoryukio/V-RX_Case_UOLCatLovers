import requests
import csv

def buscar_ceps_e_salvar_csv():

    # URL final
    url = f"https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=100"
    nome_arquivo_csv = "D:\VittorY\Documents\Desafio\Verx\Extract\UOLCatLovers.csv"

    try:
        print(f"Buscando endereços em: {url} ...\n")

        # Fazendo a requisição
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        # Arquivo CSV
        with open(nome_arquivo_csv, mode='w', newline='', encoding='utf-8-sig') as arquivo:

            # Cabeçalhos
            cabecalhos = dados[0].keys()

            # CSV
            escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalhos)

            # Escreve o cabeçalho
            escritor_csv.writeheader()

            # Escreve todas as linhas
            escritor_csv.writerows(dados)

        print(f"Dados salvos com sucesso no arquivo: '{nome_arquivo_csv}'.")

    except:
        print(f"ERROR")

# --- Execução do Código ---
buscar_ceps_e_salvar_csv()

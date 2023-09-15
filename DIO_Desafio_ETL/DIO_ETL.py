import csv

nome_arquivo_origem = 'Vendas2023.csv'
nome_arquivo_destino = 'Vendas2023_Transformadas.csv'

def extrair_dados():
    dados = []
    try:
        with open(nome_arquivo_origem, mode='r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            for linha in reader:
                dados.append(linha)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo_origem} não encontrado.")

    return dados

def transformar_dados(dados):
    dados_transformados = []

    dados_transformados.append(['Data', 'Cliente', 'Produto', 'Valor', 'Comissao'])

    for linha in dados[1:]:
        data, cliente, produto, valor = linha
        valor = float(valor)
        comissao = valor * 0.1
        linha_transformada = [data, cliente, produto, valor, comissao]
        dados_transformados.append(linha_transformada)

    return dados_transformados

def carregar_dados(dados_transformados):
    with open(nome_arquivo_destino, mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for linha in dados_transformados:
            writer.writerow(linha)
    print(f"Dados transformados carregados em '{nome_arquivo_destino}' com sucesso!")

def main():
    dados = extrair_dados()

    if not dados:
        print("Nenhum dado encontrado no arquivo de origem.")
        return

    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados)
    print("Processo ETL concluído com sucesso!")

    print("Dados transformados:")
    for linha in dados_transformados:
        print(linha)

if __name__ == "__main__":
    main()

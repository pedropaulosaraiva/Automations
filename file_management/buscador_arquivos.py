import os
import shutil

def copiar_arquivos_recursivamente(origem, destino, nome_pasta_destino, extensao):
    """
    Copia arquivos de uma extensão específica de um diretório e suas subpastas para outro diretório.
    Cria uma pasta específica no destino.

    :param origem: Caminho do diretório de origem
    :param destino: Caminho do diretório de destino
    :param nome_pasta_destino: Nome da nova pasta a ser criada no diretório de destino
    :param extensao: Extensão dos arquivos a serem copiados (ex: '.xls', '.txt', '.png')
    """
    # Verifica se o diretório de origem existe
    if not os.path.exists(origem):
        print(f"Erro: O diretório de origem '{origem}' não existe.")
        return

    # Cria a nova pasta no diretório de destino
    pasta_destino = os.path.join(destino, nome_pasta_destino)
    os.makedirs(pasta_destino, exist_ok=True)

    # Contador de arquivos copiados
    arquivos_copiados = 0

    # Percorre o diretório de origem e suas subpastas
    for raiz, _, arquivos in os.walk(origem):
        for arquivo in arquivos:
            # Verifica se o arquivo possui a extensão desejada
            if arquivo.lower().endswith(extensao.lower()):
                caminho_origem = os.path.join(raiz, arquivo)
                shutil.copy(caminho_origem, pasta_destino)
                arquivos_copiados += 1
                print(f"Arquivo '{arquivo}' copiado de '{raiz}' para '{pasta_destino}'.")

    # Exibe resumo do processo
    if arquivos_copiados > 0:
        print(f"{arquivos_copiados} arquivo(s) com a extensão '{extensao}' foram copiados para '{pasta_destino}'.")
    else:
        print(f"Nenhum arquivo com a extensão '{extensao}' foi encontrado no diretório '{origem}'.")

# Exemplo de uso
diretorio_origem = r"C:\Users\ppgsa\Music\teste"
diretorio_destino = r"C:\Users\ppgsa\Music"
nome_da_pasta = "Arquivos_Copiados"
extensao_arquivo = ".txt"  # Substitua pela extensão desejada

copiar_arquivos_recursivamente(diretorio_origem, diretorio_destino, nome_da_pasta, extensao_arquivo)

import os
import shutil
from PyPDF2 import PdfReader


def contar_paginas_pdf(caminho_pdf):
    """
    Conta o número de páginas em um arquivo PDF.

    :param caminho_pdf: Caminho do arquivo PDF
    :return: Número de páginas no PDF
    """
    try:
        reader = PdfReader(caminho_pdf)
        return len(reader.pages)
    except Exception as e:
        print(f"Erro ao processar o arquivo '{caminho_pdf}': {e}")
        return -1  # Retorna -1 se houver erro


def copiar_pdfs_menos_de_4_paginas(origem, destino, nome_pasta_destino):
    """
    Copia arquivos PDF com menos de 4 páginas de um diretório e suas subpastas para outro diretório.
    Cria uma pasta específica no destino.

    :param origem: Caminho do diretório de origem
    :param destino: Caminho do diretório de destino
    :param nome_pasta_destino: Nome da nova pasta a ser criada no diretório de destino
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
            # Verifica se o arquivo possui extensão .pdf
            if arquivo.lower().endswith('.pdf'):
                caminho_origem = os.path.join(raiz, arquivo)
                paginas = contar_paginas_pdf(caminho_origem)
                if paginas > 0 and paginas < 4:  # Verifica se o PDF tem menos de 4 páginas
                    shutil.copy(caminho_origem, pasta_destino)
                    arquivos_copiados += 1
                    print(f"Arquivo '{arquivo}' ({paginas} páginas) copiado de '{raiz}' para '{pasta_destino}'.")

    # Exibe resumo do processo
    if arquivos_copiados > 0:
        print(f"{arquivos_copiados} arquivo(s) PDF com menos de 4 páginas foram copiados para '{pasta_destino}'.")
    else:
        print(f"Nenhum arquivo PDF com menos de 4 páginas foi encontrado no diretório '{origem}'.")


# Exemplo de uso
diretorio_origem = r"C:\caminho\do\diretorio\de\origem"
diretorio_destino = r"C:\caminho\do\diretorio\de\destino"
nome_da_pasta = "PDFs_Menos_4_Paginas"

copiar_pdfs_menos_de_4_paginas(diretorio_origem, diretorio_destino, nome_da_pasta)

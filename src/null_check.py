import pandas as pd

from src.extract import extract_pkg_info


def null_check():
    # Ler o arquivo Excel
    df = pd.read_excel('npm_packages.xlsx')

    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        # Verificar se 'weekly_downloads' ou ''github' está faltando ou é NaN
        if pd.isna(row['weekly_downloads']) or pd.isna(row['github']):
            url = row['link']
            # Coletar dados novamente
            repo, wk_d = extract_pkg_info(url)
            # Atualizar o DataFrame com os novos dados
            if pd.isna(row['weekly_downloads']) and wk_d:
                df.at[index, 'weekly_downloads'] = wk_d

            if pd.isna(row['github']) and repo:
                df.at[index, 'github'] = repo

    # Escrever o DataFrame atualizado em um novo arquivo Excel
    df.to_excel('npm_packages.xlsx', index=False)

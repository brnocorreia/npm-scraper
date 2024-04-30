import pandas as pd

def split():

    # Ler o arquivo Excel
    df = pd.read_excel('npm_packages.xlsx')

    # Filtrar as linhas onde a coluna 'escolhido' é True
    df_escolhidos = df.loc[df['escolhido'] == True]

    # Escrever o DataFrame dos escolhidos em um novo arquivo Excel
    df_escolhidos.to_excel('npm_packages_ready.xlsx', index=False)

    print("DataFrame dos escolhidos criado e salvo em 'npm_packages_ready.xlsx'.")

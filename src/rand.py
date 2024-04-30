import pandas as pd
import random

def choose_random(num: int):

    # Lê o arquivo Excel
    df = pd.read_excel('npm_packages.xlsx')

    # Gera 32 números aleatórios únicos dentro do intervalo de índices do DataFrame
    random_indexes = random.sample(range(len(df)), num)

    # Adicionar uma nova coluna chamada 'escolhido' e definir como False por padrão
    df['escolhido'] = False

    # Marcar como True nas linhas correspondentes aos números aleatórios gerados
    df.loc[random_indexes, 'escolhido'] = True

    # Escrever o DataFrame atualizado em um novo arquivo Excel
    df.to_excel('npm_packages.xlsx', index=False)

    print("Coluna 'escolhido' adicionada e marcada com 'True' nos índices aleatórios.")

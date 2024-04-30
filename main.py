from src.extract import init_extract
from src.null_check import null_check
from src.rand import choose_random
from src.split import split


opt = 0

while opt != 5:
    print(
"""
-----------------------------------------
1 - Coletar dados
2 - Checar por valores nulos
3 - Escolher randomicamente a amostra
4 - Separar as bases de dados
5 - Encerrar
-----------------------------------------
        """
    )
    opt = int(input("Qual execução desejada? "))
    print()

    match (opt):
        case 1:
            init_extract()
        case 2:
            null_check()
        case 3:
            print("Quantos registros terá sua amostra? 32 <= i <= 200")
            num = int(input())
            choose_random()
        case 4:
            split()
        case 5:
            break
        case _:
            pass

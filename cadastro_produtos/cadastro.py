import os
import csv



def criar_menu():
    os.system("cls")
    print("""🅴🆂🆃🅾🆀🆄🅴 🅰🅿🅿""")
    print("1. Cadastrar produto")
    print("2. Listar Produtos")
    print("3. Ativar produtos")
    print("4. Excluir produto")
    print("5. Sair")


def voltar_ao_menu_principal():
    input("Pressione Enter para voltar ao menu principal...")
    main()


def criar_titulo(titulo):
    os.system("cls")
    print(f"**** {titulo} ****\n")


def cadastrar_produto():
    criar_titulo("CADASTRO DE PRODUTOS")

    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))
    fabricante = input("Fabricante do produto: ")

    # GRAVAR O PRODUTOS NO ARQUIVO produtos.csv
    with open("produtos.csv", "a", newline="") as arquivo_produtos:
        escritor = csv.writer(arquivo_produtos)
        escritor.writerow([codigo, nome, valor, fabricante, "false"])

    print()
    print(f"Produto {nome.upper()}, cadastrado com sucesso!\n")
    ativar_produto = input("Você deseja ativar o produto? Responda sim ou não")
    if ativar_produto == "sim":
        print(f"Produto {nome.upper()} ativado com sucesso! ")
    elif ativar_produto == "nao":
        print(f"Produto {nome.upper()} cadastrado, porém inativo!")
    voltar_ao_menu_principal()


def exibir_produtos():
    criar_titulo("LISTAR PRODUTOS")



    print(f"Total de produtos cadastrados: ")
    print()
    print(f"")
    print("-------------------------------------------------------------------------")

    #ABRIR O ARQUIVO PARA LEITURA
    with open("produtos.csv", "r") as arquivo_produtos:
        leitor = csv.reader(arquivo_produtos)
        for produto in leitor:
            print(f"{produto[0]:<10}  {produto[1]:<30}  R$ {produto[3]:>6} {produto[4]:<15}")


    print()
    voltar_ao_menu_principal()


def excluir_produto():
    criar_titulo("Excluir Produto")

    indice = int(input("Qual o índice do produto que será removido? "))

    nome_produto = (input("Qual o nome do produto? "))



    # confirmacao = input(f"Você confirma a exclusão do produto {produtos[indice]} (s/n)?")
    #
    # if confirmacao == "s":
    #     excluido = produtos.pop(indice)
    #     print(f"O produto {excluido} foi excluído com sucesso!")
    # else:
    #     print("Operação de exclusão cancelada.")
    #     voltar_ao_menu_principal()

    voltar_ao_menu_principal()




    voltar_ao_menu_principal()

def ativar_desativar_produto():
    criar_titulo("Ativar ou Desativar produto")

    codigo = int(input("Qual o codigo do produto? "))






    voltar_ao_menu_principal()


def escolher_opcao():

    try:
        opcao = int(input("\nEscolha uma opção(1 a 5): "))

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            exibir_produtos()
        elif opcao == 3:
            ativar_desativar_produto()
        elif opcao == 4:
            excluir_produto()
        elif opcao == 5:
            exit()
        else:
            tratar_erro()

    except:
        tratar_erro()


def tratar_erro():
    input("Valor inválido! Pressione Enter para voltar ao menu principal...")
    main()


def main():
    criar_menu()
    escolher_opcao()


if __name__ == "__main__":
    main()












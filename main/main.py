from functions.create_products import criar_produto
from functions.read_products import ver_produtos_cadastrados
from functions.update_products import atualizar_produto
from functions.delete_products import deletar_produto

info_produtos = []

while(True):
    print("\n\tMenu Principal\t\t")
    print("\n1 - Cadastrar produtos")
    print("2 - Ver produtos cadastrados")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("0 - Sair")
    opcao = int(input("\nEscolha uma opção: "))

    if(opcao == 1):
        criar_produto(info_produtos)
    elif(opcao == 2):
        ver_produtos_cadastrados(info_produtos)
    elif(opcao == 3):
        atualizar_produto(info_produtos)
    elif(opcao == 4):
        deletar_produto(info_produtos)
    elif(opcao == 0):
        print("\nFechando o programa...")
        print("Tenha um excelente dia!\n")
        break
    else:
        print("Opção inválida. Tente novamente!")
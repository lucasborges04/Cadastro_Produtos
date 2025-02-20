def deletar_produto(lista_produtos):
    while(True):
        id_produto = int(input("Digite o ID do produto que deseja deletar: "))
        produto_encontrado = None

        for produto in lista_produtos:
            if(produto["ID"] == id_produto):
                print("\nProduto encontrado!")
                produto_encontrado = produto
                break

        if(produto_encontrado):
            lista_produtos.remove(produto_encontrado)
            print(f"\nProduto com ID {id_produto} foi removido com sucesso!")
        else:
            print(f"\nProduto com ID {id_produto} não foi encontrado na lista!")        
        
        continua_deletando = input("\nDeseja excluindo mais produtos(Sim ou Não)? ").strip().lower()

        while(continua_deletando != ["sim", "não", "nao"]):
            if (continua_deletando == "sim"):
                break
            elif(continua_deletando == "nao" or continua_deletando == "não"):
                return
            else:
                print("Entrada inválida! Digite 'sim' ou 'não' para seguir")

            continua_deletando = input("\nDeseja continuar excluindo produtos do sistema(Sim ou Não)? ").strip().lower()

    return
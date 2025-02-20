def atualizar_produto(lista_produtos):
    while(True):
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
        produto_encontrado = False

        for produto in lista_produtos:
            if(produto["ID"] == id_produto):
                print(f"\nProduto encontrado!\n")
                produto_encontrado = True
                for chave, valor in produto.items():
                    print(f"{chave}: {valor}")
                
                print("\nDigite os novos valores ou aperte ENTER para manter os atuais.")

                novo_nome = input("Digite um novo nome: ")
                if(novo_nome):
                    produto["Nome"] = novo_nome
                
                novo_preco = input("Digite um novo preço para o produto: ")
                if(novo_preco):
                    produto["Preço"] = float(novo_preco)
                
                nova_marca = input("Digite o nome da marca: ")
                if(nova_marca):
                    produto["Marca"] = nova_marca
                
                novo_peso = input("Digite o novo peso: ")
                if(novo_peso):
                    produto["Peso"] = float(novo_peso)

                nova_quantidade = input("Digite uma nova quantidade: ")
                if(nova_quantidade):
                    produto["Quantidade"] = int(nova_quantidade)

                print("\nProduto atualizado com sucesso!")

        if(not produto_encontrado):   
            print("\nProduto não encontrado!")

        continuar_editando = input("\nDeseja continuar editando(Sim ou Não)? ").strip().lower()

        while(continuar_editando != ["sim", "não", "nao"]):
            if(continuar_editando == "sim"):
                break
            elif(continuar_editando == "não" or continuar_editando == "nao"):
                return
            else:
                print("Entrada inválida! Digite 'sim' ou 'não' para seguir")
            
            continuar_editando = input("\nDeseja continuar editando(Sim ou Não)? ").strip().lower()
    
    return
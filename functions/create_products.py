def criar_produto(lista_produtos):
    while(True):
        produto = {}

        while(True):
            id_produto = int(input("\nDigite o ID do produto: "))
            id_existente = False

            for produto_cadastrado in lista_produtos:
                if(produto_cadastrado["ID"] == id_produto):
                    id_existente = True
                    break
            
            if(id_existente):
                print(f"ERRO: O ID {id_produto} já existe! Insira outro para continuar o cadastro.")
            else:
                break

        produto["ID"] = id_produto
        produto["Nome"] = input("Digite o nome do produto: ")
        produto["Preço"] = float(input("Digite o preço do produto: "))
        produto["Marca"] = input("Digite o nome da marca: ")
        produto["Peso"] = float(input("Digite o peso do produto(em caso de líquidos, quantos litros): "))
        produto["Quantidade"] = int(input("Digite a quantidade para adicionar no estoque: "))
        lista_produtos.append(produto)

        print(f"\n{produto["Nome"]} cadastrado com sucesso!")

        continuar_cadastro = input("\nDeseja continuar cadastrando(Sim ou Não)? ").strip().lower()

        while(continuar_cadastro != ["sim", "não", "nao"]):
            if(continuar_cadastro == "sim"):
                break
            elif(continuar_cadastro == "não" or continuar_cadastro == "nao"):
                return
            else:
                print("Entrada inválida! Digite 'sim' ou 'não' para seguir")
            
            continuar_cadastro = input("\nDeseja continuar cadastrando(Sim ou Não)? ").strip().lower()

    return
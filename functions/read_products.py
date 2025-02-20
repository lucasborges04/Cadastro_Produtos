def ver_produtos_cadastrados(lista_produtos_cadastrados):
    for i, produto_cadas in enumerate(lista_produtos_cadastrados, start = 1):
        print(f"\n\t\tProduto {i}:")
        print(f"ID: {produto_cadas["ID"]}")
        print(f"Nome do produto: {produto_cadas["Nome"]}")
        print(f"Preço do produto: {produto_cadas["Preço"]:.2f}")
        print(f"Marca do produto: {produto_cadas["Marca"]}")
        print(f"Peso do produto: {produto_cadas["Peso"]}")
        print(f"Quantidade de produtos adicionados ao estoque: {produto_cadas["Quantidade"]}")
    
    return
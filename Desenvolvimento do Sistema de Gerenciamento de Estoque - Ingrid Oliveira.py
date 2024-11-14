class Produto:
    def __init__(self, idproduto: int, produto: str, localizacao: str, quantidade: float, preco_compra: float, preco_venda: float):
        self.idproduto = idproduto
        self.produto = produto
        self.localizacao = localizacao
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda

    def cadastro(self):
        print(f"{self.produto}, localizado em {self.localizacao}, quantidade: {self.quantidade}, Preço de Compra: R${self.preco_compra}, Preço de Venda: R${self.preco_venda}.")

class Cadastros:
    def __init__(self, profissao: str):
        self.profissao = profissao
        self.produtos = [
            Produto(1, "Produto A", "Prateleira 1", 100, 10.0, 15.0),
            Produto(2, "Produto B", "Prateleira 2", 200, 20.0, 30.0),
            Produto(3, "Produto C", "Prateleira 3", 150, 12.5, 18.0),
            Produto(4, "Produto D", "Prateleira 4", 300, 5.0, 8.0),
            Produto(5, "Produto E", "Prateleira 5", 50, 25.0, 35.0),
            Produto(6, "Produto F", "Prateleira 6", 250, 8.0, 12.0),
            Produto(7, "Produto G", "Prateleira 7", 120, 10.5, 15.5)
        ]
        self.movimentacoes = []  # Lista para registrar movimentações

    def check_permission(self, requisitos_funcoes):
        return self.profissao in requisitos_funcoes

    def cadastrar_produtos(self):
        if not self.check_permission(["gerente"]):
            print("Acesso negado.")
            return
        produto = input("Digite o nome do produto: ")
        try:
            idproduto = int(input("Digite o ID do produto cadastrado: "))
            quantidade = float(input("Digite a quantidade de produto a ser cadastrada: "))
            localizacao = input("Digite o local onde o produto será armazenado: ")
            preco_compra = float(input("Digite o preço de compra do produto: "))
            preco_venda = float(input("Digite o preço de venda do produto: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira os valores corretamente.")
            return
        
        itens = Produto(idproduto, produto, localizacao, quantidade, preco_compra, preco_venda)
        self.produtos.append(itens)
        print(f"O produto {produto} foi cadastrado com sucesso!")

    def editar_produto(self):
        if not self.check_permission(["gerente"]):
            print("Acesso negado.")
            return
        try:
            idproduto = int(input("Digite o ID do produto que deseja editar: "))
            for itens in self.produtos:
                if idproduto == itens.idproduto:
                    print(f"Produto encontrado: {itens.produto}, Localização: {itens.localizacao}, Quantidade: {itens.quantidade}")
                    novo_nome = input(f"Digite o novo nome do produto (atual: {itens.produto}): ")
                    if novo_nome:
                        itens.produto = novo_nome
                    nova_localizacao = input(f"Digite a nova localização do produto (atual: {itens.localizacao}): ")
                    if nova_localizacao:
                        itens.localizacao = nova_localizacao
                    nova_quantidade = input(f"Digite a nova quantidade do produto (atual: {itens.quantidade}): ")
                    if nova_quantidade:
                        try:
                            itens.quantidade = float(nova_quantidade)
                        except ValueError:
                            print("Quantidade inválida! Não foi possível atualizar.")
                            return
                    novo_preco_compra = input(f"Digite o novo preço de compra do produto (atual: {itens.preco_compra}): ")
                    if novo_preco_compra:
                        try:
                            itens.preco_compra = float(novo_preco_compra)
                        except ValueError:
                            print("Preço de compra inválido! Não foi possível atualizar.")
                            return
                    novo_preco_venda = input(f"Digite o novo preço de venda do produto (atual: {itens.preco_venda}): ")
                    if novo_preco_venda:
                        try:
                            itens.preco_venda = float(novo_preco_venda)
                        except ValueError:
                            print("Preço de venda inválido! Não foi possível atualizar.")
                            return
                    print(f"O produto {itens.produto} foi atualizado com sucesso!")
                    return
            print("Produto não encontrado.")
        except ValueError:
            print("ID inválido! Digite um número de ID válido.")

    def excluir_produto(self):
        if not self.check_permission(["gerente"]):
            print("Acesso negado.")
            return
        try:
            idremover = int(input("Digite o ID do produto que será excluído: "))
            for itens in self.produtos:
                if idremover == itens.idproduto:
                    self.produtos.remove(itens)
                    print("O produto detalhado abaixo foi removido: ")
                    itens.cadastro()
                    return
            print("Produto não encontrado.")
        except ValueError:
            print("ID inválido! Digite um número de ID válido.")

    def localizacao_produto(self):
        if not self.check_permission(["gerente", "estoquista", "atendente"]):
            print("Acesso negado.")
            return
        try:
            idlocalizar = int(input("Digite o ID do produto para localizar: "))
            for itens in self.produtos:
                if idlocalizar == itens.idproduto:
                    print(f"Produto encontrado: {itens.produto}")
                    print(f"Localização: {itens.localizacao}")
                    print(f"Quantidade disponível: {itens.quantidade}")
                    return
            print("Produto não encontrado.")
        except ValueError:
            print("ID inválido! Digite um número de ID válido.")

    def atualizacao_estoque(self):
        if not self.check_permission(["gerente", "estoquista"]):
            print("Acesso negado.")
            return
        try:
            idproduto = int(input("Digite o ID do produto que deseja atualizar a quantidade: "))
            quantidade_atualizada = float(input("Digite a quantidade conferida para o produto: "))
            for itens in self.produtos:
                if idproduto == itens.idproduto:
                    itens.quantidade = quantidade_atualizada
                    print(f"A quantidade do produto {itens.produto} foi atualizada para {quantidade_atualizada}.")
                    return
            print("Produto não encontrado.")
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir valores numéricos válidos.")

    def registro_entrada(self):
        if not self.check_permission(["gerente", "estoquista"]):
            print("Acesso negado.")
            return
        try:
            idproduto = int(input("Digite o ID do produto que está entrando no estoque: "))
            quantidade_entrada = float(input("Digite a quantidade de entrada do produto: "))
            if quantidade_entrada <= 0:
                print("A quantidade de entrada deve ser maior que zero.")
                return
            for itens in self.produtos:
                if idproduto == itens.idproduto:
                    itens.quantidade += quantidade_entrada
                    self.movimentacoes.append((idproduto, quantidade_entrada, "Entrada"))
                    print(f"A quantidade do produto {itens.produto} foi aumentada em {quantidade_entrada}. Novo estoque: {itens.quantidade}")
                    return
            print("Produto não encontrado.")
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir valores numéricos válidos.")

    def registro_saida(self):
        if not self.check_permission(["gerente", "estoquista"]):
            print("Acesso negado.")
            return
        try:
            idproduto = int(input("Digite o ID do produto que está saindo do estoque: "))
            quantidade_saida = float(input("Digite a quantidade de saída do produto: "))
            if quantidade_saida <= 0:
                print("A quantidade de saída deve ser maior que zero.")
                return
            for itens in self.produtos:
                if idproduto == itens.idproduto:
                    if quantidade_saida > itens.quantidade:
                        print(f"Erro: Não há estoque suficiente para realizar a saída de {quantidade_saida} unidades do produto {itens.produto}.")
                        print(f"Estoque disponível: {itens.quantidade}")
                        return
                    else:
                        itens.quantidade -= quantidade_saida
                        self.movimentacoes.append((idproduto, quantidade_saida, "Saída"))
                        print(f"A quantidade do produto {itens.produto} foi reduzida em {quantidade_saida}. Novo estoque: {itens.quantidade}")
                        return
            print("Produto não encontrado.")
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir valores numéricos válidos.")

    def gerar_relatorio_movimentacao(self):
        if not self.check_permission(["gerente"]):
            print("Acesso negado.")
            return
        print("\nRelatório de Movimentação de Produtos:")
        if not self.movimentacoes:
            print("Nenhuma movimentação registrada.")
        else:
            for mov in self.movimentacoes:
                print(f"ID Produto: {mov[0]} | Quantidade: {mov[1]} | Tipo: {mov[2]}")

    def visualizar_produtos(self):
        if not self.check_permission(["gerente", "estoquista", "atendente"]):
            print("Acesso negado.")
            return
        if not self.produtos:
            print("Não há produtos cadastrados.")
        else:
            print("\nLista de Produtos Cadastrados:")
            for produto in self.produtos:
                print(f"ID: {produto.idproduto} | Produto: {produto.produto} | Localização: {produto.localizacao} | Quantidade: {produto.quantidade} | Preço Compra: R${produto.preco_compra} | Preço Venda: R${produto.preco_venda}")

    def sistema_menu(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Cadastrar Produto")
            print("2. Editar Produto")
            print("3. Excluir Produto")
            print("4. Localizar Produto")
            print("5. Atualizar Estoque")
            print("6. Registro de Entrada")
            print("7. Registro de Saída")
            print("8. Visualizar Todos os Produtos")
            print("9. Relatório de Movimentação")
            print("0. Sair")

            opcao = input("Escolha a opção: ")
            if opcao == "1":
                self.cadastrar_produtos()
            elif opcao == "2":
                self.editar_produto()
            elif opcao == "3":
                self.excluir_produto()
            elif opcao == "4":
                self.localizacao_produto()
            elif opcao == "5":
                self.atualizacao_estoque()
            elif opcao == "6":
                self.registro_entrada()
            elif opcao == "7":
                self.registro_saida()
            elif opcao == "8":
                self.visualizar_produtos()
            elif opcao == "9":
                self.gerar_relatorio_movimentacao()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

# Executando o programa com profissão especificada
if __name__ == "__main__":
    profissao = input("Digite sua profissão (gerente, estoquista, atendente): ").lower()
    cadastros = Cadastros(profissao)
    cadastros.sistema_menu()

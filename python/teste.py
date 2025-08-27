
def gerar_relatorio(self):
        relatorio = {
            "estoque_baixo": [],
            "estoque_excesso": [],
            "movimentacao": []
        }
        for produto in self.produtos.values():
            if produto.quantidade < 10:  
                relatorio["estoque_baixo"].append(produto.nome)
            elif produto.quantidade > 100:  
                relatorio["estoque_excesso"].append(produto.nome)
            relatorio["movimentacao"].append((produto.nome, produto.quantidade))
        
        print("Relatório de Estoque:")
        print("Produtos com estoque baixo:", relatorio["estoque_baixo"])
        print("Produtos com excesso de estoque:", relatorio["estoque_excesso"])
        print("Movimentação do estoque:", relatorio["movimentacao"])

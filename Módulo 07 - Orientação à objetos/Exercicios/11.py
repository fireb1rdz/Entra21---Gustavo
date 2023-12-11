"""
11) Crie uma classe chamada Produto com os seguintes atributos:
Nome (str)
Preço (float)
Quantidade em estoque (int)

A classe deve ter métodos para realizar as seguintes operações:
Vender produto: recebe a quantidade a ser vendida como parâmetro e atualiza a quantidade em estoque.
Comprar produto: recebe a quantidade a ser comprada como parâmetro e atualiza a quantidade em estoque.
Calcular valor total: retorna o valor total do estoque, multiplicando o preço pela quantidade em estoque.
"""

class Produto:
    
    def __init__(self, nome:str, preco: float, quantidade_estoque: int) -> None:
        """Essa classe representa um produto.
        
        Args:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
            quantidade_estoque (int): Quantidade disponível em estoque do produto.
        """
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def vender_produto(self, quantidade_venda: int) -> bool:
        """Realiza a venda do produto e atualização do estoque.
        
        Args:
            quantidade_venda (int): Quantidade do produto a ser vendida (se possui estoque disponível para determinada venda retorna True, caso contrário retorna False.)
        
        Returns:
            True: Venda realizada com sucesso.
            False: Quantidade no estoque insuficiente para a venda.
        """
        if self.quantidade_estoque < quantidade_venda:
            return False
        else:
            self.quantidade_estoque -= quantidade_venda
            return True
    
    def comprar_produto(self, quantidade_compra: int) -> None:
        """Realiza a compra do produto e atualização do estoque.
        
        Args:
            quantidade_compra (int): Quantidade do produto a ser comprada.
        """
        self.quantidade_estoque += quantidade_compra

    def calcular_valor_estoque(self) -> float:
        """Realiza a multiplicação da quantidade em estoque pelo preço do produto.
        
        Returns: 
            valor_estoque (float): Valor do estoque disponível do produto.
        """
        valor_estoque = self.quantidade_estoque * self.preco
        return valor_estoque
    

if __name__ == "__main__":
    celular = Produto("iPhone", 4_000, 10)
    celular.comprar_produto(200)
    print(celular.quantidade_estoque)
    celular.vender_produto(10)
    print(celular.quantidade_estoque)
    print(celular.calcular_valor_estoque())
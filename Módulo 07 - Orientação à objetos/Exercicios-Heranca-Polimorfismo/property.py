"""
4) Implemente as classes abaixo:

Classe Imovel: Esta será a classe base.
Atributos:
endereco: Uma string que armazena o endereço do imóvel.
preco: Um valor numérico representando o preço do imóvel.

Métodos:
Um construtor para inicializar os atributos endereco e preco.
Métodos de acesso (getters) para ambos os atributos.
Um método de impressão que exibe o endereço e o preço do imóvel.

Classe Novo (herda de Imovel): Esta classe representa um imóvel novo e tem um adicional no preço.
Atributos:
adicional: Um valor numérico que representa o adicional no preço do imóvel novo.

Métodos:
Um construtor que inicializa o endereço, o preço e o valor adicional.
Métodos de acesso e modificação (getters e setters) para o atributo adicional.
Um método de impressão que exibe o endereço, o preço base, o adicional e o preço final (preço base + adicional).

Classe Velho (herda de Imovel): Esta classe representa um imóvel antigo e tem um desconto no preço.

Atributos:
desconto: Um valor numérico que representa o desconto no preço do imóvel antigo.

Métodos:
Um construtor que inicializa o endereço, o preço e o valor do desconto.
Métodos de acesso e modificação (getters e setters) para o atributo desconto.
Um método de impressão que exibe o endereço, o preço base, o desconto e o preço final (preço base - desconto).

"""

class Property():
    """This class represents a property.
    
    Attributes:
        address (str) = the address
        price (float) = the price
    """
    def __init__(self, address, price) -> None:
        # Defines de attributes of the property
        self.__address = address
        self.__price = price
    
    @property
    def address(self):
        """str: The property's address"""
        return self.__address

    @property
    def price(self):
        """float: The property's price"""
        return self.__price
    
    def info(self):
        """Prints the property's info (address and price)"""
        print(f"Address: {self.address} | Price: {self.price}")


if __name__ == "__main__":
    casa = Property("Rua aparecida", 70_000)
    casa.info()
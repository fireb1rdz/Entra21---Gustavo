"""
Classe - É um modelo para o objeto.
* Atributos - Características do objeto
* Métodos - Ações do objeto.
"""

class NomeClasse:
    """Docstring da classe."""

    # Método construtor: método utilizado para inicializar um objeto da classe.
    def __init__(self, parametro1: int = 10) -> None:
        # self -> referência ao próprio objeto.
        self.atributo1 = parametro1

        # Declarar um atributo privado.
        self.__atributo_privado = 0

    # Getters
    @property
    def atributo_privado(self):
        return self.__atributo_privado

    # Setters
    @atributo_privado.setter
    def atributo_privado(self, new_value: int):
        self.__atributo_privado = new_value

    # Métodos do objeto
    def metodo1(self):
        """Docstring"""
        print("Chamando o método do objeto.")


if __name__ == "__main__":
    # Sintaxe para criar um objeto
    objeto_teste = NomeClasse(20)

    #  Acessando os atributos
    print(objeto_teste.atributo1)

    # Acessando os métodos
    objeto_teste.metodo1()
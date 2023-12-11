"""
12) Crie uma classe chamada ConversorMoeda com os seguintes atributos estáticos:
Taxa de conversão (float)
Moeda base (str)

A classe deve ter os seguintes métodos estáticos:
Um método converter_para_real() que recebe um valor em outra moeda como parâmetro e retorna o valor convertido para reais.
Um método converter_de_real() que recebe um valor em reais como parâmetro e retorna o valor convertido para a moeda base.
"""

class ConversorMoeda:
    __taxa_conversao = 5
    __moeda_base = "dólar"
    
    def __init__(self, nome: str) -> None:
        """Essa classe representa um conversor de moedas.
        
        Args:
            nome (str): Nome do conversor.
        """
        self.nome = nome
    
    def converter_para_real(cls, valor: float) -> str:
        """Converte o valor dado como parâmetro utilizando a taxa de conversão da classe (atributo estático).
        
        Args: 
            valor (float): O valor da outra moeda à ser convertido.

        Returns:
            valor_convertido (float): O valor resultante da conversão.
        """
        valor_convertido = valor * cls.__taxa_conversao
        return f"O valor de {valor} em {cls.__moeda_base} convertido para real é {valor_convertido}"
    
    def converter_de_real(cls, valor: float) -> str:
        """Converte o valor dado como parâmetro utilizando a taxa de conversão da classe (atributo estático).
        
        Args: 
            valor (float): O valor em real à ser convertido.

        Returns:
            valor_convertido (float): O valor resultante da conversão.
        """
        valor_convertido = valor / cls.__taxa_conversao
        return f"O valor de {valor} em real convertido para {cls.__moeda_base} é {valor_convertido:.2f}"
    
if __name__ == "__main__":
    conversor = ConversorMoeda("Conversor2000")
    print(conversor.converter_de_real(5000))
    print(conversor.converter_para_real(5000))
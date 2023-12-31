from property import Property

class newProperty(Property):
    def __init__(self, address, price, addicional) -> None:
        super().__init__(address, price)
        self.__addicional = addicional

    @property
    def addicional(self):
        """float: returns the property's addicional value."""
        return self.__addicional

    @addicional.setter
    def addicional(self, addicional_value):
        """float: Property's addicional value."""
        self.__addicional = addicional_value
    
    def info(self):
        """Prints the new property info.
        
        Address: The address
        Price: The original price
        Addicional: The addicional value
        Total: The sum (price + addicional)
        """
        print(f"Address: {self.address} | Price: {self.price} | Addicional: {self.addicional} | Total (Price + Addicional): {self.price + self.addicional}")
    
if __name__ == "__main__":
    nova_casa = newProperty("Rua aparecida", 80_000, 20_000)
    nova_casa.info()
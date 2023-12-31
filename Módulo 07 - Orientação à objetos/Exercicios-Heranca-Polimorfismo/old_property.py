from property import Property

class oldProperty(Property):
    def __init__(self, address, price, discount) -> None:
        super().__init__(address, price)
        self.__discount = discount
    
    @property
    def discount(self):
        """float: gets the property's discount."""
        return self.__discount
    
    @discount.setter
    def discount(self, discount_value):
        """float: new discount value"""
        self.discount = discount_value
        
    def info(self):
        """Prints the old property info.
        
        Address: The address
        Price: The original price
        Discount: The discount value
        Total: The subtraction (price - discount)
        """
        print(f"Address: {self.address} | Price: {self.price} | Discount: {self.discount} | Total (Price - discount): {self.price - self.discount}")
    
if __name__ == "__main__":
    nova_casa = oldProperty("Rua aparecida", 80_000, 20_000)
    nova_casa.info()
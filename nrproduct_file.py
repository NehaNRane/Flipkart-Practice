from nrparent_file import Base

class Product(Base):
    """This is for product related information."""
    product_list = []
    def __init__(self, id, name, category, price, quantity):
        self.ProductID = id
        self.ProductName = name
        self.ProductCategory = category
        self.ProductPrice = price
        self.ProductQuantity = quantity

    def show_proddetail(self):
        print(f"""
        Product ID     : {self.ProductID}
        Product Name   : {self.ProductName}
        Category       : {self.ProductCategory}
        Price          : {self.ProductPrice}
        Quantity       : {self.ProductQuantity}
        """)

if __name__ == '__main__':
    prod_obj1 = Product(1001, "Tablet", "Electronics", 75000, 10)
    prod_obj2 = Product(1002, "Denim", "Clothing", 1245, 10)
    
    # prod_obj1.show_proddetail()
    # prod_obj2.show_proddetail()

    print([prod_obj1, prod_obj2])
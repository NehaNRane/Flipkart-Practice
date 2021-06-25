from nrparent_file import Base

class Order(Base):
    """For Order related informations"""
    all_ordered_list = []
    def __init__(self, transactionid, cust, prod, amount, quantity, disprice):
        self.OrderTransactionID = transactionid
        self.OrderCust = cust
        self.OrderProduct = prod
        self.OrderAmount = amount
        self.OrderQuantity = quantity
        self.DiscountedPrice = disprice

    def show_orderdetail(self):
        print(f"""
        Transaction ID   : {self.OrderTransactionID}
        Customer         : {self.OrderCust}
        Product Name     : {self.OrderProduct}
        Amount           : {self.OrderAmount}
        Quantity         : {self.OrderQuantity}
        """)

    # def get_orderdetails(self, cust):
    #     if cust in self.OrderCust:
    #         return self.OrderTransactionID, self.OrderAmount, self.OrderQuantity
        

if __name__ == '__main__':
    order_obj = Order(2123, "Neha Rane", 2500)
    #print(order_obj.__dict__)
    order_obj.show_orderdetail()
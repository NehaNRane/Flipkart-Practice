from nrparent_file import Base
from nrproduct_file import Product
from nraccount_file import Account
from nrorder_file import Order
from nrcustomer_file import Customer
import random
from copy import deepcopy

class Flipkart(Base):
    """This class is for Flipkart Warehouse or Delivery Centre Information"""
    def __init__(self, location, headquarter, no_of_warehouse, products, acc):
        self.FlipkartLocation = location
        self.FlipkartHeadQuarters = headquarter
        self.FlipkartNoOfWarehouse = no_of_warehouse
        self.FlipkartProducts = products
        self.FlipkartAcc = acc
        self.Product_Names = list(map(lambda x : x.ProductName, self.FlipkartProducts))

    def show_Flipkartdetail(self):
        print(f"""
        Location         : {self.FlipkartLocation}
        HeadQuarter      : {self.FlipkartHeadQuarters}
        No. of Warehouse : {self.FlipkartNoOfWarehouse}
        Products         : {self.FlipkartProducts}
        Account          : {self.FlipkartAcc}
        Product Names    : {self.Product_Names}
        """)

    def purchase_product(self, productname, cust, qty):  # Laptop
        if productname in self.Product_Names:  # Check whether product is available or not
            for prod in self.FlipkartProducts:  # iterate single single product  # flipkart prods
                if productname == prod.ProductName:
                    if qty <= prod.ProductQuantity:
                        total_price =  qty * prod.ProductPrice
                        # print(f"Total price for ur purchase is:- {total_price}")
                        
                        if cust.CustAcc.AccountBalance >= total_price:
                            print(prod, "Flipkart Stock before order")
                            print()
                            # Check if customer is plusmember, if yes then 5% discount on total price
                            if cust.PlusMember == True:
                                if total_price >= 15000:
                                    discount = total_price - total_price * (10/100)
                                    total_price = discount
                                else:
                                    discount = total_price - total_price * (5/100)
                                    total_price = discount
                            else:
                                discount = total_price - total_price * (5/100)
                                total_price = discount
                            cust.CustAcc.AccountBalance -=  total_price
                            self.FlipkartAcc.AccountBalance += total_price
                            actual_qty = prod.ProductQuantity
                            prod.ProductQuantity = qty
                            cust.OrderedProducts.append(deepcopy(prod))
                            prod.ProductQuantity = actual_qty - qty  # update the stock
                            # create transaction id
                            trans_id = random.randint(1111111, 9999999)
                            print("Total Price after discount", total_price)
                            order_obj = Order(trans_id, cust, productname, total_price, qty, discount)
                            Order.all_ordered_list.append(order_obj)
                            print(f"Thanks for purchasing product with Flipkart..Your generated transaction id is:- {trans_id}")
                            print(prod, "Flipkart Stock after order") 
                        else:
                            print("Insufficient amount to purchase this product..!")
                            return
                    else:
                        print(f"Out of Stock!!! We have only {prod.ProdQty}")
                        return 
        else:
            print(f"Product not available!!! Available products are:- {self.Product_Names}")

    def return_product(self, cust, prodname, qty):
        # print(Order.all_ordered_list)
        for ord in Order.all_ordered_list:
            # print(ord.OrderCust.CustName)
            if cust.CustName == ord.OrderCust.CustName and prodname == ord.OrderProduct:
                if qty <= ord.OrderQuantity:
                    # print("YESSSSSSSSSSSSSSSSSSSSS")
                    for prod in Product.product_list:
                        # print(prod.ProductName)
                        if prodname == prod.ProductName:
                            a = ord.DiscountedPrice // ord.OrderQuantity
                            # print(f"***************** {a} ******************************")
                            refund_price = qty * a
                            # print(refund_price)
                            cust.CustAcc.AccountBalance +=  refund_price
                            self.FlipkartAcc.AccountBalance -= refund_price
                            
                            actual_qty = prod.ProductQuantity
                            prod.ProductQuantity = qty
                            cust.ReturnedProducts.append(deepcopy(prod))
                            prod.ProductQuantity = actual_qty + qty

                            print("-------------------------------------------Before Returning Product Quantity---------------------------------------------")
                            print(cust.OrderedProducts)

                            for i in cust.OrderedProducts:
                                # print(i.ProductQuantity)
                                i.ProductQuantity -= qty
                                # print(i.ProductQuantity)
                            print("-------------------------------------------After Returning Product Quantity---------------------------------------------")
                            print(cust.OrderedProducts)

                else:
                    print(f"Sorry, you have not purchased {qty} {prod} from us.")
            else:
                print(f"Sorry, you have not purchased {prodname} from us.")

        


# if __name__ == '__main__':
#     prod_obj1 = Product(1001, "Tablet", "Electronics", 75000, 10)
#     prod_obj2 = Product(1002, "Denim", "Clothing", 1245, 10)

#     acc_obj = Account("saving", 3500)
    
#     flip_obj = Flipkart("Navi-Mumbai", "Mumbai", 4, [prod_obj1, prod_obj2], acc_obj)
#     flip_obj.show_Flipkartdetail()
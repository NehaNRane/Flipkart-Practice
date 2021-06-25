from nraccount_file import Account
from nrcustomer_file import Customer, Address
from nrflipkart_file import Flipkart, Product, Order


prod_obj_1 = Product(1001, "Laptop", "Electronics", 10000, 5)
prod_obj_2 = Product(1002, "Denim", "Clothing", 151, 10)
prod_obj_3 = Product(1003, "Watch", "Accessories", 5000, 25)
prod_obj_4 = Product(1004, "BMW Car", "Toy", 1215, 2)
prod_obj_5 = Product(1005, "Pan", "Utensils", 6451, 25)
prod_obj_6 = Product(1006, "Basmati Rice", "Groceries", 100, 50)

Product.product_list.extend([prod_obj_1,prod_obj_2,prod_obj_3,prod_obj_4,prod_obj_5,prod_obj_6])
# print(Product.product_list)

flip_acc_obj = Account("Current", 10000)
flip_obj = Flipkart("Navi-Mumbai", "Mumbai", 4, [prod_obj_1, prod_obj_2, prod_obj_3, prod_obj_4, prod_obj_5, prod_obj_6], flip_acc_obj)

ad_obj = Address(1401, "Oval", "Sector-35", 410210, "Kharghar", "Maharashtra")

acc_obj = Account("Saving", 50000)
cust_obj_1 = Customer(123456789, "Neha", ad_obj, acc_obj, "+919541678455", "abc@gmail.com", False)

# acc_obj = Account("Saving", 50000)
# cust_obj_1 = Customer(123456789, "Neha", ad_obj, acc_obj, "+919541678455", "abc@gmail.com", False)

print(cust_obj_1, "Before order")
print("------------------------------------------------------------")
flip_obj.purchase_product("Watch", cust_obj_1, 10)

print(cust_obj_1, "After order")  # 1

print(flip_obj)
print("\n------------------------------- Returning of Product -----------------------------------\n\n")
flip_obj.return_product(cust_obj_1, "Watch", 3)

# flip_obj.return_product(cust_obj_1, "Laptop", 2)
print("\n---------------------------------------After Returning-----------------------------------------------------")
print(cust_obj_1)

print(flip_obj)


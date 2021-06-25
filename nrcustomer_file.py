from nrparent_file import Base
from nraddress_file import Address
from nraccount_file import Account

class Customer(Base):
    """This Class shows details of Customer"""
    def __init__(self, custid, custname, custaddr, custacc, custmobile_no, custemail, isplus_member=False):
        self.CustID = custid
        self.CustName = custname
        self.CustAddress = custaddr
        self.CustAcc = custacc
        str_mobile = str(custmobile_no)
        if str_mobile[:3] == "+91" and len(str_mobile[3:]) == 10:
            self.CustMobileNo = custmobile_no
        else:
            raise ValueError("Invalid Mobile No. Enter again!!!")

        # if "@gmail.com" not in custemail:
        #     raise ValueError("Only Gmail is allowed")
        # self.CustEmail_id = custemail

        if custemail[-10:] == "@gmail.com":
            self.CustEmail_id = custemail
        else:
            raise ValueError("Only Gmail is allowed")
        

        self.PlusMember = isplus_member
        self.OrderedProducts = []
        self.ReturnedProducts = []

    def show_custdetail(self):
        print(f"""
        Customer ID         : {self.CustID}
        Customer Name       : {self.CustName}
        Customer Address    : {self.CustAddress}
        Customer Account    : {self.CustAcc}
        Customer Mobile No. : {self.CustMobileNo}
        Customer Email ID   : {self.CustEmail_id}
        Plus Membership     : {self.PlusMember}
        Ordered Products    : {self.OrderedProducts}
        Returned Products   : {self.ReturnedProducts}
        """)

if __name__ == '__main__':
    addr_obj = Address(1401, "Oval", "Sector-35", 410210, "Kharghar", "Maharashtra")

    acc_obj = Account("saving", 3500)

    cust1 = Customer(101, "Neha", addr_obj, acc_obj, "+919345682389", "abc@gmail.com", True)
    #print(cust1.__dict__)
    cust1.show_custdetail()


from nrparent_file import Base
import random

class Account(Base):
    """This class contains Account related information"""
    def __init__(self, acctype, accbal):
        self.AccountNo = random.randint(11111,99999)
        self.AccountType = acctype
        if accbal <= 3000:
            raise ValueError("Balance should be more than Rs. 3000/-")
        else:
            self.AccountBalance = accbal

    def show_accdetail(self):
        print(f"""
        Account No.      : {self.AccountNo}
        Account Type     : {self.AccountType}
        Account Balance  : {self.AccountBalance}
        """)

if __name__ == '__main__':
    acc_obj = Account("saving", 3500)
    #print(acc_obj.__dict__)
    acc_obj.show_accdetail()
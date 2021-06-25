from nrparent_file import Base

class Address(Base):
    """This Class is for storing Customer's Address"""
    def __init__(self, house_no, building, area, pcode, city, state):
        self.AddrHouse_No = house_no
        self.AddrBuildingName = building
        self.AddrArea = area
        self.AddrPincode = pcode
        self.AddrCity = city
        self.AddrState = state

    def show_address(self):
        print(f"""
        House No      : {self.AddrHouse_No}
        Building Name : {self.AddrBuildingName}
        Area          : {self.AddrArea}
        City          : {self.AddrCity} 
        PinCode       : {self.AddrPincode}
        State         : {self.AddrState}
        """)

if __name__ == '__main__':
    addr_obj = Address(1401, "Oval", "Sector-35", 410210, "Kharghar", "Maharashtra")
    # print(addr_obj)
    addr_obj.show_address()
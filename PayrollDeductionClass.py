class PayrollDeduction:

    def __init__(self,desc,date,amt,ID):
        self.__desc = desc
        self.__date = date
        self.__charge = amt
        self.__employeeID = ID

    
    def get_desc(self):
        return self.__desc

    def get_date(self):
        return self.__date 
    
    def get_amt(self):
        return self.__charge 

    def get_ID(self):
        return self.__employeeID 
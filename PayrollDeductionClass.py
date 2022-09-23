class PayrollDeduction:

    def __init__(self,desc,date,amt,ID):
        self.__desc = desc
        self.__date = date
        self.__charge = amt
        self.__employeeID = ID

    def set_desc(self,desc):
        self.__desc = desc

    def set_date(self,date):
        self.__date = date
    
    def set_amt(self,amt):
        self.__charge = amt

    def set_ID(self,ID):
       return self.__employeeID 
    
    def get_desc(self,desc):
        return self.__desc

    def get_date(self,date):
        return self.__date 
    
    def get_amt(self,amt):
        return self.__charge 

    def get_ID(self,ID):
        return self.__employeeID 
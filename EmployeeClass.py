class Employee:

    def __init__(self,name,ID,dep,title,salary):
        self.__name = name
        self.__ID = ID
        self.__department = dep
        self.__title = title
        self.__salary = salary

    def set_name(self,name):
        self.__name = name
    
    def set_ID(self,ID):
        self.__ID = ID

    def set_dep(self,dep):
        self.__dep = dep
    
    def set_title(self,title):
        self.__salary = salary 

    def get_name(self,name):
        return self.__name
    
    def get_ID(self,ID):
        return self.__ID

    def get_dep(self,dep):
        return self.__dep 
    
    def get_title(self,title):
        return self.__salary  


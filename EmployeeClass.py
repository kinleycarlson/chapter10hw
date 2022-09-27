class Employee:

    def __init__(self,name,ID,dep,title,salary):
        self.__name = name
        self.__ID = ID
        self.__dep = dep
        self.__title = title
        self.__salary = salary

  
    def get_name(self):
        return self.__name
    
    def get_ID(self):
        return self.__ID

    def get_dep(self):
        return self.__dep 
    
    def get_title(self):
        return self.__title

    def get_salary(self):
        return self.__salary  


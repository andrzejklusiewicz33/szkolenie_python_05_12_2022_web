class Fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Author:
    def __init__(self,first_name,last_name,email):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email


class Employee:
    def __init__(self,employee_id,first_name,last_name,salary,comment):
        self.employee_id=employee_id
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        self.comment=comment
    def __str__(self):
        return str(self.__dict__)

class Product:
    def __init__(self,product_id,name,price,description,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.description=description
        self.stock=stock
    def __str__(self):
        return str(self.__dict__)
class Accounts:
    def __init__ (self , bal ,acc):
        self.baclance=bal
        self.account_no= acc
        
    def debits(self , ammount):
        self.baclance-=ammount
        print("RS." , ammount , "was debits")
        print("total blance is", self.baclance)
    def credits(self, ammount):
        self.baclance += ammount
        print("RS.", ammount , "is cridets")
        print("total blances is ", self.baclance)
        
    def get_balance(self):
        return self.baclance
          
acc1=Accounts(10000, 9823221)
acc1.debits(1000)
acc1.credits(1)


class Cricle:
    
    def __init__ (self, redies):
        self.redies=redies
        
    def area(self):
        return (22/7)* self.redies ** 2
    
    def perameter(self):
        return 2 * (22/7) * self.redies
    
    
c1 = Cricle(21)
print (c1.perameter())
print (c1.area())

class Empolyee:
    def __init__ (self , dept , role , salary):
        self.dept=dept
        self.role=role
        self.salary=salary
        
    def show_details(self):
        print("dept :" , self.dept)
        print("role :" , self.role)
        print("salary :", self.salary)
e1 = Empolyee("IT", "Software Developer", 70000)
e1.show_details()
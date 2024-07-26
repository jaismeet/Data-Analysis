class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
        
    def debit(self,amount):
        self.balance-=amount
        print(amount,"was debited")
        # print(self.get_balance())
        
    def credit(self,amount):
        self.balance+=amount
        print(amount,"was credited")
        
    def get_balance(self):
        return self.balance
            
        
acc1=Account(10000,12345) 
acc1.debit(1000)
acc1.credit(2000)
print(acc1.get_balance())     

print("----------------------------------------------------")

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
         
    def showdetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept)
        print("salary =", self.salary)
        
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","d1",30000)
          
        
e1=Engineer("elon musk",40)  
e1.showdetails()

        
        
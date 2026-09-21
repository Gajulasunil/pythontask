''' task 1.Employee Details'''
class Employee:
    def __init__(self,id,name,salary):
        self.id = id 
        self.name = name
        self.salary = salary
    def display_employee(self):
        print("employee id :",self.id)
        print("employee name:",self.name)
        print("employee salary :",self.salary)
e = Employee(101,"ramesh",30000)
e.display_employee()
'''TASK 2. mobile details'''
class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def display_mobile(self):
        print("mobile brand :",self.brand)
        print("mobile model :",self.model)
        print("mobile price :",self.price)
m = Mobile("samsung","s20",50000)
m.display_mobile()
m1 = Mobile("apple","iphone 15",150000)
m1.display_mobile()
'''Task 3. bank Account'''
class BankAccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def display_account(self):
        print("account number :",self.account_number)
        print("account holder name:",self.account_holder_name)
        print("account balance :",self.balance)
b = BankAccount(123333,"sunil",50000)
b.display_account()


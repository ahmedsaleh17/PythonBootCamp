# object oriented programming -- getter & setter 
class Member: 
    def __init__(self, name):
        self.__name = name   # Private


    def get_name(self):
        return self.__name
    
    def set_name(self, new_name): 
        self.__name =  new_name

    

    def greeting(self):
        return f"Hello {self.__name}"

# object oriented programming -- property decorator
class Employee: 
    def __init__(self, name, salary):
        self.name = name      # goes through setter 
        self.salary = salary  # goes through setter

    # getter and setter but using @property decorator 
    
    # getter method but we treat as property
    @property 
    def name(self):
        return self.__name
    
    # setter 
    @name.setter
    def name(self, new_name):
        # validation check 
        if not new_name.isalpha(): 
            raise ValueError("Enter only letters")
        self.__name = new_name
    
    # get salary 
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        # validation check 
        if new_salary > 5000:
            self.__salary = new_salary
        else: 
            print('Invalid Salary')


    def gretting(self):
        # you can cass the private attriputes only inside the class
        return f"hello {self.__name}"

# bank account class 
class Account: 
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    # define getter and setters 
    @property 
    def name(self): 
        return self.__name
    
    @name.setter
    def name(self, new_name):
        # validation check 
        if new_name.isalpha():
            self.__name = new_name
        else:
            raise ValueError('Names should only be letters')


    @property 
    def balance(self):
        return self.__balance 

    @balance.setter 
    def balance(self, new_balance):
        # validation 
        """
        Docstring for balance setter
        
        :param self: refer to the object
        :param new_balance: the value of balance should be greater than 1000 (businees rule)
        """
        if new_balance >= 1000:
            self.__balance = new_balance
        else: 
            raise ValueError('Invalid balance, please enter values greater than or equal 1000')


    def __str__(self):
        return f"Account's {self.__name} has amount balance {self.__balance}"


    def deposite(self, amount):
        if amount > 0 :
            self.__balance += amount
        else: 
            raise ValueError("Invalid input, please Enter positive number")
    
    def withdraw(self, amount):
        if amount > 0:
            if  self.__balance > amount:
                self.__balance -= amount
            else: 
                print("sorry, you don't have enough balance")
        else: 
            raise ValueError("Invalid input, please Enter positive number")



# object oriented programming -- inhertience 
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname +'.'+lname+'@email.com'


class Teacher(Employee):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.email = 't-'+self.email



if __name__ == '__main__':

    # member1 = Member('ahmed')

    # print(member1.get_name())

    # member1.set_name('Mariam')
    # print(member1.get_name())


    # ----------------------------------

    # emp1 = Employee('ahmed', 5500)
    # print(emp1.name)                # looks like public access, but it's the getter
    # print(emp1.salary)
    
    # print(emp1.gretting())
    # print(emp1.__name)    # AttributeError: 'Employee' object has no attribute '__name'.
    
    # emp1.name = 'mariam'            # looks like direct assignment, but it's the setter
    # emp1.salary = 5000
    
    # print(emp1.name)
    # print(emp1.salary)

    # print(emp1.salary)

    # --------------------------------------



    # acct1 = Account('Ahmed', 1500)
    
    # # print(acct1.name)
    # print(acct1.balance)

    # acct1.deposite(550)
    # print(acct1.balance)

    # acct1.withdraw(1000)
    # print(acct1.balance)
    
    # acct1.withdraw(500)
    # print(acct1.balance)

    # -------------------------------------

    tr1 = Teacher('rabie', 'omran')
    print(tr1.email)
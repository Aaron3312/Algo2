from abc import ABC, abstractmethod

class Company(ABC):
    @abstractmethod
    def get_employee(self):
        pass

    @abstractmethod
    def create_software(self):
        pass

class Employee(ABC):
    @abstractmethod
    def do_work(self):
        pass

class Developer(Employee):
    def do_work(self):
        print('Coding')

class Tester(Employee):
    def do_work(self):
        print('Testing')

class Designer(Employee):
    def do_work(self):
        print('Designing')
    
class GameDevCompany(Company):
    def get_employee(self):
        return [Developer(), Tester(), Designer()]
    
class OutsourcingCompany(Company):
    def get_employee(self):
        return [Developer(), Tester()]


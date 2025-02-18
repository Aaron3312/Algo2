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





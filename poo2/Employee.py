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
    
    def create_software(self):
        return print("Providing software for game development")

class OutsourcingCompany(Company):
    def get_employee(self):
        return [Developer(), Tester()]
    
    def create_software(self):
        return print("Providing software for outsourcing")
    

def main():
    game_dev_company = GameDevCompany()

    for employee in game_dev_company.get_employee():
        employee.do_work()

    
if __name__ == '__main__':
    main()


# necesitamos crear una clase de tipo personaje que tenga atributos de forma especifica, y implementar unos metodos que por medio de polimorfismo cada uno de los personajes pueda usar, pero usar un contexto original, no de un videojuego talvez algo mas 
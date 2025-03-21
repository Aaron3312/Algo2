class Computer:
    def _init_(self, cpu, ram, storage, gpu):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def displaySystem(self):
        print(f"{self.cpu} {self.gpu or "No tiene GPU"} {self.storage} {self.ram}")

class ComputerBuilder:
    def _init_(self):
        self.computer = Computer(None,None,None,None)

    def setRam(self, ram):
        self.computer.ram = ram
        return self
    
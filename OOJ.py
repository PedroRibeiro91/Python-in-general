
class Computer:

    def __init__(self, cpu, rom, ram, gpu, price):
        self.cpu = cpu
        self.rom = rom
        self.ram = ram
        self.gpu = gpu
        self.price = price

    def configuration(self):
        print("This computer comes with a", self.cpu, "processor", self.rom, "memory", self.ram, "RAM and a",
         self.gpu, "graphics card")

    def cost(self):
        print("This computer is sold for", self.price)




computer1 = Computer('i7','512gb SSD', '16gb', 'gtx1080', 1500)

computer1.configuration()
computer1.cost()
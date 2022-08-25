from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    model: str
    price: int

    @abstractmethod
    def build(self, count):
        pass


class Printer(OfficeEquipment):
    model = 'printer001'
    price = 5000
    printing_technology = 'laser'

    def build(self, **kwargs):
        printers = []
        count = 1
        for x in range(count):
            printers.append([Printer.model, Printer.price])
        return printers

    def extend(self, printers):
        pass


class Scanner(OfficeEquipment):
    model = 'scanner012'
    price = 3000
    scanner_type = 'flatbed type'

    def build(self, **kwargs):
        count = 1
        scanners = []
        for x in range(count):
            scanners.append([Scanner.model, Scanner.price])
        return scanners

    def extend(self, scanners):
        pass


class Copier(OfficeEquipment):
    model = 'copier006'
    price = 4000
    copier_type = 'digital-type'

    def build(self, **kwargs):
        count = 1
        copiers = []
        for x in range(count):
            copiers.append([Copier.model, Copier.price])
        return copiers

    def extend(self, copiers):
        pass


class Stock(Copier, Scanner, Printer):
    max_count: int
    printers: list
    scanners: list
    copiers: list

    def __init__(self, count=10):
        self.max_count = count
        self.printers = []
        self.scanners = []
        self.copiers = []

    @classmethod
    def store(cls, printers: Printer, scanners: Scanner, copiers: Copier):
        printers.extend(printers)
        scanners.extend(scanners)
        copiers.extend(copiers)
        return f'{printers}, {scanners}, {copiers}'


printer = Printer()
scanner = Scanner()
copier = Copier()
stock = Stock(10)
printer_list = printer.build()
scanner_list = scanner.build()
copier_list = copier.build()
stock.store(printer_list, scanner_list, copier_list)
print(Stock.store(printer_list, scanner_list, copier_list))

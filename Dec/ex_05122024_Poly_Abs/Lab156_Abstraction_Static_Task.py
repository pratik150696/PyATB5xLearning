from abc import ABC, abstractmethod


class PC(ABC):

    def start_pc(self):
        pass


class MotherBoard(PC):

    @abstractmethod
    def start_motherboard(self):
        pass


class Ram(MotherBoard):

    @abstractmethod
    def start_ram(self):
        pass


class Processor(Ram):

    @abstractmethod
    def start_processor(self):
        pass


class Storage(Processor):

    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def load_OS():
        print("Loading OS")

    def start_mouse(self):
        pass

    def use_headphone(self):
        pass


class TC1(Storage):
    def start_pc(self):
        print("Starting PC")

    def start_motherboard(self):
        print("MotherBoard is Starting")

    def start_ram(self):
        print("Ram is Starting")

    def start_processor(self):
        print("Starting Processor")

    def storage_data(self):
        print("Printing Storage Data")

    def start_mouse(self):
        print("Starting Mouse")

    def use_headphone(self):
        print("Using Headphones")

    def task(self):
        self.start_pc()
        self.start_motherboard()
        self.start_ram()
        self.start_processor()
        self.storage_data()
        self.start_mouse()
        self.use_headphone()
        Storage.load_OS()


tc1_object = TC1()
tc1_object.task()

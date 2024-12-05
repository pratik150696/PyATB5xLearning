from abc import ABC, abstractmethod


class GearBox(ABC):

    @abstractmethod
    def set_gear(self):
        pass


class Engine(GearBox):

    @abstractmethod
    def start(self):
        super().set_gear()
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Starting")

    def stop(self):
        print("Stopping")

    def set_gear(self):
        print("Gearbox is Ready")

    def drive(self):
        self.start()
        self.stop()
        self.set_gear()

car_ref = Car()
car_ref.drive()
from abc import ABC, abstractmethod

class Father(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass


class Son(Father):

    def loan(self):
        print("1L Loan")

son_ref = Son("Pratik")
son_ref.loan()

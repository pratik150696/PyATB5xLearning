from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):

    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def stop_browser(self):
        pass

class TC1(Browser):


    def start_browser(self):
        print("Starting Browser")


    def stop_browser(self):
        print("Stopping Browser")

    def readFromExcel(self):
        print("ReadFromExcel is Ready")

    def run_test(self):
        self.start_browser()
        self.stop_browser()
        self.readFromExcel()

tc1_ref = TC1()
tc1_ref.run_test()
class BaseTest:

    def open_browser(self):
        print("Starting the Browser!!!")

    def read_from_excel(self):
        print("Read From Excel File")

    def close_browser(self):
        print("Closing the Browser")


class TestCase1(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Tset Case P1 Executed")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Tset Case N1 Executed")
        self.close_browser()


class TestCase2(BaseTest):

    def test_2(self):
        self.open_browser()
        print("Tset Case 2 Executed")
        self.close_browser()


class TestCase3(BaseTest):

    def test_3(self):
        self.open_browser()
        print("Tset Case 3 Executed")
        self.close_browser()

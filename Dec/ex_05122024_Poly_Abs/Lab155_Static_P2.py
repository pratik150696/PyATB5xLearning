class ExcelReader:

    @staticmethod
    def read_from_excel():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def read_mysql_file():
        print("Reading from MYSQL")

class TC1:

    def test_case(self):
        ExcelReader.read_from_excel()
        MYSQLDBConnection.read_mysql_file()

tc1_obj = TC1()
tc1_obj.test_case()


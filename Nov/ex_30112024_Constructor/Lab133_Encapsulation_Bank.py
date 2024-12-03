class Bank:

    def __init__(self,account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_account_number(self):

            print(self.__account_number)


    def __internal_private_method(self):
        print("Private Method, can only access by Class")

icici = Bank(982843175779, 500)
icici.check_balance()
icici.deposit(200)
icici.check_balance()
icici.show_me_account_number()
# icici.__internal_private_method         -----> Not Allowed
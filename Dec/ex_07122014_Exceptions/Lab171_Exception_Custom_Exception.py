# Custom Exception    (Optional)

class LowBalanceExceptionCustom(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the Amount: "))

if withdraw > balance:
    raise LowBalanceExceptionCustom("Balance is Low")
else:
    print("Remaining Amount is", (balance-withdraw))
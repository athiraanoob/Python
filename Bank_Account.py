class BankAccount:
    def __init__(self):
        self.__private = "balance"

    def balance(self):
        print(f"The amount Present in Bank {self.__private}")

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, value):
        self.__private = value

    # Transaction modules
    def deposit(self, amount_to_add):
        new_balance_after_deposit = self.private + amount_to_add
        self.private = new_balance_after_deposit
        return self.private

    def withdrawel(self, amount_withdrawn):
        print(self.private,amount_withdrawn)
        new_balance_after_withdraw = self.private - amount_withdrawn
        self.private=new_balance_after_withdraw
        return self.private


bk = BankAccount()
bk.private = 800
bk.balance()
amt = bk.deposit(300)
imbalance = bk.withdrawel(400)
print(f" Balance Amount after deposit {amt}")
print(f" Balance amount after withdrawel {imbalance}")

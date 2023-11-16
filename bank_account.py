class BankAccount:

    default_account_number = 1

    def __init__(self, balance, account_owner):
        self.balance = balance
        self.account_owner = account_owner
        self.account_number = BankAccount.default_account_number
        BankAccount.default_account_number += 1

    def __repr__(self):
        return f'BankAccount({self.balance}, {self.account_owner})'

    def __str__(self):
        return f'Bank account number {self.account_number} belonging to {self.account_owner}'

    def depose_money(self, money_amount):
        self.balance += money_amount

    def withdraw_money(self, money_amount):
        if money_amount <= self.balance:
            self.balance -= money_amount
        else:
            print(f'Your balance is too low to withdraw {money_amount}')

    def check_balance(self):
        print(f'Your balance is {self.balance}')



if __name__ == '__main__':
    bank_account_zac = BankAccount(1000, 'Zac Rozenberg')
    print(bank_account_zac)
    bank_account_zac.check_balance()

    bank_account_zac.depose_money(50)
    bank_account_zac.check_balance()

    bank_account_zac.withdraw_money(900)
    bank_account_zac.check_balance()

    bank_account_zac.withdraw_money(1100)
    bank_account_zac.check_balance()

    bank_account_eden = BankAccount(2000, 'Eden Borberg')
    print(bank_account_eden)


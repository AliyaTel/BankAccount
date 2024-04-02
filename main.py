class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class Bank:
    def __init__(self):
        self.accounts = {}
        self.customers = {}

    def add_customer(self, first_name, last_name, passport_number):
        human = Customer(first_name, last_name, passport_number)
        self.customers[passport_number] = human

    def add_account(self, account, customer):
        self.accounts[customer] = account

    def deposit(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.deposit(amount)

    def withdraw(self, passport_number, amount):
        account = self.get_customer_account(passport_number)
        account.withdraw(amount)

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError("Клиент не найден")
        return self.customers[passport_number]

    def get_customer_account(self, passport_number):
        use = self.get_customer(passport_number)
        if use not in self.accounts:
            raise KeyError("аккаунт не найден")
        return self.accounts[use]


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.amount = 0
        self.currency = currency

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            raise ValueError("Недостаточно денег на счету")
        self.amount -= amount



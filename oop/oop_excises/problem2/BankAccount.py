class BankAccount:
    # Class variable to keep track of the next account ID
    ID = 1

    def __init__(self, name, balance=0):
        self._id = BankAccount.ID
        BankAccount.ID += 1
        self._name = name
        self._balance = balance

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            raise ValueError("Deposit amount must be positive")

    def withdrawal(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            raise ValueError("Insufficient balance or invalid withdrawal amount")

    def __str__(self):
        return f"BankAccount(ID: {self._id}, Name: {self._name}, Balance: {self._balance})"

# Example usage
account1 = BankAccount("Alice", 1000)
print(account1)
account1.deposit(500)
print(account1)
account1.withdrawal(200)
print(account1)

account2 = BankAccount("Bob", 500)
print(account2)

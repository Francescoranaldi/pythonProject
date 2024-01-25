class AccountTransaction:
    def __init__(self, account_id, transaction_type, amount):
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount

    def __repr__(self):
        return f'AccountTransaction[{self.account_id}, {self.transaction_type}, {self.amount}]'


class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        self.transactions = []  # List to store AccountTransaction objects

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            raise InvalidAmountException(f'Amount is invalid: {amount}')

        self._balance += amount
        transaction = AccountTransaction(self.id, "Deposit", amount)
        self.transactions.append(transaction)

    def charge(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0 or amount > self._balance:
            raise InvalidAmountException(f'Amount is invalid or insufficient funds: {amount}')

        self._balance -= amount
        transaction = AccountTransaction(self.id, "Charge", amount)
        self.transactions.append(transaction)

    def __repr__(self):
        return f'Account[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.customer_list = []
        self.account_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        # Find "from" and "to" accounts based on the provided ids
        from_account = next((acc for acc in self.account_list if acc.id == from_account_id), None)
        to_account = next((acc for acc in self.account_list if acc.id == to_account_id), None)

        if from_account and to_account:
            # Perform the transfer
            from_account.charge(amount)
            to_account.deposit(amount)
        else:
            raise BankException("Invalid account ids for transfer")

    def find_account(self, account_id):
        return next((acc for acc in self.account_list if acc.id == account_id), None)

    def __repr__(self):
        return f'Bank[{self.customer_list}; {self.account_list}]'


class BankException(Exception):
    pass


class InsufficientFundsException(BankException):
    pass


class InvalidAmountException(BankException):
    pass


# Example Usage:
if __name__ == "__main__":
    bank = Bank()

    c = bank.create_customer('John', 'Brown')
    a = bank.create_account(c)
    a2 = bank.create_account(c)

    c2 = bank.create_customer('Anne', 'Smith')
    a3 = bank.create_account(c2)

    try:
        a.deposit(330)
        a3.deposit(-100)
        a2.deposit(-50)
    except BankException as ie:
        print(f'Something went wrong {ie}')

    for acc in bank.account_list:
        print(f"Account {acc.id} Transactions:")
        for transaction in acc.transactions:
            print(f"{transaction.transaction_type}: {transaction.amount}")

    print('before transfer')
    print(bank)

    try:
        bank.transfer(from_account_id=a3.id, to_account_id=a2.id, amount=140)
    except BankException as e:
        print(f"Transfer failed: {e}")

    print('after transfer')
    print(bank)

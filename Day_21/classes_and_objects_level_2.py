# Day 21 - Level 2

class PersonAccount():
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        sum = 0
        for i in self.incomes:
            sum += i[0]
        return sum

    def total_expense(self):
        sum = 0
        for e in self.expenses:
            sum += e[0]
        return sum

    def account_info(self):
        return f"First Name: {self.firstname}\nLast Name: {self.lastname}\nIncomes: {self.incomes}\nExpenses: {self.expenses}"

    def add_income(self, income):
        self.incomes.add(income)

    def add_expense(self, expense):
        self.expenses.add(expense)

    def account_balance(self):
        return self.total_income() - self.total_expense()



person = PersonAccount(
    firstname="Jane",
    lastname="Doe",
    incomes={
        (2500, "Monthly salary"),
        (200, "Freelance project"),
        (150, "Online sales")
    },
    expenses={
        (800, "Rent"),
        (250, "Groceries"),
        (60, "Internet and phone"),
        (100, "Transportation"),
        (120, "Electricity and water")
    }
)

print(f"Total income: {person.total_income()}")
print(f"Total expense: {person.total_expense()}")
print(f"Account info: {person.account_info()}")
person.add_income((200, "Console sale"))
person.add_expense((70, "Ocarina of Time purchase"))
print(f"Total income: {person.total_income()}")
print(f"Total expense: {person.total_expense()}")
print(f"Account info: {person.account_info()}")
print(f"Account balance: {person.account_balance()}")

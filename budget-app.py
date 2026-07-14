class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    percentages = []
    for spent in spent_amounts:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((spent / total_spent) * 10) * 10)

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for pct in percentages:
            if pct >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_len = max([len(cat.name) for cat in categories])
    names = [cat.name.ljust(max_len) for cat in categories]

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"

    return chart
food = Category("Food")
food.deposit(100, "deposit")
food.withdraw(10, "groceries")
print(food)
print(create_spend_chart([food]))
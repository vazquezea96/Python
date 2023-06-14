class Category:

    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "you have successfully deposited {} in {} category. You now have {}".format(amount, self.category, self.amount)

    def check_balance(self):
        return "your balance is {} in {} category.".format(self.amount, self.category)

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawed {} from {} category. You now have {}".format(amount, self.category, self.amount)

    def transfer(self, amount, category):
        category.amount -= amount
        self.amount += amount
        return "You have transfered {} in {} category to {} category".format(amount, category.category, self.category)


clothing_category = Category("Clothing", 400)
food_category = Category("Food", 500)
car_category_ = Category("Entertainment", 1000)

print(food_category.deposit(250))

print(food_category.check_balance())

print(food_category.withdraw(250))

print(food_category.transfer(250, car_category_))

print(food_category.check_balance())

print(car_category_.check_balance())

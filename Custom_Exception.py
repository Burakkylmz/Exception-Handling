

class InvalidWidthDrawal(Exception):
    def __init__(self, balance, amaount):
        super().__init__("Acccount doesn't have ${}".format(amaount))
        self.amount = amaount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


# raise InvalidWidthDrawal(25, 50)

try:
    raise InvalidWidthDrawal(
        int(input("Please type into balance: ")),
        int(input("Please type into amount: ")))
except InvalidWidthDrawal as e:
    print("I'm sorry, but your withdrawal is more then your balance by ${}".format(e.overage()))
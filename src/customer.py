class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def buy_drink(self, pub, drink):
        self.wallet -= drink.price
        pub.increase_till(drink.price)
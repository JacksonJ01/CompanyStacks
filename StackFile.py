# Jackson J.
# 3/9/2020
# A program that simulates the order system for a small paper supply company.
# The company gets in cases of paper that it then resells at a 10% profit
from LinkedStacks import Stack
MyStack = Stack()
MyCost = Stack()


def menu_(self=None):
    inventory = 0
    profit = 0
    menu = input("\n1. ADD to inventory"
                 "\n2. SELL from inventory"
                 "\n3. check PROFIT to date"
                 "\n>>>").title()

    if menu != 'ADD' or menu != 1 or menu != 'SELL' or menu != 2 or menu != 'Profit' or menu != 3:
        print('Can you repeat that for me')
        menu_()

    elif menu == 'ADD' or menu == 1:
        add = int(input("How many items do you wish to add to the inventory? (whole numbers only)"
                        "\n>>>"))
        self.MyStack.push(add)
        inventory += add
        cost = int(input("\nHow much does each item cost? (whole numbers only)"
                         "\n>>>"))
        self.MyCost.push(cost)
        print(f"{add} items added at ${cost} each")
        return inventory

    elif menu == 'SELL' or menu == 2:
        sell = int(input("How many items do you wish to sell from the inventory? (whole numbers only)"
                         "\n>>>"))

        if sell > inventory:
            print("Request too large")
            menu_()
            return

        inventory -= sell

        value = self.MyStack.head.data

        if value > sell:
            self.MyStack.pop()
            self.MyStack.push(value - sell)
            print((self.MyCost * 1.1) * sell)
            profit += (self.MyCost * 1.1) * sell
            menu_()
            return profit

        elif value < sell:
            holder = 0
            while sell >= 0:
                if value > sell:
                    value = value - sell
                    self.MyStack.pop()
                    self.MyStack.push(value)
                    check = 0
                    total = []
                    while check < holder:
                        total.append(self.MyCost.head.data)
                        self.MyCost.pop()
                        check += 1
                    print(sum(total) / holder * 1.1 * sell)
                    profit += (sum(total) / holder * 1.1 * sell)
                    menu_()
                    return profit
                sell = sell - value
                self.MyStack.pop()
                value = self.MyStack.head.data
                holder += 1
                menu_()
            return

    elif menu == 'PROFIT' or menu == 3:
        print(f'Your profit to date is {profit}')
        menu_()
        return

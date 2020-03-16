# Jackson J.
# 3/9/2020
# A program that simulates the order system for a small paper supply company.
# The company gets in cases of paper that it then resells at a 10% profit
from LinkedStacks import Stack
MyStack = Stack()
MyCost = Stack()
Inventory = 0
Profit = 0
menu = 'Hello World'

while menu != 'Exit' or menu == '4':
    print('\nCurrent Inventory:', Inventory)
    menu = input("\n1. ADD to inventory"
                 "\n2. SELL from inventory"
                 "\n3. check PROFIT to date"
                 "\n4. EXIT"
                 "\n>>>").title()

    if menu == 'Add' or menu == '1':
        add = int(input("How many items do you wish to add to the inventory? (whole numbers only)"
                        "\n>>>"))
        MyStack.push(add)
        Inventory += add
        cost = int(input("\nHow much does each item cost? (whole numbers only)"
                         "\n>>>"))
        MyCost.push(cost)
        print(f"{add} items added at ${cost} each")

    elif menu == 'Sell' or menu == '2':
        sell = int(input("How many items do you wish to sell from the inventory? (whole numbers only)"
                         "\n>>>"))
        value = MyStack.head()

        if sell > Inventory:
            print(f"Request too large:"
                  f"\nYou have {Inventory} items in your inventory")

        elif value > sell:
            MyStack.pop()
            MyStack.push(value - sell)
            print((MyCost.head() * 1.1) * sell - MyCost.head())
            Profit += ((MyCost.head() * 1.1) * sell - MyCost.head())
            Inventory -= sell

        elif value < sell:
            holder = 0
            while sell >= 0:
                if value > sell:
                    value = value - sell
                    MyStack.pop()
                    MyStack.push(value)
                    check = 0
                    total = []
                    while check < holder:
                        total.append(MyCost.head())
                        MyCost.pop()
                        check += 1
                    print(sum(total) / holder * 1.1 * sell - MyCost.head())
                    Profit += (sum(total) / holder * 1.1 * sell - MyCost.head())
                    Inventory -= sell
                sell = sell - value
                MyStack.pop()
                value = MyStack.head()
                holder += 1
            Inventory -= sell

    elif menu == 'Profit' or menu == '3':
        print(f'Your profit to date is ${Profit}')

print("Thanks for the data")

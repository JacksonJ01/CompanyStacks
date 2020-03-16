# Jackson J.
# 3/9/2020
# A program that simulates the order system for a small paper supply company.
# The company gets in cases of paper that it then resells at a 10% profit
from LinkedStacks import Stack
from getpass import getuser
from time import sleep
terminal = getuser()

MyStack = Stack()
MyCost = Stack()
Inventory = 0
Profit = 0
menu = 'Hello World'


input("CLICK HERE, THEN PRESS ENTER")

name = input("\nHello there user, what is your name?"
             "\n>>>").title()

sleep(1)
print("\nI like that name a lot."
      f"\n{name}\b\b\b, {name}\b\b, {name}"
      f"\n{name} rolls off the tongue nicely.")

sleep(2.5)
print(f'\nAs you may know I, {terminal} (your terminal), have a LIFO inventory set up for you to use.'
      "\nAnd now that I've mentioned this, it's only natural for me to take you to the menu."
      "\nHave fun XD")

input("\nPress Enter")

while menu != 'Exit' or menu != '4':
    sleep(1)
    print('\nCurrent Inventory:', Inventory)
    menu = input("\n1. ADD to inventory"
                 "\n2. SELL from inventory"
                 "\n3. check PROFIT to date"
                 "\n4. EXIT"
                 "\n>>>").title()

    if menu == 'Add' or menu == '1':
        add = 'Hello World'
        while add != int:
            add = input("\nHow many items do you wish to add to the inventory?"
                        "\n>>>")
            try:
                if int(add) > 0:
                    add = int(add)
                    break
                else:
                    print("Enter a whole number greater than 0.")
            except ValueError:
                print("Why are you typing letters, words and or floats?"
                      "\nEnter a whole number greater than 0.")

        MyStack.push(add)
        Inventory += add

        cost = "Hello World"
        while cost != int:
            cost = input("\nHow much does each item cost?"
                         "\n>>>")
            try:
                if int(cost) > 0:
                    cost = int(cost)
                    break
                else:
                    print("Enter a number greater than 0.")
            except ValueError:
                try:
                    if float(cost) > 0:
                        cost = float(cost)
                        break
                    else:
                        print("Enter a number greater than 0.")
                except ValueError:
                    print("Why are you typing letters and words?"
                          "\nOnly enter numbers.")

        MyCost.push(cost)
        print(f"{add} items added at ${cost} each.")

    elif menu == 'Sell' or menu == '2':
        sell = "Hello World"
        while sell != int:
            sell = input("How many items do you wish to sell from the inventory?"
                         "\n>>>")
            try:
                if int(sell) > 0:
                    sell = int(sell)
                    break
                else:
                    print("Enter a whole number greater than 0.")
            except ValueError:
                print("Why are you typing letters, words and or floats?")

        value = MyStack.head()

        if sell > Inventory or value is None:
            print(f"Request too large:"
                  f"\nYou have {Inventory} items in your inventory.")

        elif value > sell or value == sell:
            if value == sell:
                MyStack.pop()
                made = int(MyCost.head() * 1.1 * sell)
                profit = abs(made - (MyCost.head() * sell))
                MyCost.pop()
                print(f'You made ${made}, with a profit of ${profit}.')
                Profit += profit
                Inventory -= sell
            elif value > sell:
                MyStack.pop()
                MyStack.push(value - sell)
                made = MyCost.head() * 1.1 * sell
                profit = made - MyCost.head() * sell
                print(f'You made ${made: .2f}, with a profit of ${profit: .2f}.')
                Profit += profit
                Inventory -= sell

        elif value < sell or Inventory > sell or Inventory == sell:
            sold = sell
            Inventory -= sell
            total_cost = []
            divider = 0
            while sell >= 0:
                if sell - value <= 0:
                    if sell - value == 0:
                        MyStack.pop()
                        total_cost.append(MyCost.head())
                        divider += 1
                        MyCost.pop()
                    elif value - sell > 0:
                        MyStack.pop()
                        MyStack.push(value)
                        total_cost.append(MyCost.head())
                        divider += 1
                    break
                sell -= value
                MyStack.pop()
                total_cost.append(MyCost.head())
                divider += 1
                MyCost.pop()
                value = MyStack.head()
            made = (sum(total_cost) / divider) * 1.1 * sold
            profit = made - (sold * sum(total_cost) / divider)
            print(f"You made ${made: .2f}, with a profit of ${profit: .2f}.")
            Profit += profit

    elif menu == 'Profit' or menu == '3':
        print(f'Your profit to date is ${Profit}.')

    elif menu == 'Exit' or menu == '4':
        print(f"\nThanks for playing {name}."
              f"\nI mean it, from one terminal, to another."
              f"\n{terminal} over and out")
        break

# Jackson Jared
# 02/26/20
# This file will contain the 2 classes that will allow the creation and alteration of LinkedLists
from random import *


# This creates the Data class which will allow the insertion of data along with its node, or pointer to the next Link
class Data:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# This is the LinkedLink class which
class LinkedList:

    # Creates the head node, which points to the list
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Data(data)
        new_node.next = self.head
        self.head = new_node
        return

    def add_end(self, data):
        new_node = Data(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return

    def rem_front(self):
        gone = self.head
        self.head = self.head.next
        return f"{gone.data} was removed from the front of the Linked List."

    def rem_end(self):
        gone = self.head
        previous = self.head
        if self.head is None:
            return "There is nothing to remove."
        while gone.next is not None:
            previous = gone
            gone = gone.next
        previous.next = None
        return gone.data, "was removed from the Linked List."

    def search1(self, check):
        elements = self.display()
        for element in elements:
            if check == element:
                return True
        return False

    def search2(self, check):
        current = self.head
        if self.head.data == check:
            return True
        while current.next is not None:
            if current.data == check:
                return True
            current = current.next
        if current.data == check:
            return True
        return False

    # For these methods, remove1 and remove2, I had the problem where i set the previous.next to None and that got rid of the list.
    # It took me a while to realize i needed to set it equal to previous.next.next
    # Because previous.next points to the data that points to the rest of the list and i got rid of that piece.
    def remove1(self, delete):
        if delete == self.head.data:
            self.head = self.head.next
            return
        gone = self.head
        previous = self.head
        if self.search1(delete) is True:
            while gone.next is not None or gone.data == delete:
                if gone.data == delete:
                    previous.next = previous.next.next
                    return f'Link deleted! {gone.data} is no longer included'
                previous = gone
                gone = gone.next
            return f'Link deleted! {gone.data} is no longer included'
        return 'No value to remove'

    # adding .data to the end of the if delete == self.head made it work, along with adding the or done.data == delete for these 2 remove methods
    def remove2(self, delete):
        if delete == self.head.data:
            self.head = self.head.next
            return
        gone = self.head
        previous = self.head
        while gone.next is not None or gone.data == delete:
            if gone.data == delete:
                previous.next = previous.next.next
                return f'{gone.data} has been removed'
            previous = gone
            gone = gone.next
        else:
            return 'No data to remove'

    def display(self):
        elements = []
        if self.head is None:
            print(elements)
            return
        current = self.head
        while current.next is not None:
            elements.append(current.data)
            current = current.next
        elements.append(current.data)
        return elements

    def dis_elm(self):
        return f'\nThe items in this Linked List are:\n{self.display()}'

    def clear_all(self):
        self.head = None
        self.dis_elm()
        return "All values have been removed"

    #
    #
    #
    #

    def interface(self):
        rand = randint(1, 20)
        do = input("\n\n- PREPEND"
                   "\n- APPEND"
                   "\n- REMOVE FORM HEAD"
                   "\n- REMOVE FROM END"
                   "\n- REMOVE A VALUE"
                   "\n- SEARCH LIST"
                   "\n- DISPLAY LIST"
                   "\n- CLEAR ALL"
                   "\n- EXIT"
                   "\n\n>>>").title()

        if do == 'Pre':
            add = input("What value would you like to add to the list?"
                        "\n>>>")
            self.add_head(add)
            self.interface()
            return

        elif do == 'App':
            add = input("What value would you like to add to the list?"
                        "\n>>>")
            self.add_end(add)
            self.interface()
            return

        elif do == 'Rh':
            self.rem_front()
            self.interface()
            return

        elif do == 'Re':
            self.rem_end()
            self.interface()
            return

        elif do == 'R':
            remove = input("What value would you like to remove from the list?"
                           "\n>>>")
            if rand <= 10:
                self.remove1(remove)
            elif rand >= 11:
                self.remove2(remove)
            self.interface()
            return

        elif do == 'S':
            search = input("What value would you like to search from the list?")
            if rand <= 10:
                self.search1(search)
            elif rand >= 11:
                self.search2(search)
            self.interface()
            return

        elif do == 'D':
            if rand <= 10:
                print(self.display())
            elif rand >= 11:
                print(self.dis_elm())
            self.interface()
            return

        elif do == 'Clear All':
            sure = input("Are you sure you wish to clear all data in the list?"
                         "\n>>>").title()
            if sure == "No":
                print("You're lucky I asked you")
            else:
                self.clear_all()
            self.interface()
            return

        elif do == 'Exit':
            print("Bye")
            quit()
            return

        else:
            while do != 'Pre' or do != 'App' or do != 'Rh' or do != 'Re' or do != 'R' or do != 'D' or do != "S" or do != 'Clear All' or do != 'Exit':
                do = input("Sorry, I didn't catch that.."
                           "\nRepeat that for me").title()
                if do == 'Pre':
                    add = input("What value would you like to add to the list?"
                                "\n>>>")
                    self.add_head(add)
                    self.interface()
                    return

                elif do == 'App':
                    add = input("What value would you like to add to the list?"
                                "\n>>>")
                    self.add_end(add)
                    self.interface()
                    return

                elif do == 'Rh':
                    self.rem_front()
                    self.interface()
                    return

                elif do == 'Re':
                    self.rem_end()
                    self.interface()
                    return

                elif do == 'R':
                    remove = input("What value would you like to remove from the list?"
                                   "\n>>>")
                    if rand <= 10:
                        self.remove1(remove)
                    elif rand >= 11:
                        self.remove2(remove)
                    self.interface()
                    return

                elif do == 'S':
                    search = input("What value would you like to search from the list?")
                    if rand <= 10:
                        self.search1(search)
                    elif rand >= 11:
                        self.search2(search)
                    self.interface()
                    return

                elif do == 'D':
                    if rand <= 10:
                        print(self.display())
                    elif rand >= 11:
                        print(self.dis_elm())
                    self.interface()
                    return

                elif do == 'Clear All':
                    sure = input("Are you sure you wish to clear all data in the list?"
                                 "\n>>>").title()
                    if sure == "No":
                        print("You're lucky I asked you")
                    else:
                        self.clear_all()
                    self.interface()
                    return

                elif do == 'Exit':
                    print("Bye")
                    quit()
                    return

#Frances Lee

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'
              .format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        count = 0
        for i in self.cart_items:
            if i.item_name == item_name:
                self.cart_items.remove(i)
                count += 1
        if count == 0:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        count = 0
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].item_quantity = int(item.item_quantity)
                count += 1
        if count == 0:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total_number = 0
        for i in self.cart_items:
            total_number += i.item_quantity
        return total_number

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += (i.item_price * i.item_quantity)
        return total_cost

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print('Number of Items: {}\n'.format(str(self.get_num_items_in_cart())))
        if len(self.cart_items) > 0:
            for i in self.cart_items:
                i.print_item_cost()
        else:
            print('SHOPPING CART IS EMPTY')
        total = self.get_cost_of_cart()
        print('\nTotal: ${}'.format(str(total)))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}\n".format(self.customer_name, self.current_date))
        print('Item Descriptions')
        if len(self.cart_items) > 0:
            for i in self.cart_items:
                i.print_item_description()
        else:
            print('SHOPPING CART IS EMPTY')


def print_menu():
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' descriptions")
    print('o - Output shopping cart')
    print('q - Quit\n')


def execute_menu(option, my_cart):
    if option == 'o':
        print('OUTPUT SHOPPING CART', end='\n')
        my_cart.print_total()
        print()

    elif option == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        my_cart.print_descriptions()
        print()

    elif option == 'a':
        print('ADD ITEM TO CART')
        item_name = input('Enter the item name:\n')
        item_description = input('Enter the item description:\n')
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        new_cart = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        my_cart.add_item(new_cart)
        print()

    elif option == 'r':
        print('REMOVE ITEM FROM CART')
        item_name = input('Enter name of item to remove:\n')
        my_cart.remove_item(item_name)
        print()

    elif option == 'c':
        print('CHANGE ITEM QUANTITY')
        name = input('Enter the item name:\n')
        quantity = int(input('Enter the new quantity:\n'))
        items = ItemToPurchase()
        items.item_name = name
        items.item_quantity = quantity
        my_cart.modify_item(items)
        print()


if __name__ == "__main__":
    customer = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print('\nCustomer name:', customer)
    print("Today's date: {}\n".format(date))
    my_cart = ShoppingCart(customer, date)
    option = ''
    print_menu()
    while option != 'q':
        option = input('Choose an option:\n')
        if option in ['a', 'r', 'c', 'i', 'o']:
            execute_menu(option, my_cart)
            print_menu()

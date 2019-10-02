# Author tjm165

def store_checkout(inventory_tuple_list, item_purchase_list):
    """
    inventory_tuple_list: 
        A list of tuples. Each tuple has a string representing an
        item name, an int representing a price, and a string representing
        a description.

        Example: [("A", 5, "shiny new A"), ("B", 10, "big heavy B")]
    """

    # First, lets put all the inventory items into a name to price dictionary
    inventory_name_to_price = {}
    for item in inventory_tuple_list:
        inventory_name_to_price[item[0]] = item[1]

    """
    item_purchase_list:
        A list of strings. Each string represents an item name.

        Example: ["A", "A", "B", "C"]

    Return the total price of the items in item_purchase_list by using
    prices from the provided inventory_tuple_list. If an item does not
    have a price, it is free. The descriptions are extra, useless
    information for this function.

    The example inputs here would have a total cost of:
    5 + 5 + 10 + 0 = 20 
    """
    # next let's go through the purchase list. 
    # We can use the name to price dicionary to quickly get the prices
    total_price = 0
    for item in item_purchase_list:
        if item in inventory_name_to_price:
            total_price += inventory_name_to_price[item]

    return total_price

def store_checkout_test():
    inventory_tuple_list = [("A", 5, "shiny new A"), ("B", 10, "big heavy B"), ("C", 20, "big heavy B")]
    item_purchase_list = ["A", "A", "B", "C", "D"]

    # expected checkout price is 5 + 5 + 10 + 20 + 0 = 40
    return 40 == store_checkout(inventory_tuple_list, item_purchase_list)

def highest_frequency_count(item_list):
    """
    item_list:
        A list of strings. Each string represents an item name.

        Example: ["A", "A", "B", "C", "A", "B", "B"]



    Find and return a count for the most frequently occurring item
    in item_list.

    In the example, "A" and "B" each appear 3 times, while "C" appears 
    only 1 time. Therefore, expected return value would be 3.
    """

    # let's use an item to frequency dictionary to quickly count all the frequencies
    item_frequency = {}
    for item in item_list:
        if item not in item_frequency:
            item_frequency[item] = 0
        item_frequency[item] = item_frequency[item] + 1

    # finally, let's go through the dictionary and find the highest frequency
    highest_frequency = 0
    for item in item_frequency:
        if item_frequency[item] > highest_frequency:
            highest_frequency = item_frequency[item]
        
    return highest_frequency

def highest_frequency_count_test():
    item_list = ["A", "A", "B", "C", "A", "B", "B", "B", "C", "D"]
    # expected highest frequency is 4
    return 4 == highest_frequency_count(item_list)

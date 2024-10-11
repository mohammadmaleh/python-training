def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(person + " have " + str(coins) + " coins left")
        elif coins == 1:
            print(person + " have " + str(coins) + " coin left")
        else:
            print(person + " have no coins left")

    return play_game


tommy = parent_function("mohammad" ,3)
jenny = parent_function("jenny",  4)
tommy() # mohammad have 3 coins left
tommy() # mohammad have 2 coins left
jenny() # jenny have 4 coins left

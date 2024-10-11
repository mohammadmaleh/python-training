person = "Mohamad"
coins = 3
# print (person + " have " + str(coins) + " coins left")

# older method
message = "%s has %s coins left." % (person, coins)


message_using_format = "{} has {} coins left.".format(person, coins)

player = {"name": "Mohamad", "coins": 3}
dic_message = "{name} has {coins} coins left.".format(**player)


# most modern method
message_new_way = f"{person} has {coins} coins left."

# you can also use operators and functions inside f strings
message_new_way = f"{person.lower()} has {coins * 2} coins left."
message_new_way = f"{player['name'].upper()} has {player['coins']} coins left."

# you can pass options to f strings
message_new_way = f"{person} has 2.5 {2.5 * coins:.2f} coins left."  # here im formatting the coins to have 2 decimals


 
print(message)  # Mohamad has 3 coins left.

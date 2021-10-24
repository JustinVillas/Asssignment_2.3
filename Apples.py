Amount_money = int(input("Amount of money that you have? "))
Price_of_Apple = int(input("What is the price of an apple? "))
maximum_apples = int(Amount_money / Price_of_Apple)
Remaining_money = int(Amount_money - (maximum_apples * Price_of_Apple))
print(
    f"You can buy {maximum_apples} apples and your change is {Remaining_money} pesos.")

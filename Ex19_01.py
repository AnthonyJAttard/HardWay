def buy_apples(amount_of_apples, price_of_apples):
    format_str = "The cost of {:d} apples at {:d} cents each is {:d} cents or {:04.2f} dollars."

    print(format_str.format(amount_of_apples, price_of_apples,
                            amount_of_apples * price_of_apples,
                            (amount_of_apples * price_of_apples) / 100.00))


# 1 Use variables
apples = 20
cost = 5

buy_apples(apples, cost)

# 2 Use values directly
buy_apples(100, 2)

# 3 Use variables and math
buy_apples(apples * 3, cost * 3)

# 4 Get input for data
buy_apples(int(input("How many apples? ")), int(input("Cents per apple? ")))

# 5 Use values and math directly
buy_apples(12 * 2, 12 - 4)

# 6 Combine input and math
buy_apples(int(input("How many apples? ")) * 80, int(input("Cents per apple? ")) - 5)

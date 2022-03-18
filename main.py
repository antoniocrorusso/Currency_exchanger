import currency_converter as cc

run = True

while run:
    print("""This is the currency exchange program.
Please, select a option bellow:
1 - Convert from Brazilian Real
2 - Convert to Brazilian Real
3 - Exit""")

    first_choice = int(input("Option: "))

    while first_choice != 1 and first_choice != 2 and first_choice != 3:
        print("Type only the numbers of the Menu")
        first_choice = int(input("1 - Convert FROM Brazilian Real\n2 - Convert TO Brazilian Real\n3 - Exit\nOption: "))

    if first_choice == 1 or first_choice == 2:
        print("""Now choose the other currency:
1 - Euro
2 - Dollar
3 - Pound
4 - Exit""")
        currency_choice = int(input("Option: "))

        while currency_choice != 1 and currency_choice != 2 and currency_choice != 3 and currency_choice != 4:
            print("Type only the numbers of the Menu.")
            first_choice = int(input("1 - Euro\n2 - Dollar\n3 - Pound\n4 - Exit\nOption: "))

        if currency_choice == 1:
            tag = "eur-brl"

        elif currency_choice == 2:
            tag = "usd-brl"

        elif currency_choice == 3:
            tag = "gbp-brl"
        else:
            cc.exit_program()

        if first_choice == 1:
            print("Now type the value in Reais. The number must be different than 0.\nUse '.' for decimals.")
            user_value = float(input("Value: "))
            while user_value <= 0:
                print(f"Wrong Input. The number must be different than 0 or negative.\nUse '.' for decimals.")
                user_value = float(input("Value: "))

            rate = cc.get_current_rate(tag)
            to_real = 1/rate
            value = user_value * to_real
            print(f"The value is {value:.2f} {tag[:3]}")
            run = cc.run_again()
        else:
            print(f"Now type the value in {tag[:3]}. The number must be different than 0.\nUse '.' for decimals.")
            user_value = float(input("Value: "))
            while user_value <= 0:
                print(f"Wrong Input. The number must be different than 0 or negative.\nUse '.' for decimals.")
                user_value = float(input("Value: "))
            rate = cc.get_current_rate(tag)
            value = user_value * rate
            print(f"The value is {value:.2f} reais")
            run = cc.run_again()

    else:
        cc.exit_program()

import random 
print("Welcome to our Bank")
balance = 10
while True:
    pin = int(input("\nEnter your Password: "))

    while pin < 1000 or pin > 9999:
        pin = int(input("\nInvalid Pin.. Re-enter your Pin please: "))

    while True:
        print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit ")
        selection = int(input("\nEnter your selection: " + " "))
        # View Balance
        if selection == 1:
            print("\nYour Balance is: " +  str(balance)+ " ")
        # Withdraw
        elif selection == 2:
            print("\nYour Balance is: " +  str(balance)+ " ")
            withDraw = float(input("\nPlease Enter amount to withdraw: "))

            if withDraw > balance:
                print("\nYou're balance is less than withdrawl amount: " + str(balance) + " \n")
                print("Please make a deposit.\n")
            else:
                print("\nYour Balance was: " +  str(balance) + " ")
                balance -= withDraw
                print("\nUpdated Balance: " + str(balance) + " \n")
        # Deposit
        elif selection == 3:
            print("\nYour Balance is: " +  str(balance)+ " ")
            depo = float(input("\nEnter amount to deposit: "))
            print("\nYour Balance was: " +  str(balance) + " ")
            balance += depo
            print("\nUpdated Balance: " + str(balance) + " \n")
        # QUIT
        elif selection == 4:
            check = input("\nAre you sure you want to quit?, Yes, or No: ")
            if check == "Yes":
                print("\nYour Transaction is complete")
                print("\nTransaction number: ", random.randint
                        (10000, 1000000))
                print("\nThanks for choosing us as your bank\n")
                break
            else:
                print("\nReturn to main list")
                continue
        
    break

# Made by AIET CE department:
#     3- Adham Ahmed Kotp
#     24- Mohammed Hesham 
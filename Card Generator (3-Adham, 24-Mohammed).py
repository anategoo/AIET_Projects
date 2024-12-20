import random 
import re
# lists for storing card numbers and to check if the card number does exist
Orange_card_list=[]
Vodafone_card_list=[]
Etisalat_card_list=[]
# lists for storing recharged card to ensure we won't use it agian
Recharged_Orange_card_list=[]
Recharged_Vodafone_card_list=[]
Recharged_Etisalat_card_list=[]

# main function to execute the code
def main():
    while True:
        # check if the user want a new card or want to recharge his own card
        Service_choice = input("1-Order new card \t 2-Recharge your card \t 3-Quit \n")
        # calling function to generate card number
        if Service_choice == '1':
            card_generator()
        # calling function to recharge the card for user
        elif Service_choice == '2':
            card_recharge()
        # ending 
        elif Service_choice == '3':
            return
        
        else : print("Please choose between 1 or 2 \n")

# function to generate cards number according to user requirement
def card_generator():
    while True:
        # asking user to choose company
        Company_choice = input("1-Orange \t 2-Vodafone \t 3-Etisalat \t 4-return \n")
        # generate orange card
        if Company_choice == '1':
            while True:
                # asking user to choose card value and print it for the suer
                print("Enter the value of your card")
                Card_category_choice = input("1-25 \t 2-50 \t 3-75 \t 4-return\n")
                # 25EG orange card
                if Card_category_choice == '1':
                    generate_card = random.randint(2500000000000000, 2599999999999999)
                    new_card = generate_card
                    Orange_card_list.append(new_card)
                    print(f'Your Orange 25EG card is {new_card}')
                    return
                # 50EG orange card
                elif Card_category_choice == '2':
                    generate_card = random.randint(5000000000000000, 5099999999999999)
                    new_card = generate_card
                    Orange_card_list.append(new_card)
                    print(f'Your Orange 50EG card is {new_card}')
                    return
                # 75EG orange card
                elif Card_category_choice == '3':
                    generate_card = random.randint(7500000000000000, 7599999999999999)
                    new_card = generate_card
                    Orange_card_list.append(new_card)
                    print(f'Your Orange 75EG card is {new_card}')
                    return
                # return to prevoius menu
                elif Card_category_choice == '4':
                    break
                # when user choose wronge choice
                else : print("Please choose between 1, 2 , 3 or 4")

        # generate Vodafone card
        elif Company_choice == '2':
            while True:
                print("Enter the value of your card")
                Card_category_choice = input("1-25 \t 2-50 \t 3-75 \t 4-return\n")
                if Card_category_choice == '1':
                    generate_card = random.randint(2500000000000000, 2599999999999999)
                    new_card = generate_card
                    Vodafone_card_list.append(new_card)
                    print(f'Your Vodafone 25EG card is {new_card}')
                    return
                elif Card_category_choice == '2':
                    generate_card = random.randint(5000000000000000, 5099999999999999)
                    new_card = generate_card
                    Vodafone_card_list.append(new_card)
                    print(f'Your Vodafone 50EG card is {new_card}')
                    return
                elif Card_category_choice == '3':
                    generate_card = random.randint(7500000000000000, 7599999999999999)
                    new_card = generate_card
                    Vodafone_card_list.append(new_card)
                    print(f'Your Vodafone 75EG card is {new_card}')
                    return
                elif Card_category_choice == '4':
                    break
                else : print("Please choose between 1, 2 , 3 or 4")

        # generate Etisalat card
        elif Company_choice == '3':
            while True:
                print("Enter the value of your card")
                Card_category_choice = input("1-25 \t 2-50 \t 3-75 \t 4-return\n")
                if Card_category_choice == '1':
                    generate_card = random.randint(2500000000000000, 2599999999999999)
                    new_card = generate_card
                    Etisalat_card_list.append(new_card)
                    print(f'Your Etisalat 25EG card is {new_card}')
                    return
                elif Card_category_choice == '2':
                    generate_card = random.randint(5000000000000000, 5099999999999999)
                    new_card = generate_card
                    Etisalat_card_list.append(new_card)
                    print(f'Your Etisalat 50EG card is {new_card}')
                    return
                elif Card_category_choice == '3':
                    generate_card = random.randint(7500000000000000, 7599999999999999)
                    new_card = generate_card
                    Etisalat_card_list.append(new_card)
                    print(f'Your Etisalat 75EG card is {new_card}')
                    return
                elif Card_category_choice == '4':
                    break
                else : print("Please choose between 1, 2 , 3 or 4")

        # return to main function
        elif Company_choice == '4': return

        else: print("Please choose between 1, 2 or 3")

# function to recharge the card and verify the validity of the card
def card_recharge():
    card_input = ''
    # regular exp to check if the card valid or not
    pattern = r"#10[345]\*\d{16}#"
    while True:
        card_input = input("Enter your card please \n")
        # check the card is valid or not
        if not re.fullmatch(pattern, card_input):
            print("please enter your card number in this way #105* you card with 16 digits # \n")
        # check if the card has already recharged or not
        elif int(card_input[5:-1]) in Recharged_Orange_card_list or \
        int(card_input[5:-1]) in Recharged_Etisalat_card_list or \
        int(card_input[5:-1]) in Recharged_Vodafone_card_list: 
            print("This card already recharged")
            return
        else : break

    # recharge the card for user and storing this card as a recharged one
    if card_input[0:5] == '#105*' and int(card_input[5:-1]) in Orange_card_list:
        print(f"Thank you for using orange {card_input[5:7]} card")
        Recharged_Orange_card_list.append(int(card_input[5:-1]))
    elif card_input[0:5] == '#104*' and int(card_input[5:-1]) in Vodafone_card_list:
        print(f"Thank you for using Vodafone {card_input[5:7]} card")
        Recharged_Vodafone_card_list.append(int(card_input[5:-1]))
    elif card_input[0:5] == '#103*' and int(card_input[5:-1]) in Etisalat_card_list:
        print(f"Thank you for using Etisalat {card_input[5:7]} card")
        Recharged_Etisalat_card_list.append(int(card_input[5:-1]))
    else: print("your card doesn't exist")

main()
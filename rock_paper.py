import random
#from platform import machine

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# #getting user choice input
# #0(Rock) Beat 2(Scissors)  2 > 0/ 0 < 2
# #1(Paper) Beat 0(Rock) 1 > 0 / 0 < 1
# #2(Scissors) Beat 1(Paper) 2 > 1 / 1 < 2
# #DRAW  user_choice == machine_choice

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# machine_choice = random.randint(0, 2)
#
# if user_choice > 2 or user_choice < 0:
#     print(user_choice)
#     print("Wrong input, Try again Please!")
# if user_choice <= 2 and user_choice >= 0:
#     signs = [rock, paper, scissors]
#     if user_choice == 0 and machine_choice == 2:
#         print(f"You chose: ___{user_choice}__")
#         print(signs[user_choice])
#         print(f"Machine chose: ___{machine_choice}__")
#         print(signs[machine_choice])
#         print("You win!")
#     elif machine_choice == 0 and user_choice == 2:
#         print(f"You chose: ___{user_choice}__")
#         print(signs[user_choice])
#         print(f"Machine chose: ___{machine_choice}__")
#         print(signs[machine_choice])
#         print("You Lose!")
#     elif user_choice > machine_choice:
#         print(f"You chose: ___{user_choice}__")
#         print(signs[user_choice])
#         print(f"Machine chose: ___{machine_choice}__")
#         print(signs[machine_choice])
#         print("You Win!")
#     elif machine_choice > user_choice:
#         print(f"You chose: ___{user_choice}__")
#         print(signs[user_choice])
#         print(f"Machine chose: ___{machine_choice}__")
#         print(signs[machine_choice])
#         print("You lose!")
#     elif user_choice == machine_choice:
#         print("It's a Draw")


play_rounds = int(input("How many rounds do you want to play between \"3 rounds\" & \"5 rounds\",\n"
                    "       in order to win the \"Rock-Paper-Scissors Game\".\n"
                    "         _________________________________________\n"
                    "         Choose \"1 for 3 rounds\" or \"2 for 5 rounds\":    \n"))
if play_rounds == 1:
    print("You going to play 3 rounds!")
    for rounds in range(1, 4):
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        machine_choice = random.randint(0, 2)
        if user_choice > 2 or user_choice < 0:
            print(user_choice)
            print("Wrong input, Try again Please!")
        if user_choice <= 2 and user_choice >= 0:
            signs = [rock, paper, scissors]
            # test = 0
            if user_choice == 0 and machine_choice == 2:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You win!"
                print(str(final))
                # test = final
            elif machine_choice == 0 and user_choice == 2:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You Lose!"
                print(str(final))
                # test = final
            elif user_choice > machine_choice:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You Win!"
                print(str(final))
            elif machine_choice > user_choice:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You lose!"
                print(str(final))
            elif user_choice == machine_choice:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "It's a Draw"
                print(str(final))
            if final == "You Win!":
                if user_choice == 0 and machine_choice == 2 or user_choice > machine_choice:
                    print("Final Win")
                else:
                    print("Final Win")
            elif final == "You lose!":
                if machine_choice == 0 and user_choice == 2 or machine_choice > user_choice:
                    print("Great lose")
                else:
                    print("Great lose")
            elif final == "It's a Draw":
                if user_choice == machine_choice:
                    print("Final Draw!")
            # else:
            #     print("Error Occured!")
            # win_add_value = 0
            # counter = 1
            # win_add_value += counter
            # win_add_value = []
            # for var_count in 1,2,3:
            #     holder = var_count
            #     win_add_value.append(holder)
            # print(win_add_value)
                # elif final == "You lose!":
                #     lose_add_value = []
                #     for var_count in range(1, 4):
                #         holder = var_count
                #         lose_add_value.append(holder)
                #     print(lose_add_value)
#Going for 5 rounds if the choice was 2
elif play_rounds == 2:
    print("You going to play 5 rounds!")
    for rounds in range(1, 6):
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        machine_choice = random.randint(0, 2)

        if user_choice > 2 or user_choice < 0:
            print(user_choice)
            print("Wrong input, Try again Please!")
        if user_choice <= 2 and user_choice >= 0:
            signs = [rock, paper, scissors]
            if user_choice == 0 and machine_choice == 2:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You win!"
                print(final)
            elif machine_choice == 0 and user_choice == 2:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You Lose!"
                print(final)
            elif user_choice > machine_choice:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You Win!"
                print(final)
            elif machine_choice > user_choice:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "You lose!"
                print(final)
            elif user_choice == machine_choice:
                print(f"You chose: ___{user_choice}__")
                print(signs[user_choice])
                print(f"Machine chose: ___{machine_choice}__")
                print(signs[machine_choice])
                final = "It's a Draw"
                print(final)
else:
    print("Wrong input. Try again please!")

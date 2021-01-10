# # # # # # # # Define the validate function
# # # # # # # def validate(hand):
# # # # # # #     if hand < 0 or hand > 2:
# # # # # # #         return False
# # # # # # #     else:
# # # # # # #         return True
# # # # # # #
# # # # # # #     # Add control flow based on the value hand
# # # # # # #
# # # # # # #
# # # # # # # def print_hand(hand, name='Guest'):
# # # # # # #     hands = ['Rock', 'Paper', 'Scissors']
# # # # # # #     print(name + ' picked: ' + hands[hand])
# # # # # # #     if validate(player_hand):
# # # # # # #         print_hand(player_name, str(player_hand))
# # # # # # #     else:
# # # # # # #         return False
# # # # # # #
# # # # # # #
# # # # # # # print('Starting the Rock Paper Scissors game!')
# # # # # # # player_name = input('Please enter your name: ')
# # # # # # #
# # # # # # # print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
# # # # # # # player_hand = int(input('Please enter a number (0-2): '))
# # # # # # #
# # # # # # # # Add control flow based on the return value of the validate function
# # # # # # #
# # # # # # # print_hand(player_hand, player_name)
# # # # # #
# # # # # #
# # # # # # # Define the validate function
# # # # # # def validate(hand):
# # # # # #
# # # # # #     if hand < 0 or hand > 2:
# # # # # #         return False
# # # # # #     else:
# # # # # #         return True
# # # # # #
# # # # # #
# # # # # # def print_hand(hand, name):
# # # # # #     hands = ['Rock', 'Paper', 'Scissors']
# # # # # #     print(name + ' picked: ' + hands[hand])
# # # # # #
# # # # # #
# # # # # # print('Starting the Rock Paper Scissors game!')
# # # # # # player_name = input('Please enter your name: ')
# # # # # #
# # # # # # print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
# # # # # # player_hand = int(input('Please enter a number (0-2): '))
# # # # # #
# # # # # # if validate(player_hand):
# # # # # #     print_hand(player_hand, player_name)
# # # # # # else:
# # # # # #     print('Please enter a valid number')
# # # # #
# # # # #
# # # # # def validate(hand):
# # # # #     if hand < 0 or hand > 2:
# # # # #         return False
# # # # #     return True
# # # # #
# # # # #
# # # # # def print_hand(hand, name='Guest'):
# # # # #     hands = ['Rock', 'Paper', 'Scissors']
# # # # #     print(name + ' picked: ' + hands[hand])
# # # # #
# # # # #
# # # # # # Define the judge function
# # # # # def judge(player, computer):
# # # # #     if player == computer:
# # # # #         return "Draw"
# # # # #     # Add control flow based on the comparison of player and computer
# # # # #     elif player == 0 and computer == 1:
# # # # #
# # # # #
# # # # #         return "Lose"
# # # # #
# # # # #
# # # # # print('Starting the Rock Paper Scissors game!')
# # # # # player_name = input('Please enter your name: ')
# # # # #
# # # # # print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
# # # # # player_hand = int(input('Please enter a number (0-2): '))
# # # # #
# # # # # if validate(player_hand):
# # # # #     computer_hand = 1
# # # # #
# # # # #     print_hand(player_hand, player_name)
# # # # #     print_hand(computer_hand, 'Computer')
# # # # #
# # # # #     # Assign the return value of judge to the result variable
# # # # #
# # # # #     # Print the result variable
# # # # #
# # # # # else:
# # # # #     print('Please enter a valid number')
# # # # def validate(hand):
# # # #     if hand < 0 or hand > 2:
# # # #         return False
# # # #     return True
# # # #
# # # #
# # # # def print_hand(hand, name='Guest'):
# # # #     hands = ['Rock', 'Paper', 'Scissors']
# # # #     print(name + ' picked: ' + hands[hand])
# # # #
# # # #
# # # # # Define the judge function
# # # # def judge(player, computer):
# # # #     if player == computer:
# # # #         return "Draw"
# # # #     # Add control flow based on the comparison of player and computer
# # # #     elif player ==0 and computer== 1:
# # # #         return "Lose"
# # # #
# # # #     elif player== 1 and computer == 2:
# # # #         return "Lose"
# # # #     elif player == 2 and computer == 0:
# # # #         return "Lose"
# # # #     else:
# # # #         return "win"
# # # #
# # # #
# # # # print('Starting the Rock Paper Scissors game!')
# # # # player_name = input('Please enter your name: ')
# # # #
# # # # print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
# # # # player_hand = int(input('Please enter a number (0-2): '))
# # # #
# # # # if validate(player_hand):
# # # #     computer_hand = 1
# # # #     print_hand(player_hand, player_name)
# # # #     print_hand(computer_hand, 'Computer')
# # # #     # Assign the return value of judge to the result variable
# # # #     # Print the result variable
# # # # else:
# # # #     print('Please enter a valid number')
# # # # result =judge(player_hand,computer_hand)
# # # # print(result)
# # #
# # #
# # #
# # class MenuItem:
# #     pass
# #
# #
# # menu_item1 = MenuItem()
# #
# # menu_item1.name = 'Sandwich'
# # print(menu_item1.name)
# #
# # menu_item1.price = 5
# # print(menu_item1.price)
# #
# # # Create an instance of the MenuItem class
# # menu_item2 = MenuItem()
# #
# # # Set the name of menu_item2 to 'Chocolate Cake'
# # menu_item2.name = "Chocolate Cake"
# #
# # # Output the name of menu_item2
# # print(menu_item2.name)
# #
# # # Set the price of menu_item2 to 4
# #
# #
# # # Output the price of menu_item2a
# #
# class MenuItem:
#
#     def info(self):
#         print(self.name,': $', str(self.price))
#         # Output in the format '____: $____'
#
#         menu_item1 = MenuItem()
#         menu_item1.name = 'Sandwich'
#         menu_item1.price = 5
#
#         menu_item1.info()
#
#         menu_item2 = MenuItem()
#         menu_item2.name = 'Chocolate Cake'
#         menu_item2.price = 4
#
#         print(menu_item2.info())
#
#


class MenuItem:
    def info(self):
        return self.name + ': $' + str(self.price)

    # Define the get_total_price method
    def get_total_price(self,count):
        total_price = count * self.price
        return total_price
        return 'Your total is $' + str(result)


menu_item1 = MenuItem()
menu_item1.name = 'Sandwich'
menu_item1.price = 5
result = get_total_price(4)
print(menu_item1.info())

# Call the get_total_price method


# Output 'Your total is $____'


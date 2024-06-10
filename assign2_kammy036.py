#
# File: assign2_kammy036.py
# Author: Max Kamp
# Email Id: kammy036@mymail.unisa.edu.au
# Description: Assignment 2 – this is my blackjack game :)
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import blackjack

def read_file(filename):

    player_list = []
    with open(filename, "r") as infile:

        # Read first line of file.
        line = infile.readline()

        # While not end of file reached i.e. empty string not returned from readline method.
        while line != '':
            # Read name
            name = line.strip('\n')
            # Read in next line
            line = infile.readline()
            # Split line into games played, no won, no lost, etc
            info_list = line.split()
            games_played = int(info_list[0])
            no_won = int(info_list[1])
            no_lost = int(info_list[2])
            no_drawn = int(info_list[3])
            chips = int(info_list[4])
            total_score = int(info_list[5])
            # Create new player list with player info
            new_player = [name, games_played, no_won, no_lost, no_drawn, chips, total_score]
            # Add new player to player_list list
            player_list.append(new_player)
            # Read next line of file.
            line = infile.readline()

    return player_list

# Function display_players()
def display_players(player_list):

    #printing the player summary table and making the layour fit the requirment
    print("In function display_players()")

    print("="*59)    
    print("-                     Player Summary                      -")
    print("="*59)   
    print("-                             P  W  L  D   Chips   Score  -")
    print("-"*59)    

    #adding each players stats and name followed by more layout lines and and ending border line
    for player in player_list:
        name = player[0]
        p, w, l, d, chips, score = player[1:]
        print(f"-  {name:<25} {p:>2} {w:>2} {l:>2} {d:>2} {chips:>8} {score:>4}  -")
        print("-"*59)
    print("="*59,"\n")


def write_to_file(filename, player_list):
    #write to file function where the player info is stored 
    with open(filename, "w") as outfile:
        for player in player_list:
            name = player[0]
            games_played, no_won, no_lost, no_drawn, chips, total_score = player[1:]
            outfile.write(f"{name}\n")
            outfile.write(f"{games_played} {no_won} {no_lost} {no_drawn} {chips} {total_score}\n")    

def update_players(player_list, player_name, no_chips, game_result):

    #this function is to update each players stats each time they change 
    updated = "N"
    #itterating through all of the players in the list and updadting the stats
    for player in player_list:

        #adding player games played  if the player names match
        if player[0] == player_name:
            player[1] += 1
            #if the player wins the game they get a win and 3 points added 
            if game_result == 3:
                player[2] += 1
                player[6] += 3
            #a draw is adde and the player gets 1 point
            elif game_result == 1:
                player[4] += 1
                player[6] += 1
            
            #if the player looses, a loss is added and then the player has their chips stats updated ans they would have lost or gained some
            else:
                player[3] += 1
            player[5] = no_chips
            
            #ensuring the players are updated
            updated = 'Y'
    if updated != "Y":
        print("error message from update_players")
    
#function to find player in the player_list
def find_player(player_list, name):
    for index in range(len(player_list)):
        if player_list[index][0] == name:
            return index
    return "unfound"

def add_player(player_list): #function to add a new plaer to the list of players 

    player_name = input("\nEnter new player's name: ")

    if find_player(player_list, player_name) != "unfound":
        print(f"Player {player_name} already exists")
        return
    
    #initialising all of the players new stats
    games_played = 0
    no_won = 0
    no_lost = 0
    no_drawn = 0
    chips = 100
    total_score = 0 

    new_player = [player_name, games_played, no_won, no_lost, no_drawn, chips, total_score]

    player_list.append(new_player)
    print(f"\nSuccessfully added {player_name} to player list.\n")

#function to add chips to theplayers balance
def buy_player_chips(player_list):
    player_name = input("Please enter name: ") #asking for a name
    player_find = find_player(player_list, player_name) # finding teh player using a func
    invalid_value = True
    invalid_name = True

    while invalid_name == True:
        
        #if the player name is unfound ask for the name again
        if player_find == "unfound":
            print(f"\n{player_name} is not found in player list.\n")
            invalid_name = True
            player_name = input("Please enter name: ")
        
        #if the player is not unfound show how many chiops they have and ask how many more they want to buy then add them and update the name status
        elif player_find != "unfound":
            print(f"\n{player_list[player_find][0]} currently has {player_list[player_find][5]} chips\n")
            amount_add = int(input("How many chips would you like to buy?: "))
            invalid_name = False

            #check for an invalid value that the user inputs
            while invalid_value == True:
                if amount_add > 0 and amount_add <= 100:
                    player_list[player_find][5] += amount_add
                    print(f"\nSuccessfully updated {player_list[player_find][0]}'s chip balance to {player_list[player_find][5]}\n")
                    invalid_value = False
                else:
                    print("You may only buy between 1-100 chips at a time!\n")
                    amount_add = int(input("How many chips would you like to buy?: "))
                    
def remove_player(player_list, name): #func to remove a player from the player lists
    player_find = find_player(player_list,name)
    if player_find == "unfound":
        print(f"{name} is not found in players.")
    else:
        #if the player the user is asking fro is found, delete that element in the list
        del player_list[player_find]
        print(f"\nSuccessfully removed {name} from player list.\n")
    return player_list

def display_highest_chip_holder(player_list): #function to display the user with the highest chip balance
    #checking if the list is empty
    if not player_list:
        print("no players in the list")
        return

    Player_with_most_chips = None

    #itterating over the players in player_list and is they have more then the comparison or have the same ammount with less games set them to the highest temperarily until all players have been checked
    for player in player_list:
        if Player_with_most_chips is None or player[5] > Player_with_most_chips[5] or (player[5] == Player_with_most_chips and player[1] < Player_with_most_chips[1]):
            Player_with_most_chips = player

    #if the most chips found was 0 display a message
    if Player_with_most_chips[5] == 0:
         print("No player with a highest chip balance (all players have a balance of 0 chips)")
    else:
        print(f"\nHighest Chip Holder => {Player_with_most_chips[0]} with {Player_with_most_chips[5]}\n")

# play_blackjack_games allows a user to continue playing games until the user is finished
def play_blackjack_games(player_list, player_pos):
    player = player_list[player_pos]
    player_name = player[0]
    no_chips = player[5]
    keep_gaming = True

    while keep_gaming == True:
        print(f"Starting a new game for {player_name}. current chips: {no_chips}")
        game_result, no_chips = blackjack.play_one_game(no_chips) 

        #incrementing game results and stats
        player[1] += 1
        if game_result == 3:
            player[2] += 1
            player[6] += 3
        elif game_result == 1:
            player[4] += 1
            player[6] += 1
        else:
            player[3] += 1
        player[5] = no_chips

        #asking if they want to play again
        play_again = input("Play again [y|n]?: ").strip().lower()
        if play_again == "y":
            keep_gaming = True
        else:
            keep_gaming = False
            
#using a bubble sort to sort the players in the list so that they can be displayed in decending order
def sort_by_chips(player_list):
    #creating a new list and gets the infomatuion in the list of lists
    sorted_list = [player[:] for player in player_list]

    n = len(sorted_list)
    for i in range(n):

        # this loops through from the start to the end of the unsorted section to determine
        for j in range(0,n-i-1):

            #this if statments asks if and element of chips is greater then the other or if they're the same ammount of chips but pne has more games played
            if sorted_list[j][5] < sorted_list[j+1][5] or (sorted_list[j][5] == sorted_list[j+1][5] and sorted_list[j][1] > sorted_list[j+1][1]):
                
                # this creates a tuple of the twi eklements on the right hand side and the left side shows where the elements should be in respect to the number of chips.
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    return sorted_list


def main():

    #getting the file to read and displaying them using a function
    filename = "players.txt"
    new_filename = "new_players.txt"
    player_list= read_file(filename)
    display_players(player_list)

    #setting the avalible game options
    game_options_list = ["list", "buy", "search", "high", "add", 'remove', "play", "chips", "quit"]

    while True:
        choice = input("Please enter choice\n[list, buy, search, high, add, remove, play, chips, quit]:").strip().lower()

        #validating user input
        if choice not in game_options_list:
            print('Not a valid command - please try again.')
        else:
            #all elif statements are what happens when the user prompts to choose that list option
            if choice == "quit": #quitting the game
                write_to_file(new_filename, player_list)
                print("Quitting the program.")
                print("\n\n-- Program terminating--\n\n")
                return
            elif choice == "list":#displaying the player list
                display_players(player_list)

            elif choice == "buy":#buying/adding more chips to the players 
                buy_player_chips(player_list)

            elif choice == "search": #searching for a player
                print("search\n")
                player_name = input("Please enter name: ")
                player_find = find_player(player_list, player_name)
                if player_find != "unfound":
                    player = player_list[player_find]
                    print(f"\n{player_name} stats:\n")
                    print(f"P   W   L   D   Score")
                    print(f"{player[1]:<3} {player[2]:<3} {player[3]:<3} {player[4]:<3} {player[6]:<5}\n")
                    print(f"Chips: {player[5]}\n")
                else:
                    print(f"Player {player_name} not found")

            elif choice == "high":#getting the player with the highest chip balance
                display_highest_chip_holder(player_list)

            elif choice == "add":#adding a player to the list of players
                add_player(player_list)

            elif choice == "remove":#removing a player in the list of players
                name = input("Please enter name: ")
                remove_player(player_list,name)

            elif choice == "chips":#displaying in decending order teh players and their chip balance
                print("in chips command")
                sorted_list = sort_by_chips(player_list)

                print("Sorted in decending order")

                print("="*59)    
                print("-                     Player Summary                      -")
                print("="*59)   
                print("-                             P  W  L  D   Chips   Score  -")
                print("-"*59)    


                for player in sorted_list:
                    name = player[0]
                    p, w, l, d, chips, score = player[1:]
                    print(f"-  {name:<25} {p:>2} {w:>2} {l:>2} {d:>2} {chips:>8} {score:>4}  -")
                    print("-"*59)
                print("="*59)
            
            #playing the game
            elif choice == "play":
                player_name = input("Enter player's name:")
                player_find = find_player(player_list, player_name)
                
                if player_find != "unfound":

                    play_blackjack_games(player_list, player_find)

                else:
                    print(f"Player {player_name} not found")        

main()



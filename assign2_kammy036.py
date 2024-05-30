#
# File: assign2_kammy036.py
# Author: Max Kamp
# Email Id: kammy036@mymail.unisa.edu.au
# Description: Assignment 2 – place assignment description here…
# This is my own work as defined by the University's
# Academic Misconduct policy.
#


import blackjack

# Function read_file() - place your own comments here...  : )
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
    
    print("In function display_players()")

    print("="*59)    
    print("-                     Player Summary                      -")
    print("="*59)   
    print("-                             P  W  L  D   Chips   Score  -")
    print("-"*59)    


    for player in player_list:
        name = player[0]
        p, w, l, d, chips, score = player[1:]
        print(f"-  {name:<25} {p:>2} {w:>2} {l:>2} {d:>2} {chips:>8} {score:>4}  -")
        print("-"*59)
    print("="*59)

def write_to_file(filename, player_list):
    
    with open(filename, "w") as outfile:
        for player in player_list:
            name = player[0]
            games_played, no_won, no_lost, no_drawn, chips, total_score = player[1:]
            outfile.write(f"{name}\n")
            outfile.write(f"{games_played} {no_won} {no_lost} {no_drawn} {chips} {total_score}\n")
    #return("hello from write_to_file")
    
    ### Place the rest of your function definitions here...  : )

def update_players(player_list, player_name, no_chips, game_result):
    updated = "N"
    for player in player_list:
        if player[0] == player_name:
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
            
            updated = 'Y'
    if updated != "Y":
        print("error message from update_players")
        
def find_player(player_list, name):
    for index in range(len(player_list)):
        if player_list[index][0] == name:
            return index
    return "unfound"

def add_player(player_list):

    player_name = input("Enter new player's name: ")

    if find_player(player_list, player_name) != "unfound":
        print(f"Player {player_name} already exists")
        return
    
    games_played = 0
    no_won = 0
    no_lost = 0
    no_drawn = 0
    chips = 100
    total_score = 0 

    new_player = [player_name, games_played, no_won, no_lost, no_drawn, chips, total_score]

    player_list.append(new_player)
    print(f"Successfully added {player_name} to player list.")

def buy_player_chips(player_list):
    player_name = input("Please enter name: ")
    player_find = find_player(player_list, player_name)
    invalid_value = True
    invalid_name = True

    while invalid_name == True:

        if player_find == "unfound":
            print(f"{player_name} is not found in player list.")
            invalid_name = True
            player_name = input("Please enter name: ")

        elif player_find != "unfound":
            print(f"{player_list[player_find][0]} currently has {player_list[player_find][5]} chips\n")
            amount_add = int(input("How many chips would you like to buy?: "))
            invalid_name = False

            while invalid_value == True:
                if amount_add > 0 and amount_add <= 100:
                    player_list[player_find][5] += amount_add
                    print(f"Successfully updated {player_list[player_find][0]}'s chip balance to {player_list[player_find][5]}")
                    invalid_value = False
                else:
                    print("You may only buy between 1-100 chips at a time!")
                    amount_add = int(input("How many chips would you like to buy?: "))
                    
def remove_player(player_list, name):
    player_find = find_player(player_list,name)
    if player_find == "unfound":
        print(f"{name} is not found in players.")
    else:
        del player_list[player_find]
        print(f"\nSuccessfully removed {name} from player list.\n\n")
    return player_list

def display_highest_chip_holder(player_list):
    if not player_list:
        print("no players in the list")
        return

    Player_with_most_chips = None

    for player in player_list:
        if Player_with_most_chips is None or player[5] > Player_with_most_chips[5] or (player[5] == Player_with_most_chips and player[1] < Player_with_most_chips[1]):
            Player_with_most_chips = player

    if Player_with_most_chips[5] == 0:
         print("No player with a highest chip balance (all players have a balance of 0 chips)")
    else:
        print(f"Highest Chip Holder => {Player_with_most_chips[0]} with {Player_with_most_chips[5]}")

    
def play_blackjack_games(player_list, player_pos):
    player = player_list[player_pos]
    player_name = player[0]
    no_chips = player[5]
    keep_gaming = True

    while keep_gaming == True:
        print(f"Starting a new game for {player_name}. current chips: {no_chips}")
        game_result, no_chips = blackjack.play_one_game(no_chips) 

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


        play_again = input("Play again [y|n]?: ").strip().lower()
        if play_again == "y":
            keep_gaming = True
        else:
            keep_gaming = False
            
    



def main():


    filename = "players.txt"
    player_list= read_file(filename)
    display_players(player_list)



    game_options_list = ["list", "buy", "search", "high", "add", 'remove', "play", "chips", "quit"]


    while True:
        choice = input("Please enter choice\n[list, buy, search, high, add, remove, play, chips, quit]").strip().lower()


        if choice not in game_options_list:
            print('Not a valid command - please try again.')
        else:
            
            if choice == "quit":
                write_to_file(filename, player_list)
                print("Quitting the program.")
                print("\n\n-- Program terminating--\n\n")
                return
            elif choice == "list":
                display_players(player_list)


            elif choice == "buy":
                buy_player_chips(player_list)


            elif choice == "search":
                print("in search command")
                player_name = input("Enter player's name to searth: ")
                player_find = find_player(player_list, player_name)
                if player_find != "unfound":
                    player = player_list[player_find]
                    print(f"Player found {player}")
                else:
                    print(f"Player {player_name} not found")



            elif choice == "high":
                display_highest_chip_holder(player_list)


            elif choice == "add":
                add_player(player_list)


            elif choice == "remove":
                name = input("Please enter name: ")
                remove_player(player_list,name)

            elif choice == "chips":
                print("in chips command")
                
            elif choice == "play":
                player_name = input("Enter player's name:")
                player_find = find_player(player_list, player_name)
                
                if player_find != "unfound":

                    play_blackjack_games(player_list, player_find)


                    # player = player_list[player_find]
                    # no_chips = player[5]
                    # game_result, no_chips = blackjack.play_one_game(no_chips)
                    # update_players(player_list, player_name, no_chips, game_result)
    
                else:
                    print(f"Player {player_name} not found")        

main()



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
        print(f"-  {name:<25} {p:>2} {w:>2} {l:>2} {d:>2} {chips:>8} {score:>6}  -")
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
    player_name = input("Enter player name")

    



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
                print("in buy command")


                
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
                print("in high command")
            elif choice == "add":
                add_player(player_list)
            elif choice == "remove":
                print("in remove command")
            elif choice == "chips":
                print("in chips command")

            elif choice == "play":
                player_name = input("Enter player's name:")
                player_find = find_player(player_list, player_name)
                
                if player_find != "unfound":
                    player = player_list[player_find]
                    no_chips = player[5]
                    game_result, no_chips = blackjack.play_one_game(no_chips)
                    update_players(player_list, player_name, no_chips, game_result)
    
                else:
                    print(f"Player {player_name} not found")
                

            

if __name__ == "__main__":
    main()







            ###output_filename = 'new_players.txt'
            ###write_to_file(output_filename, player_list)

            ###new_player_list = read_file(output_filename)
            ###display_players(new_player_list)




            ##blackjack.play_one_game(no_chips)



            # Read player information from file and store in player_list
            #player_list = read_file("players.txt")


            ### you will remove some of the following code as it's been included for development purposes only...  : )

            # Display player list to the screen to ensure read_file is working correctly


            # for player in player_list:
            #     print(player)

            

            # Plays one game of blackJack and assigns the result of the game and the chip balance
            # to variables game_result and no_chips respectively.
            #game_result, no_chips = blackjack.play_one_game(no_chips)

            # Display to the screen the result of play_one_game() – game result (value of 3, 1 or 0)
            # and number of chips remaining.
            #print(game_result, no_chips)




import blackjack
import os



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


# Function display_players() - place your own comments here...  : )
def display_players(player_list):
    
    # This line will eventually be removed - used for development purposes only.
    print("In function display_players()")

    print("="*59)    
    print("-                     Player Summary                      -")
    print("="*59)   
    print("-                             P  W  L  D   Chips   Score  -")
    print("="*59)    


    for player in player_list:
        name = player[0]
        p, w, l, d, chips, score = player[1:]
        print(f"-  {name:<25} {p:>2} {w:>2} {l:>2} {d:>2} {chips:>8} {score:>6}  -")
    print("="*59)

def write_to_file(filename, player_list):
    
    with open(filename, "w") as outfile:
        for player in player_list:
            name = player[0]
            games_played, no_won, no_los, no_drawn, chips, total_score = player[1:]
            outfile.write(f"{name}\n")
            outfile.write(f"{games_played} {no_won} {no_los} {no_drawn} {chips} {total_score}\n")
    return("hello from write_to_file")
    
    ### Place the rest of your function definitions here...  : )




def main():

    ### Define list to store player information
    filename = "players.txt"
    #filename = 'D:/Source/PSP_Assesment/PSP2/players.txt'    
    player_list= read_file(filename)
    display_players(player_list)

    output_filename = 'new_players.txt'
    write_to_file(output_filename, player_list)

    new_player_list = read_file(output_filename)
    display_players(new_player_list)


    player_list = []
    no_chips = 100
    game_result = 0

    blackjack.play_one_game(no_chips)



    # Read player information from file and store in player_list
    player_list = read_file("players.txt")


    ### you will remove some of the following code as it's been included for development purposes only...  : )

    # Display player list to the screen to ensure read_file is working correctly
    for player in player_list:
        print(player)

        
    no_chips = 100
    game_result = 0

    # Plays one game of blackJack and assigns the result of the game and the chip balance
    # to variables game_result and no_chips respectively.
    game_result, no_chips = blackjack.play_one_game(no_chips)

    # Display to the screen the result of play_one_game() – game result (value of 3, 1 or 0)
    # and number of chips remaining.
    print(game_result, no_chips)



    print("\n\n-- Program terminating --\n")

if __name__ == "__main__":
    main()

import datetime
import random

def print_game_interface(welcome_msg):
    message = f"""
                {welcome_msg}
                   1 --> Play
                   2 --> show logs
                   3 --> clear logs
                   4 --> Exit

                 """
    print(message)

def play_user():
    print('[1]: Stone, [2]: Paper, [3]: Scissors')
    player_input = int(input('Type your choice: '))
    while player_input not in (1,2,3):
        print(f'{player_input} is not recognised, choose from the menu')
        player_input = int(input('Type your choice: '))
    return player_input

def play_computer():
    computer_choice = random.choice([1,2,3])
    print(f'comptuer palyed {computer_choice}')
    return computer_choice

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'round ends with draw'
    if user_choice == 1 and computer_choice == 2:
        return 'computer wins'
    if user_choice == 2 and computer_choice == 3:
        return 'computer wins'
    if user_choice == 3 and computer_choice == 1:
        return 'computer wins'
    else:
        return 'user wins'
    
def store_logs(round, user_choice, computer_choice, winner):
    with open('logs_data.txt', 'a') as file:
        file.write(
                ( f'{datetime.datetime.now()},: round: {round}, user choice: {user_choice},' 
                   f' computer choice: {computer_choice} winner: {winner}\n')
                )


def will_continue():
    will_you_continue = input('Would you like to continue game? y/n: ')
    return will_you_continue.lower() == 'y'


def start_game():
    """ To run the game !! """
    while True:
        times_to_play = int(input('How many rounds to play? : '))
        round = 0 
        for times in range (times_to_play):  
            round +=1
            print(f'--------- round {round} start ----------')
            user_choice = play_user()
            computer_choice = play_computer()
            winner = decide_winner(user_choice, computer_choice)
            print(f'--------- round {round} ends ----------')
            print(f'-------- Result is: {winner} ----------')
            store_logs(round, user_choice, computer_choice, winner)
        # print_game_summary()
        if not will_continue():
            main("Welcome back to Stone-Paper-Scissors Game !! ")
            break


def show_logs():
    print('Here is the history logs: ')
    with open('logs_data.txt', 'r') as file:
        for line in file:
            print(line)
    main("Welcome back to Stone-Paper-Scissors Game !! ")

def clear_logs():
    with open('logs_data.txt', 'w') as file:
        pass

    print('logs has been cleared successfully !!')
    main("Welcome back to Stone-Paper-Scissors Game !! ")

def exit_game():
    print('Game Exit.. Good Bye !! ')


def main(welcome_msg="Welcome to Stone-Paper-Scissors Game!"):
    """The entry point to the game:)"""

    print_game_interface(welcome_msg)

    user_input = int(input('Type your choice: '))
    while user_input not in (1,2,3,4):
        print(f'{user_input} is not recognized please choose from the minue: ')
        user_input = int(input('Type your choice: '))

    if user_input ==   1:
        start_game()
    elif user_input == 2:
        show_logs()
    elif user_input ==3:
        clear_logs()
    elif user_input == 4:
        exit_game()


if __name__ == "__main__":
    main()

    
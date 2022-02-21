from random import randint


def get_non_prize_door(host, num_doors, player_choice):
    i = 1
    while (i == host or i == player_choice):
        i = (i + 1) % (num_doors)
    return i


def switch_function(shown_door, num_doors, player_choice):
    i = 1
    while i == shown_door or i == player_choice:
        i = (i + 1) % num_doors
    return i


def monty_hall_game(switch, num_tests):
    win_switch_cnt = 0
    win_no_switch_cnt = 0
    lose_switch_cnt = 0
    lose_no_switch_cnt = 0
    doors = [0, 1, 2]
    num_doors = len(doors)

    for i in range(0, num_tests):
        door_with_prize = randint(0, num_doors - 1)
        host = door_with_prize
        player_choice = randint(0, num_doors - 1)
        original_player_choice = player_choice
        shown_door = get_non_prize_door(host, num_doors, player_choice)
        if switch == True:
            player_choice = switch_function(shown_door, num_doors, player_choice)

        if player_choice == host and switch == False:

            print('Player Wins (No switch) - The player chose door: ', player_choice, ' Original choice: ',
                  original_player_choice, ', Door with prize:', door_with_prize, ', Shown Door: ', shown_door)
            win_no_switch_cnt = win_no_switch_cnt + 1
        elif player_choice == host and switch == True:

            print('Player Wins (switch) - The player chose door: ', player_choice, ' Original choice: ',
                  original_player_choice, ', Door with prize:', door_with_prize, ', Shown Door: ', shown_door)
            win_switch_cnt = win_switch_cnt + 1
        elif player_choice != host and switch == False:

            print('Player Lost (No switch) - The player chose door: ', player_choice, ' Original choice: ',
                  original_player_choice, ', Door with prize:', door_with_prize, ', Shown Door: ', shown_door)
            lose_no_switch_cnt = lose_no_switch_cnt + 1
        elif player_choice != host and switch == True:

            print('Player Lost (switch) - The player chose door: ', player_choice, ' Original choice: ',
                  original_player_choice, ', Door with prize:', door_with_prize, ', Shown Door: ', shown_door)
            lose_switch_cnt = lose_switch_cnt + 1
        else:
            print('SOMETHING IS WRONG')

    return win_no_switch_cnt, win_switch_cnt, lose_no_switch_cnt, lose_switch_cnt, num_tests


x = monty_hall_game(True, 100)
print('Win switch %: ', x[1] / x[4])
print('Lose switch %: ', x[3] / x[4])
print('Win No switch %: ', x[0] / x[4])
print('Lose No switch %: ', x[2] / x[4])

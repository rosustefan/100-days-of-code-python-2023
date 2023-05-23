'''
1. Rock beats scissors and loses to paper. -> OK
2. Scissors beats paper but loses to rock. -> OK
3. Paper beats rock, but loses to scissors. -> OK
4. If both players throw the same object, it’s a tie.

Source: https://www.wikihow.com/Play-Rock,-Paper,-Scissors
'''

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

computer_win = '''
        .--.  .-"     "-.  .--.
       / .. \/  .-. .-.  \/ .. \
      | |  '|  /   Y   \  |'  | |
      | \   \  \ 0 | 0 /  /   / |
       \ '- ,\.-"`` ``"-./, -' /
        `'-' /_   ^ ^   _\ '-'`
        .--'|  \._ _ _./  |'--. 
      /`    \   \.-.  /   /    `\
     /       '._/  |-' _.'       \
    /          ;  /--~'   |       \
   /        .'\|.-\--.     \       \
  /   .'-. /.-.;\  |\|'~'-.|\       \
  \       `-./`|_\_/ `     `\'.      \
   '.      ;     ___)        '.`;    /
     '-.,_ ;     ___)          \/   /
      \   ``'------'\       \   `  /
       '.    \       '.      |   ;/_
     ___>     '.       \_ _ _/   ,  '--.
   .'   '.   .-~~~~~-. /     |--'`~~-.  \
  // / .---'/  .-~~-._/ / / /---..__.'  /
 ((_(_/    /  /      (_(_(_(---.__    .'
           | |     _              `~~`
           | |     \'.
            \ '....' |
             '.,___.'
'''

you_win = '''
  __                                                                                      
  /_/l                                                                                     
 : : :                                                                                     
  ; ; ;                                                                                    
  : : :                                                                                    
   L ; ;  __.-._.-+.                                                                       
  /."^.:.L.' .^-.  \`.                                                                     
 :`.`. \"/\ /.-. `. \ \                                                                    
 ;\ \ ` ;-.y(_.-\  \ `.`.                                                                  
 :   _. ;;  `    \  \. `-\                                                                 
  \ T :: :=,   ,=^\  \"-._;          __..------.._                                         
  /;:-'; ; `._L.--^.     .-""-.`.   \     ""--..                                   
 : :_.': :           ;/     \   /      \ \   ;          ""--._                             
 ;  T   \ \  s      /:.---.  ;_/    `-._; ;  :     ______    \"-.      ___                 
:   :\   \ `.-=^" .:-"    _\   \_.      : :  _:.--".-"  .T"---:-.""--""\  ""-.             
;    \\   "-.\__.:'      /-'. ; ;    _. ; ;  /   -'    '    .- \        ;     "-._.-"""""-,
:     ;\     `..'      .'    \: ;      / / .'               )   ;  __  /         T        :
 ;      `,     \    .-"       ;/"---" /.' /                 `- /"""  ""---""""----..___..-'
 :    .-" `.      .'.-\      / ""----""""^-.._              .-"  Lara                       
  \_.'      "._.-"-..-'`-..-'                 ""--..__..--""
'''

tie_match = '''
       .-.,     ,.-.
 '-.  /:::\\   //:::\  .-'
 '-.\|':':' `"` ':':'|/.-'
 `-./`. .-=-. .-=-. .`\.-`
   /=- /     |     \ -=\
  ;   |      |      |   ;
  |=-.|______|______|.-=|
  |==  \  0 /_\ 0  /  ==|
  |=   /'---( )---'\   =|
   \   \:   .'.   :/   /
    `\= '--`   `--' =/'
      `-=._     _.=-'
           `"""`
'''

#Write your code below this line 👇
import random
import time
import os


print("Hello and welcome to a game of `rock, paper, scissors`!\n\
This game consists of 5 rounds on the principle of `best out of 5`.\n\
Type `quit` at any time to end the game prematurely.\n")
input("\nPress Enter to continue ...")
os.system('clear')

hand_signals = ['rock', 'paper', 'scissors']

score = {
    'Computer': 0,
    'You': 0,
}

number_of_rounds = 1
game_over = False
your_signal = None

while number_of_rounds < 6:
    print(f"=== Round {number_of_rounds} ===")
    random_signal = random.randint(0, len(hand_signals) -1)

    while your_signal not in hand_signals:
        your_signal = input("\nType `rock`, `paper` or `scissors`: ").lower()
    
    if hand_signals[random_signal] == your_signal:
        print(f"\nThe computer hand signal is `{hand_signals[random_signal]}` and your hand signal is `{your_signal}`.\nThis is a tie!")
    elif (hand_signals[random_signal] == 'rock') and (your_signal == 'scissors'):
        print(f"\nThe computer hand signal is: {rock} \n...and your hand signal is: {scissors}\nYou lose!")
        score['Computer'] += 1
    elif (hand_signals[random_signal] == 'rock') and (your_signal == 'paper'):
        print(f"\nThe computer hand signal is: {rock} \n...and your hand signal is: {paper}\nYou win!")
        score['You'] += 1
    elif (hand_signals[random_signal] == 'scissors') and (your_signal == 'paper'):
        print(f"\nThe computer hand signal is: {scissors} \n...and your hand signal is: {paper}\nYou lose!")
        score['Computer'] += 1
    elif (hand_signals[random_signal] == 'scissors') and (your_signal == 'rock'):
        print(f"\nThe computer hand signal is: {scissors} \n...and your hand signal is: {rock}\nYou win!")
        score['You'] += 1
    elif (hand_signals[random_signal] == 'paper') and (your_signal == 'rock'):
        print(f"\nThe computer hand signal is: {paper} \n...and your hand signal is: {rock}\nYou lose!")
        score['Computer'] += 1
    else: # `paper` loses to `scissors`
        print(f"\nThe computer hand signal is: {paper} \n...and your hand signal is: {scissors}\nYou win!")
        score['You'] += 1
    
    print("\n--------\n")
    for key, value in score.items():
        print(f"{key}: {value}")
    print("\n--------")

    number_of_rounds += 1
    your_signal = None
    
    input("\nPress Enter to continue ...")
    
    os.system('clear')
    if (score['Computer'] > 2) or (score['You'] > 2):
        break

if score['Computer'] > score['You']:
    input("\nYou lost!\n\nPress Enter to quit.")
    os.system('clear')
    print(computer_win)
elif score['Computer'] < score['You']:
    input("\nYou won!\n\nPress Enter to get your prize!")
    os.system('clear')
    print(you_win)
else:
    input("\nIt's a tie!\n\nPress Enter to quit.")
    os.system('clear')
    print(tie_match)

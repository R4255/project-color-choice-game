#projects colors choice game
import random as random
print("the winning rules of the game are \n enter a number from 1 to 5 and match the computer choice to win")
computer_score=0
player_score=0
while True:#writing it simply means the loop has to run until it breaks
    print("red=1 \nyellow=2 \norange=3 \ngreen=4 \nblue=5 \ntake a turn:")
    player_choice=int(input("user turn:"))
    while player_choice>5 and player_choice<1:
        player_choice=int(input("enter valid input:"))
    if player_choice==1:
        choice_col='red'
    elif player_choice==2:
        choice_col='yellow'
    elif player_choice==3:
        choice_col='orange'
    elif player_choice==4:
        choice_col='green'
    else:
        choice_col='blue'
    print("user color choice is:" + choice_col)
    print("\nnow its the computer's time to pickup the color")
    computer_choice=random.randint(1,5)
    while computer_choice==player_choice:
        computer_choice=random.randint(1,5)
    if computer_choice==1:
        compu_choice_col='red'
    elif computer_choice==2:
        compu_choice_col='yellow'
    elif computer_choice==3:
        compu_choice_col='orange'
    elif computer_choice==4:
        compu_choice_col='green'
    else:
        compu_choice_col='blue'
    print("computer color choice is:"+compu_choice_col)
    if(choice_col==compu_choice_col):
        player_score+=1
        print("player score:"+str(player_score))
        print("computer_score:"+str(computer_score))
    else:
        computer_score+=1
        print('player score:'+str(player_score))
        print("computer_score:"+str(computer_score))
    print("do you want to play again"+"Y/N")
    answer=input()
    if answer=='n' or answer== 'N':
        break
if computer_score==player_score:
    print("game is tied")
    print("Thanks for playing")
elif computer_score>player_score:
    print("computer wins")
    print("you couldn't win")
    print("better luck next time")
elif computer_score<player_score:
    print("player wins")
    print("thanks for playing")


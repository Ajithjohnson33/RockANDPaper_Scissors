import random
game_list = ['Rock','paper','scissors']
computer = c = 0
command = p = 0
print("score:Computer" + str(c) + "Player" + str(p))
# the loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Rock,Paper,scissors or Quit: ")
    if command == computer_choice:
        print("Tie")
    elif command == 'Rock':
        if computer_choice =='scissors':
            print("player won!")
            p+=1
        else:
            print("computer won!")
            c+=1
    elif command =='Paper':
        if command =='Rock':
            print('player won!')
            p+=1
        else:
            print("computer won")
            c+=1
    elif command =='scissors':
        if computer_choice =='paper':
            print("player won!")
            p+=1
        else:
            print("computer won")
            c+=1
    elif command =='Quit':
        break
    else:
        print("wrong command")
    print("player:"+command)
    print("computer:"+computer_choice)
    print("")
    print("score:Computer" +str(c) +" player " +str(p))
    print("")
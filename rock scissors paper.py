import random
pplay=1
player=0
machine=0
win=0
lose=0
tie=0
number=0
cont=0
while pplay==1 and cont==0 :
    player=int(input("welcome to rock paper scissors game. For rock press 0, for paper press 1, for scissors press 2 "))
    number+=1
    machine = random.randint(0, 2)
    if player!= 0 and player!=1 and player!=2:
        print("You are not qualified for this game. Maybe you should try tetris")
        cont+=1
    elif player==0 and machine ==0:
        tie+=1
        print("you chose rock and machine chose rock too. Tie!! " )
    elif player==0 and machine ==1:
        lose+=1
        print("you chose rock and machine chose paper. Lose!! " )
    elif player==0 and machine ==2:
        win+=1
        print("you chose rock and machine chose scissors. Win!! " )
    elif player==1 and machine ==0:
        win+=1
        print("you chose paper and machine chose rock. Win!! " )
    elif player==1 and machine ==1:
        tie+=1
        print("you chose paper and machine chose paper too. Tie!! " )
    elif player==1 and machine ==2:
        lose+=1
        print("you chose paper and machine chose scissors. Lose!! " )
    elif player==2 and machine ==0:
        lose+=1
        print("you chose scissors and machine chose rock. Lose!! " )
    elif player==2 and machine ==1:
        win+=1
        print("you chose scissors and machine chose paper. Win!! " )
    elif player==2 and machine ==2:
        tie+=1
        print("you chose scissors and machine chose scissors too. Tie!! " )
    print(" ")
    pplay=int(input("Do you want to play again? if yes, please press 1. If you dont wanna play new game, press something else "))

print("game is over")
print("you played " + str(number) +" times")
print("win: " + str(win))
print("lose: " + str(lose))
print("tie: " + str(tie))
print("your success rate is : %" + str(round(100*win/number,2)))


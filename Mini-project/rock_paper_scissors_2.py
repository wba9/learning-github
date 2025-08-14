import random
print("=======================\n Rock, Paper, Scissors\n=======================")
emoji = {1 : "✊", 2 : "✋", 3 : "✌️"}

com_round = 0
pyr_round = 0

while com_round < 3 and pyr_round < 3:
    try:
        pyr = int(input('Pick a number\n1) ✊\n2) ✋\n3) ✌️\n'))
        com = random.randint(1,3)
        if pyr not in [1, 2, 3]:
            print("Try again. Not a valid number")
        else:
            print(f"You: {emoji[pyr]}\n Computer: {emoji[com]}")
            if com == pyr:
                print("That's a tie")
            elif (com == 1 and pyr == 3) or (com == 2 and pyr == 1) or (com == 3 and pyr == 2):
                print("The computer wins this round!")
                com_round += 1
                
            else: 
                print("You win this round")
                pyr_round += 1
    except ValueError:
        print("Pick a number bro")
    
if pyr_round > com_round:
        print("")
        print("Player wins!")
elif pyr_round < com_round:
        print("")
        print("Computer wins!")


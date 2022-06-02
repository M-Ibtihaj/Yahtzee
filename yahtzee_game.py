#Libraries: os for system related functionality (clear screen in this program)
#and random for generating random numbers
import os
from random import randint


#--------------------------------Functions--------------------------------------
#welcome fuction to display the welcome banner on startup
def welcome():
    print("\
    ******************************************************************************\
    \n\t\t\t\tWelcome to Yahtzee\n\
    ******************************************************************************\n")
	
#title function for menu items.
def title():
    print("\
    ******************************************************************************\
    \n\t\t\t\t\tYahtzee\n\
    ******************************************************************************\n")

#menu function to show the menu and take user input
def menu():
    welcome()
    print("\n\t\t\t\t     Game Menu\n")
    print("\t\t\t\t    %%%%%%%%%%%%")
    print("\n\t\t\t\t    Play Yahtzee")
    print("\n\t\t\t\t        Help")
    print("\n\t\t\t\t        Exit")

    option = 0
    option = input("\n\nPlease enter your choice from the menu (1 - 3): ")

    return option

	
#help function to display the instructions about the game.
def help():
    print("\n\n1 - This Yahtzee game is designed for 2 players.")
    print("\n\n2 - You need to enter the names of players to start the game.")
    print("\n\n3 - Each player has 3 turns.")
    print("\n\n4 - In first turn all dice are rolled.")
    print("\n\n5 - Second and third turns are optional if player want to reroll dice or not.")
    print("\n\n6 - For second and third turn player will specify the dice for rerolling.")
    print("\n\n7 - Score card will be showed after the player take turns.")
    print("\n\n\t\t\t\t      Good Luck!!!")

#rollDice function to roll all five dice for the first turn.
    #diceCount parameter accepts the count of dice for roll.
diceScores = []
def rollDice():
    for x in range(5):
        diceScores.append(randint(1, 6))# To generate a random number between 1 & 6
    return diceScores

#reRoll function to re-roll specific dice as per player choice.
    #diceCount parameter accepts the count of dice to re-roll.
    #diceNumber parameter accepts the list containing the specific dice-
    #numbers for re-rolling.
def reRoll(diceCount, diceNumber):
    for x in range(diceCount):
       diceScores[int(diceNumber[x])-1] = randint(1, 6)
    return diceScores

#play function to take input from user for rolling and re-rolling dice.
def play():
    
    diceScores.clear()

    #Turn 1
    print("\nTurn 1:\n")        
    rollScore = rollDice()
    print("Dice roll 1 scores: ",rollScore)

    #Turn 2
    turn = input("\nDo you want second turn(yes/no): ")
    
    if(turn == 'yes'):
        print("\nTurn 2:\n")    
        selectDice = input("Please enter the dice you want to reroll \
(use , for separation): ").split(",")
        diceCount = len(selectDice)
        score2 = reRoll(diceCount,selectDice)
        rollScore = score2
        print("Dice roll 2 scores: ",score2)
    elif(turn == 'no'):
        return rollScore
    else:
        print("Invalid answer!")

    #Turn 3
    turn = input("\nDo you want third turn(yes/no): ")
    
    if(turn == 'yes'):    
        print("\nTurn 3:\n")    
        selectDice = input("Please enter the dice you want to reroll \
(use , for separation): ").split(",")
        diceCount = len(selectDice)
        score3 = reRoll(diceCount,selectDice)
        rollScore = score3
        print("Dice roll 3 scores: ",score3)
    elif(turn == 'no'):
        return rollScore
    else:
        print("Invalid answer!")

    return rollScore
           
#scoreCard function to display the complete Yahtzee score card.
    #parameter scores accepts the list containing score of all 5 dice.
def scoreCard(scores):
    print("\
    ******************************************************************************\
    \n\t\t\t\tYahtzee Score Card\n\
    ******************************************************************************\n")    
    scoresRecord = scores
       
    #Upper Section of yahtzee score card
    aces =  scoresRecord.count(1)
    twos =  scoresRecord.count(2)
    threes =  scoresRecord.count(3)
    fours =  scoresRecord.count(4)
    fives = scoresRecord.count(5)
    sixes = scoresRecord.count(6)
    totalScore = sum(scoresRecord)
    if(totalScore >= 63):
        bonus = 35
    else:
        bonus = 0
    upperTotal =  totalScore + bonus
    
    print("\n\t\t\t\t     Upper Section\n")
    print("\t__________________________________________________________________")
    print("\n\tAces (Sum of only Aces): ", aces*1)
    print("\t__________________________________________________________________")
    print("\n\tTwos (Sum of only Twos): ", twos*2)
    print("\t__________________________________________________________________")
    print("\n\tThrees (Sum of only Threes): ", threes*3)
    print("\t__________________________________________________________________")
    print("\n\tFours (Sum of only Fours): ", fours*4)
    print("\t__________________________________________________________________")
    print("\n\tFives  (Sum of only Fives): ", fives*5)
    print("\t__________________________________________________________________")
    print("\n\tSixes (Sum of only Sixes): ", sixes*6)
    print("\t__________________________________________________________________")
    print("\n\tTotal Score: ", totalScore)
    print("\t__________________________________________________________________")
    print("\n\tBonus (If Total Score is 63 or greater): ", bonus)
    print("\t__________________________________________________________________")
    print("\n\tTotal of upper section: ", upperTotal)
    print("\t__________________________________________________________________")

    #Lower Section of yahtzee score card
    fok = 0
    tok = 0
    fh = 0
    yahtzee = 0
    ss = 0
    ls = 0
    chance = 0
    
    if(sixes==3 and (aces==2 or twos==2 or threes==2 or fours==2 or fives==2)):
        fh = 25
    elif(aces==5 or twos==5 or threes==5 or fours==5 or fives==5 or sixes==5):
        yahtzee = 50
    elif(aces==4 or twos==4 or threes==4 or fours==4 or fives==4 or sixes==4):
        fok = sum(scoresRecord)
    elif(aces==3 or twos==3 or threes==3 or fours==3 or fives==3 or sixes==3):
        tok = sum(scoresRecord)
    elif(aces==1 and threes==1 and fours==1 and fives==1 and sixes==1):
        ss = 30
    elif(twos==1 and threes==1 and fours==1 and fives==1 and sixes==1):
        ls = 40
    else:
        chance = sum(scoresRecord)
        
    lowerTotal = fok + tok + fh + yahtzee + ss + ls + chance
    grandTotal = lowerTotal + upperTotal
    
    
    print("\n\n\t\t\t\t     Lower Section\n")
    print("\t__________________________________________________________________")
    print("\n\t3 of a kind (Total of all dice containing 3 similar dice): ",tok)
    print("\t__________________________________________________________________")
    print("\n\t4 of a kind (Total of all dice containing 4 similar dice): ",fok)
    print("\t__________________________________________________________________")
    print("\n\tFull House: ",fh)
    print("\t__________________________________________________________________")
    print("\n\tSmall Straight (Sequence of four dice): ",ss)
    print("\t__________________________________________________________________")
    print("\n\tLarge Straight (Sequence of five dice): ",ls)
    print("\t__________________________________________________________________")
    print("\n\tYahtzee (5 of a kind): ",yahtzee)
    print("\t__________________________________________________________________")
    print("\n\tChance (Total of all 5 dice): ",chance)
    print("\t__________________________________________________________________")
    print("\n\tTotal of Lower Section: ",lowerTotal)
    print("\t__________________________________________________________________")
    print("\n\tTotal of Upper Section: ",upperTotal)
    print("\t__________________________________________________________________")
    print("\n\tGrand Total: ",grandTotal)
    print("\t__________________________________________________________________")

    return grandTotal
    
#----------------------------------Main-----------------------------------------

opt = 'y'

while opt == 'y':
    
    selectOption = menu()

    if(selectOption == '1'):
        print("Please enter players' names:\n")
        player_1 = input("Player 1: ")
        player_2 = input("\nPlayer 2: ")
        
        os.system('cls')
        title()
        print("\n\t\t\t\t     " + player_1 + "'s turn\n")
        
        scores_1 = play()
        print("\n" + player_1 + "'s final dice scores: ", scores_1)
        
        input("\n\n\t\t\t\tPress Enter to see " + player_1 + "'s Score Card")
        grandTotal_1 = scoreCard(scores_1)
        
        input("\n\n\t\t\t\tPress Enter to proceed to " + player_2 + "'s turn")
        
        print("\n\t\t\t\t      " + player_2 + "'s turn\n")
        
        scores_2 = play()
        print("\n" + player_2 + "'s final dice scores: ", scores_2)

        input("\n\n\t\t\t\tPress Enter to see " + player_2 + "'s Score Card")
        grandTotal_2 = scoreCard(scores_2)

        print("\n\n" + player_1 + "'s grand total score: ", grandTotal_1)
        print("\n" + player_2 + "'s grand total score: ", grandTotal_2) 
        
        if(grandTotal_1 == grandTotal_2):
            print("\n\n\t\t\t\t      Game Draw!!!")
        elif(grandTotal_1 > grandTotal_2):
            print("\n\n\t\t\t\t      " + player_1 + " Won the game!!!")
        else:
            print("\n\n\t\t\t\t      " + player_2 + " Won the game!!!")
        

    elif(selectOption == '2'):
        os.system('cls')
        title()
        help()
            
    elif(selectOption == '3'):
        os.system('cls')
        print("Exiting...")
        break

    else:
        print("Invalid Input")

    opt = input("\n\n\t\tDo you want to revisit the Game Menu('y' for yes/any other to quit): ")    
    

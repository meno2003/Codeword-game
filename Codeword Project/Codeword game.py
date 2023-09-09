import getpass  #hide user password
import hashlib
import sys


#Player class for Player related details

class Player:                     
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.guesses = 0
        self.correct_guesses = 0
        self.incorrect_guesses = 0

# Game class for the game details:
class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.currentplayer = 0 # player1 starts

    def next_turn(self):
        self.currentplayer = 1 - self.currentplayer # switch to other player

    def get_current_player(self):
        return self.players[self.currentplayer]
        
       

        

def login(player_name):    
     while True:
        user = input(f"{player_name}, enter your username: ")
        passw = getpass.getpass(f"{player_name}, enter your password: ") # it's a good practice to hide password input
        print()
        with open("players.txt", "r") as f: # read login from txt file
            for line in f.readlines(): # loop through line in txt file
                username, password = line.strip().split("|") # split string into two for username and password
                if (user in username) and (passw in password):
                    print ("Login successful!")
                    print()
                    return True
        print ("Incorrect username or password, Please try again.")

   

# menu for player navigation
def menu():
    print("[1], Start Game!")
    print("[2], Rulebook  ")
    print("[0], Exit Program")


#create players
player1 = Player("Meno", 6 )
player2 = Player("Malik", 6)

login(player1.name)
login(player2.name)

 #create the game with both players
 
game = Game(player1, player2)

#grid displayed to the players


def display_grid():
    for order in player_grid:
        print(order)
        print()
    '\n'
    print(player_key)

        
       
final_grid = [
                [' F', '##', ' L', ' I', ' S', ' T', ' S', '##', '##'],
                [' I', '##', '##', '##', ' #', ' #', ' B', '##', '##'],
                [' L', '##', ' B', ' O', ' T', '##', ' I', '##', '##'],
                [' E', ' #', ' #', ' #', ' #', ' #', ' N', '##', '##'],
                ['##', ' P', ' R', ' O', ' G', ' R', ' A', ' M', '##'],
                ['##', ' Y', '##', '##', '##', '##', ' R', '##', '##'],
                [' S', ' T', ' R', ' I', ' N', ' G', ' Y', '##', ' J'],
                ['##', ' H', '##', '##', '##', '##', '##', '##', ' A'],
                [' C', ' O', ' D', ' I', ' N', ' G', '##', '##', ' V'],
                ['##', ' N', '##', '##', '##', '##', '##', '##', ' A'],
                ]

player_grid = [
                ['22', '##', '10', ' 7', '12', '16', '12', '##', '##'], 
                [' 7', '##', '##', '##', '##', '##', ' 5', '##', '##'],
                ['10', '##', ' 5', ' 4', '16', '##', ' 7', '##', '##'],
                ['11', '##', '##', '##', '##', '##', '19', '##', '##'],
                ['##', '13', '15', ' 4', ' 8', '15', '17', '18', '##'],
                ['##', ' 1', '##', '##', '##', '##', '15', '##', '##'],
                ['12', ' T', '15', ' 7', '19', ' 8', ' 1', '##', '24'],
                ['##', ' 3', '##', '##', '##', '##', '##', '##', '17'],
                ['23', ' 4', ' 2', ' 7', '19', ' 8', '##', '##', ' V'],
                ['##', '19', '##', '##', '##', '##', '##', '##', '17'],
                ]

final_key = [[1,'Y'],[2,'D',],[4,'O'],[5,'B'],[7,'I'],[8,'G'],[10,'L'],[11,'E'],
             [12,'S'],[13,'P'],[15,'R'],[16,'T'],[17,'A'],[18,'M'],[19,'N'],[22,'F'],[23,'C'],[24,'J'],[25,'V']]

player_key = [[1,''],[2,''],[4,''],[5,''],[7,''],[8,''],[10,''],[11,''],
             [12,''],[13,''],[15,''],[16,'T'],[17,''],[18,''],[19,''],[22,''],[23,''],[24,''],[25,'V']]



def display_grid():

    # aligns player_grid evenly
    for order in player_grid:
        print(order)    
    print()
    print(player_key)


def statsheet():
    for player in game.players:
        correct_guesses_str = f"{player.correct_guesses} of them were right :)" if player.correct_guesses > 0 else f"{player.correct_guesses} of them were right :("  #displays accurate emoji for if player got any right or none
        incorrect_guesses_str = f"{player.incorrect_guesses} of them were wrong :(" if player.incorrect_guesses > 0 else f"{player.incorrect_guesses} of them were wrong :)" # ^^^
        print(f"Player {player.name} scored {player.health} points, made {player.guesses} guesses, {correct_guesses_str}, {incorrect_guesses_str}")
def game_loop():
    while True:  # Start an infinite loop
        game_continues = playerinput()  # Get the player's input
        if not game_continues:
            break  # Break out of the loop
        game.next_turn()  # Switch turn to the other player

def playerinput():


    current_player = game.get_current_player()
    
    try:
        print()
        rowindex = int(input( "enter row location:  "))
        columnindex = int(input( "enter column location:  "))
        print()
        rowindex2 = (rowindex-1) # accurately picks list locations 
        columnindex2 = (columnindex-1)

        if rowindex2 not in range(len(player_grid)) or columnindex2 not in range(len(player_grid[0])):   # errorcheck for if input out of bounds or just wrong
            print("Invalid location. Make sure you choose the right location. try again :)")
            return True
        if player_grid[rowindex2][columnindex2] == '##':    #error check for when user chooses unusable location
            print("Invalid location. Are you sure you chose the right spot?")
            return True
    except ValueError:
        print("Invalid location. Are you sure you chose the right spot?")
        return True

    playerguess = input("Enter Your guess:  ")
    print()
    playerguess = playerguess.upper()   #if user enters in lowercase
    playerguess = " " +playerguess  #to fit grid
    current_player.guesses += 1

    if playerguess == final_grid[rowindex2][columnindex2]:
        current_player.health +=2
        current_player.correct_guesses +=1
    
        print("Well done " +current_player.name+ ". Your player health is now",current_player.health)
    else:
        current_player.health -=2
        current_player.incorrect_guesses +=1

        print("unlucky " +current_player.name+ ". Your health now is ",current_player.health)

        if current_player.health<2:
            print("Looks like you exaulted your last life bud. GAME OVER")
            print("Final scores!")
            print()
            statsheet()
            return False

            return game_over()
                
            
    chosennumber1 = player_grid[rowindex2][columnindex2]
    chosennumber = int(chosennumber1.strip()) #convert to num 
    if playerguess == final_grid[rowindex2][columnindex2]:
        print("Great Guess! ")
        #fill out the player_key when guessed right
        for sublist in player_key:
            if sublist[0] == chosennumber:
                sublist[1] = playerguess.strip() #strip to fit list
        for row in range(len(player_grid)):
            for item in range(len(player_grid[row])):
                if player_grid[row][item] == chosennumber1:
                    player_grid[row][item] = playerguess
    else:
        print("Incorrect Guess!")

    if player_grid == final_grid:
        print("Congratulations! You finished the puzzle!")
        print("Final scores!")
        statsheet()
        return False
    elif current_player.health<2:
        print("Looks like you exalted your last life bud. GAME OVER")
        print("Final scores!")
        statsheet()
        return False
    
    display_grid()
    
    
    game.next_turn()  # Switch turn to the other player
    return True
    playerinput()  # Call for the next turn


def game_over():
    print("[1], Start Game!")
    print("[2], Rulebook  ")
    print("[0], Exit Program")
   
    option = int(input("Enter an option: "))
    while option != 0:
        if option == 1:
            print()
            display_grid()
            playerinput()
        elif option == 2:
            print()
            print(rule_book)
            print()
            return menu()  # Return to menu function after displaying rule book
        else:
            print("Invalid Option lad, Try again.")
            break
# Initialize playerhealth outside of the playerinput function
playerhealth = 5






rule_book = " Hey, Im sure you already know how to play codeword but this one has a bit of a twist :} \n This time you have a health bar! so be extra careful with your guesses!\n 6 lives to be exact! if any of you reach below 2 it is game over. So take your time guessing! \n Or you'll Lose !!!  D:"






menu()
option = int(input("Enter an option: "))

while option != 0:
    if option == 1:
        print()
        display_grid()
        game_loop()
        
    elif option == 2:
        print()
        print(rule_book)
        print()
        menu()
        
    else:
        print("Invalid Option lad, Try again.")
    break








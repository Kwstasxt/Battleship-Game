import pygame
import numpy as np
from random import randint

pygame.init()
pygame.font.init()
#Creating the board.
screen = pygame.display.set_mode((825,625))
pygame.display.set_caption("Battleship")
board = []
board = np.zeros((6,8))
#Icons
gameicon = pygame.image.load('battleship.png')
flameIcon = pygame.image.load('flame2.png')
corveteIcon = pygame.image.load('Corvete.png')
corveteIconResized = pygame.transform.scale(corveteIcon,(60,260))
BattleshipIcon = pygame.image.load('Small_Battleship.png')
BattleshipIconResized = pygame.transform.scale(BattleshipIcon,(60,160))
BigBattleshipIcon = pygame.image.load('Huge_Battleship.png')
BigBattleshipIconResized = pygame.transform.scale(BigBattleshipIcon,(60,360))
pygame.display.set_icon(gameicon)
#Font
myfont = pygame.font.SysFont('Comic Sans MS', 30)
Num1 = myfont.render('1', False, (0, 0, 0))
Num2 = myfont.render('2', False, (0, 0, 0))
Num3 = myfont.render('3', False, (0, 0, 0))
Num4 = myfont.render('4', False, (0, 0, 0))
Num5 = myfont.render('5', False, (0, 0, 0))
Num6 = myfont.render('6', False, (0, 0, 0))
Num7 = myfont.render('7', False, (0, 0, 0))
Num8 = myfont.render('8', False, (0, 0, 0))
#---------------------------------------------
screen.fill((0,100,150))
Line_Color  = (0,0,0)
Color = (0,0,0)
#Overwrite bottom-right side color of the screen.
pygame.draw.rect(screen,(255,255,255),((0,601),(800,24)))
pygame.draw.rect(screen,(255,255,255),((801,0),(24,600)))
#Creating Vertical Lines for the board.
pygame.draw.line(screen,Line_Color,(100,0),(100,625))
pygame.draw.line(screen,Line_Color,(200,0),(200,625))
pygame.draw.line(screen,Line_Color,(300,0),(300,625))
pygame.draw.line(screen,Line_Color,(400,0),(400,625))
pygame.draw.line(screen,Line_Color,(500,0),(500,625))
pygame.draw.line(screen,Line_Color,(600,0),(600,625))
pygame.draw.line(screen,Line_Color,(700,0),(700,625))
pygame.draw.line(screen,Line_Color,(800,0),(800,625))
#Creating Horizontal Lines for the board.
pygame.draw.line(screen,Line_Color,(0,100),(825,100))
pygame.draw.line(screen,Line_Color,(0,200),(825,200))
pygame.draw.line(screen,Line_Color,(0,300),(825,300))
pygame.draw.line(screen,Line_Color,(0,400),(825,400))
pygame.draw.line(screen,Line_Color,(0,500),(825,500))
pygame.draw.line(screen,Line_Color,(0,600),(825,600))
#---------------------------------------------------#
#Draw icon on bottom-right side of the screen.
pygame.draw.rect(screen,(255,0,0),((801,601),(25,25)))
screen.blit(gameicon,(805,605))

#Draw Row-Column numbers.
#Columns!
screen.blit(Num1,(45,605))
screen.blit(Num2,(145,605))
screen.blit(Num3,(245,605))
screen.blit(Num4,(345,605))
screen.blit(Num5,(445,605))
screen.blit(Num6,(545,605))
screen.blit(Num7,(645,605))
screen.blit(Num8,(745,605))
#Rows!
screen.blit(Num1,(808,45))
screen.blit(Num2,(808,145))
screen.blit(Num3,(808,245))
screen.blit(Num4,(808,345))
screen.blit(Num5,(808,445))
screen.blit(Num6,(808,545))
#Update the final screen.
pygame.display.update()


#Methods
def draw_fire(X,Y):
    X = X*100+20
    Y = Y*100+20
    screen.blit(flameIcon,(X,Y))
    pygame.display.update()

def place_Corvette():
    print ("1)Place Corvette first!")
    print ("Type X,Y coordinates for the center of your ship")
    StartX = int(raw_input("Start X coordinates: "))
    StartY = int(raw_input("Start Y coordinates: "))
    
    print ("Choose orientation. You can place the ship horizontally or vertically")
    orientation = (raw_input("Choose Orientation (H or V): "))
    while (orientation!='V' and orientation!='H'):
        print ("Input Error: You must enter V or H")
        orientation = (raw_input("Choose Orientation (H or V): "))
    if (orientation=="H"):

        while (StartX<2 or StartY <0 or StartX>7 or StartY>6):
            print ("You cant place corvette there!")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))
    else:
        while (StartX<0 or StartY<2 or StartX>8 or StartY>5):
            print ("You cant place corvette there!")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))
    corvRotated = pygame.transform.rotate(corveteIconResized,90)
    
    if (orientation=="V"):
        transX = StartX*100+20 -100
        transY = StartY*100+20-200
        screen.blit(corveteIconResized,(transX,transY))
        board[StartY-1][StartX-1] = 5
        board[StartY-2][StartX-1] = 5
        board[StartY][StartX-1] = 5
    else:
        transX = StartX*100+20-200
        transY = StartY*100+20-100
        screen.blit(corvRotated,(transX,transY))
        board[StartY-1][StartX-1] = 5
        board[StartY-1][StartX] = 5
        board[StartY-1][StartX-2] = 5
    pygame.display.update()

def place_Battleship_big():
    print ("2)Place Big Battleship!")
    print ("Type X,Y coordinates for the center of your ship")
    StartX = int(raw_input("Start X coordinates: "))
    StartY = int(raw_input("Start Y coordinates: "))
    
    print ("Choose orientation. You can place the ship horizontally or vertically")
    orientation = (raw_input("Choose Orientation (H or V): "))
    while (orientation!='V' and orientation!='H'):
        print ("Input Error: You must enter V or H")
        orientation = (raw_input("Choose Orientation (H or V): "))
    
    if (orientation=="H"):

        while (StartX<3 or StartY <0 or StartX>6 or StartY>6):
            print ("You cant place Battleship there!")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))

        while (board[StartY-1][StartX-1]==5 or board[StartY-1][StartX-2]==5 or board[StartY-1][StartX]==5 or board[StartY-1][StartX-3]==5 ):
             print ("You cant place Battleship there!")
             print ("Another ship had taken this position")
             print ("Please choose a different location")
             StartX = int(raw_input("Start X coordinates: "))
             StartY = int(raw_input("Start Y coordinates: "))

    else:
        while (StartX<0 or StartY<2 or StartX>8 or StartY>4):
            print ("You cant place corvette there!")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))
        
        while (board[StartY-1][StartX-1]==5 or board[StartY-2][StartX-1]==5 or board[StartY-3][StartX-1]==5 or board[StartY][StartX-1]==5 ):
             print ("You cant place Battleship there!")
             print ("Another ship had taken this position")
             print ("Please choose a different location")
             StartX = int(raw_input("Start X coordinates: "))
             StartY = int(raw_input("Start Y coordinates: "))

    BigBattleshipIconRotated = pygame.transform.rotate(BigBattleshipIconResized,90)
    
    if (orientation=="V"):
        transX = StartX*100+20 -100
        transY = StartY*100+20-200
        screen.blit(BigBattleshipIconResized,(transX,transY))
        board[StartY-1][StartX-1] = 5
        board[StartY-2][StartX-1] = 5
        board[StartY+1][StartX-1] = 5
        board[StartY][StartX-1] = 5

    else:
        transX = StartX*100+20-200
        transY = StartY*100+20-100
        screen.blit(BigBattleshipIconRotated,(transX,transY))
        board[StartY-1][StartX-1] = 5
        board[StartY-1][StartX-2] = 5
        board[StartY-1][StartX] = 5
        board[StartY-1][StartX+1] = 5
    pygame.display.update()

def place_Battleship_small():
    print ("3)Place the final Battleship!")
    print ("Type X,Y coordinates for the center of your ship")
    StartX = int(raw_input("Start X coordinates: "))
    StartY = int(raw_input("Start Y coordinates: "))
    
    print ("Choose orientation. You can place the ship horizontally or vertically")
    orientation = (raw_input("Choose Orientation (H or V): "))
    while (orientation!='V' and orientation!='H'):
        print ("Input Error: You must enter V or H")
        orientation = (raw_input("Choose Orientation (H or V): "))
    if (orientation=="H"):

        while (StartX<1 or StartY <0 or StartX>7 or StartY>6):
            print ("Out of Bounds: You cant place Battleship there!")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))

        while (board[StartY-1][StartX-1]==5 or board[StartY-1][StartX]==5):
            print ("You cant place Battleship there!")
            print ("Another ship had taken this position")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))
    else:
        while (StartX<0 or StartY<1 or StartX>8 or StartY>5):
            print ("You cant place Battleship there!")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))

        while (board[StartY][StartX-1]==5 or board[StartY-1][StartX-1]==5):
            print ("You cant place Battleship there!")
            print ("Another ship had taken this position")
            print ("Please choose a different location")
            StartX = int(raw_input("Start X coordinates: "))
            StartY = int(raw_input("Start Y coordinates: "))    

    BattleshipIconRotated = pygame.transform.rotate(BattleshipIconResized,90)
    
    if (orientation=="V"):
        transX = StartX*100+20 -100
        transY = StartY*100+20-100
        screen.blit(BattleshipIconResized,(transX,transY))
        board[StartY-1][StartX-1] = 5
        board[StartY][StartX-1] = 5
        
    else:
        transX = StartX*100+20-100
        transY = StartY*100+20-100
        screen.blit(BattleshipIconRotated,(transX,transY))
        board[StartY-1][StartX] = 5
        board[StartY-1][StartX-1] = 5
        
    pygame.display.update()

def random(panel):
    return randint(0,len(panel)-1)

def randomC(panel):
    return randint(0,len(panel[0])-1)

#Previously used method. It is not used in this version.
def draw_ship(Y,X):
    StartX = X*100+20
    StartY = Y*100+20
    width = 60
    height = 60
    pygame.draw.rect(screen,Color,((StartX,StartY),(width,height)))
    pygame.display.update()
    
def place_opponent_ships():
    Ships_placed = 0
    #first_row = random(board)
    #first_col = randomC(board)
    orientation = 'V'
    randomly = randint(0,1)
    if (randomly==0):
        orientation = 'H'
    
        #Corvette first.
        
    if (orientation=='H'):
        first_row = randint(0,5)
        first_col = randint(0,5)

        while (board[first_row][first_col]==5 or board[first_row][first_col+1]==5 or board[first_row][first_col+2]==5):
            first_row = randint(0,5)
            first_col = randint(0,5)

        
        board[first_row][first_col]= 1  
        board[first_row][first_col+1] =1
        board[first_row][first_col+2] = 1  
        Ships_placed = Ships_placed+1

            
    else:
        
        first_row = randint(0,3)
        first_col = randint(0,7)
        while (board[first_row][first_col]==5 or board[first_row+1][first_col]==5 or board[first_row+2][first_col]==5):
            first_row = randint(0,3)
            first_col = randint(0,7)

        
        board[first_row][first_col]= 1  
        board[first_row+1][first_col] =1
        board[first_row+2][first_col] = 1
        
        
    #Big battleship 
    #first_row = random(board)
    #first_col = randomC(board)
    orientation = 'V'
    randomly = randint(0,1)
    if (randomly==0):
        orientation = 'H' 

    if (orientation=='H'):
        first_row = randint(0,5)
        first_col = randint(0,4)

        while (board[first_row][first_col]==5 or board[first_row][first_col+1]==5 or board[first_row][first_col+2]==5
        or board[first_row][first_col+3]==5 or board[first_row][first_col]==1 or board[first_row][first_col+1]==1 or board[first_row][first_col+2]==1
        or board[first_row][first_col+3]==1):
            first_row = randint(0,5)
            first_col = randint(0,4)

        board[first_row][first_col]= 1  
        board[first_row][first_col+1] =1
        board[first_row][first_col+2] = 1
        board[first_row][first_col+3] = 1
        
    else:
        first_row = randint(0,2)
        first_col = randint(0,7)
        while (board[first_row][first_col]==5 or board[first_row+1][first_col]==5 or board[first_row+2][first_col]==5
        or board[first_row+3][first_col]==5 or board[first_row][first_col]==1 or board[first_row+1][first_col]==1 or board[first_row+2][first_col]==1
        or board[first_row+3][first_col]==1):
            first_row = randint(0,2)
            first_col = randint(0,7)

        board[first_row][first_col]= 1  
        board[first_row+1][first_col] =1
        board[first_row+2][first_col] = 1
        board[first_row+3][first_col] = 1

    #Small Battleship
    #first_row = random(board)
    #first_col = randomC(board)
    orientation = 'V'
    randomly = randint(0,1)
    if (randomly==0):
        orientation = 'H' 

    if (orientation=='H'):
        
        first_row = randint(0,5)
        first_col = randint(0,6)
        while (board[first_row][first_col]==5 or board[first_row][first_col+1]==5 
        or board[first_row][first_col]==1 or board[first_row][first_col+1]==1):
            first_row = randint(0,5)
            first_col = randint(0,6)

        board[first_row][first_col]= 1  
        board[first_row][first_col+1] =1
        
    else:
        first_row = randint(0,4)
        first_col = randint(0,7)

        while (board[first_row][first_col]==5 or board[first_row+1][first_col]==5 
        or board[first_row][first_col]==1 or board[first_row+1][first_col]==1):
            first_row = randint(0,4)
            first_col = randint(0,7)

        board[first_row][first_col]= 1  
        board[first_row+1][first_col] =1
       

    
    print ("Opponent placed his ships!")        


print ("Game Started! ")
place_Corvette()
place_Battleship_big()
place_Battleship_small()
place_opponent_ships()
#-------------
#Debug Lines.
#draw_fire(0,0)
#draw_ship(1,2)
#draw_fire(1,2)
#print (board)
#-------------

#Game Logic
#Display rounds
round = 1
#3 ships: Battleship 4 , Corvete 3, Ship 2
player_Health = 9 
opponent_Health = 9

#print (board)
#print (len(board[0]))
#print (len(board))
    
#Player == 5 , Opponent = 1
#print the map.
#For development only reasons.
#print (board)
print ("")
print ("")
#Board MAP
#0 is unhitted yet square.
#1 is enemys ship location
#5 is players ship location
#6 is hitted square.

#print rounds
print ("Round %d \n"%round)
print ("")
print ("Valid moves are: ")
print ("Row: 1-6")
print ("Column: 1-8")
print ("")
while (player_Health>0 and opponent_Health>0):
    print ("Players Health: %d \n"%player_Health)
    print ("Opponents Health %d \n"%opponent_Health)

    successful_hit = False
    print ("It's your Turn Now! \n")
    #i want user to type values between 1-8, 1-6.
    player_move = int(raw_input("Guess col: "))-1
    player_move_C = int(raw_input("Guess row: "))-1
    
    while (player_move<0 or player_move>(len(board[0])-1) or player_move_C<0 or player_move_C>(len(board)-1)):
        print ("You entered out of bounds location. \n")
        print ("Please try again.")
        player_move = int(raw_input("Guess col: "))-1
        player_move_C = int(raw_input("Guess row: "))-1

    if (board[player_move_C][player_move]!=6):
        if (board[player_move_C][player_move]==1):
                    opponent_Health = opponent_Health -1
        if (board[player_move_C][player_move]==5):
            print ("Be careful! You hitted your own ships!")
            player_Health = player_Health - 1        
    #6 stands for hitted successfully square.  
        board[player_move_C][player_move] = 6
        draw_fire(player_move,player_move_C)
       
        successul_hit = True
    else:
        print ("This had already taken a hit! \n")
        print ("Please try another. \n")
    
    print (" ") 
    #ok opponents turn now!
    print ("Opponents Turn Now! \n")
    enemy_ready = False
    while (enemy_ready==False):
        opp_move_c = random(board)
        opp_move = randomC(board)
        
        #----------------------------------------
        if (board[opp_move_c][opp_move]!=6 and board[opp_move_c][opp_move]!=1):
            if (board[opp_move_c][opp_move]==5):
                player_Health = player_Health -1
            board[opp_move_c][opp_move] = 6
            enemy_ready = True
            print ("Opponent played: Col = %d "%(opp_move+1))
            print ("Opponent played: Row = %d "%(opp_move_c+1))
            print ("")
            draw_fire(opp_move,opp_move_c)
    if (successful_hit):
        round = round+1
        print ("Round %d \n"%round)
        print (board)
else:
    if (player_Health>opponent_Health):
        print ("Congratulations! You destroyed them Captain!")
    else:
        print ("Game Over!")
        print ("Better luck next time! ")


pygame.display.update()

#Running condition. Terminates if user closes window.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit
            running = False

    







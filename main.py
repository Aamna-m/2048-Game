#Build 2048 in python using pygame!! 
#Took the display ideas from the snake game using pygame
#https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
#Used this to create the rectangle board

#Importing pygame to create a game in python
import pygame
#Importing random to use random randint
import random
#Initializing all the modules needed for pygame
pygame.init()

#Setting the width of the whole game display to 600
WIDTH = 600
#Setting the length of the whole game display to 500
HEIGHT = 500
#Using this to display the width and height of the game board on our coding space
screen = pygame.display.set_mode([WIDTH, HEIGHT])
#Adding a caption to the game and introducing our game
pygame.display.set_caption('2048 By: Aamna')
#Selecting the font for the pygame first part for the text and the second part for the text size
font = pygame.font.Font('freesansbold.ttf', 25)

# Using the RGB colors for the different tiles and other background colors
#Also using the RGB colors for the the lighter and dark texts
#All this useing the curly brackets to define the lists
colors = {
    0: (73, 126, 201),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    'light text': (249, 246, 242),
    'dark text': (119, 110, 101),
    'other': (0, 0, 0),
    'bg': (18, 4, 9)
}

#Game variables initialize
#This is a a combination of two lists, the first one creates the rows with 0 or blanks and the second list creates the columns of the board
#This creates the 4 by 4 board
game_board_values = [[0 for _ in range(4)] for _ in range(4)]
#Setting the game over to false because the game hasnt even been played yet
stop_playing = False
#This variable is used to see if you need to bring new tiles to the board as needed and it is set to True because new tiles are brought each time
spawn_new = True
#This is the inital count of the number of tiles already on the board
#This variable is used with the spawn_new variable because then you can see if you need to add more tiles and compare it with the initial tiles during the game
init_count = 0
#Setting the direction to nothing because the directions havent been set to any value yet
directiontion = ''
#Since the game still needs to be played the score is 0
score = 0


# draw game over and restart text
#Creating a new variable if the player lost
def draw_over():
    #This function is used to draw the board by using the pygame draw tool from the importing pygame library
    #The first bit is drawing the rectangle, then the color of the border which is black
    #The secondly the string represents the top of the rectangle in the corner (its x and y position) meaning 50 pixels from the right and 50 from down
    #300, 100 represent the height and width
    #The 0, 10 means theres no border (0) and 10 pixels is the radius
    pygame.draw.rect(screen, 'black', [50, 50, 300, 100], 0, 10)
    #Using font.render it will create a space to write "Game Over" once the game is over, True and white make the font look more smoother and appealing
    game_over_text1 = font.render('Game Over!', True, 'white')
    #After the player knows they have lost it will print press enter to restart
    #This will display after the Game over, the font being white here as well
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    #This positions the text 130 pixels to the right and 65 pixels down from the top left corner
    screen.blit(game_over_text1, (130, 65))
    #This positions the text 70 pixels to the right and 105 pixels down from from the top left corner
    screen.blit(game_over_text2, (70, 105))


# take your turn based on direction 
#Reference: Asked Livjot for a bit of help in the merging part and what i was not able to understand, Websites: https://data-flair.training/blogs/python-2048-game/, https://www.geeksforgeeks.org/2048-game-in-python/


def take_turn(directiontion, game_board):
    #in the take_turn function we check everything moving in the game_board and display it all in one. So we would merge and move them all into another number.

    global score
    #Needs to create a list of what tiles have merge and what not. At the begining wed add false since nothing is merged yet. The _ is also there since we dont know for sure what numbers would merge therefore a variable isnt needed.
    merged = [[False for _ in range(4)] for _ in range(4)]
    if directiontion == 'UP':
        for i in range(4):
            #The range is 4 since our grid is 4 and 4 so the numbers would move within these boxes. The range also determines tha the top row is going to merge first.
            for y in range(4):
                #We move according to the 0's on the game_board. So we set a variable to 0
                blank_spaces = 0
                #If your in a row that isnt the top row because the top row tiles would not move up since theyre already at the top row.
                if i > 0:
                    #This for loop checks checks everypiece right above the current piece and see if its 0.
                    for current_piece in range(i):
                        if game_board[current_piece][y] == 0:
                            #If there is nothing above move 1
                            blank_spaces += 1
#Create another if statement so if there are still more 0s on top
                    if blank_spaces > 0:
                        #Allows the tiles to blank_spaces from all the zeros till the top row
                        #The tiles that are underneth the moving tiles will check the empty spaces and move up as well.
                        game_board[i - blank_spaces][y] = game_board[i][y]
                        #This now means that the part of the game_board the tiles had moved is going to be ecurrent_pieceual to 0.
                        game_board[i][y] = 0
#If the tiles are together and the same we want them to merge however we dont want them to merge if the tiles have already merged together since 2048 dos not let multiple tiles merge all at one. The \ allows the condition to go on the next row.
                    if game_board[i - blank_spaces - 1][y] == game_board[i - blank_spaces][y] and not merged[i - blank_spaces][y] \
                            and not merged[i - blank_spaces - 1][y]:
                        #To double the original vlaue and empty out the space of the previous tile.
                        game_board[i - blank_spaces - 1][y] *= 2
                        ##LOOK AT LATER
                        score += game_board[i - blank_spaces - 1][y]
                        #Cleares the previous tile to 0
                        game_board[i - blank_spaces][y] = 0
                        #This allows the new value to be printed
                        merged[i - blank_spaces - 1][y] = True

    elif directiontion == 'DOWN':
        ##The range is different from UP as we want the bottom rows to merge first rather than the top ones. The reason the range is also three and not for the rest of the move functions is becaus DOWN is the only fucntion where we need the tites to move in a negative direction and all the other directions are counted as positive.
        for i in range(3):
            for y in range(4):
                blank_spaces = 0
                #The rest of the code is similar to what we did in UP however instead of subtraction we do addition because we want them to move the opposite/negative side which is down.
                for current_piece in range(i + 1):
                    #
                    if game_board[3 - current_piece][y] == 0:
                        blank_spaces += 1
                if blank_spaces > 0:
                    game_board[2 - i + blank_spaces][y] = game_board[2 - i][y]
                    game_board[2 - i][y] = 0
                if 3 - i + blank_spaces <= 3:
                    #Merges the last blocks first and does not merge the blocks again if they have already been merged.
                    if game_board[2 - i + blank_spaces][y] == game_board[3 - i + blank_spaces][y] and not merged[3 - i + blank_spaces][y] \
                            and not merged[2 - i + blank_spaces][y]:
                        game_board[3 - i + blank_spaces][y] *= 2
                        score += game_board[3 - i + blank_spaces][y]
                        game_board[2 - i + blank_spaces][y] = 0
                        merged[3 - i + blank_spaces][y] = True

#If the direction chosen is left
    elif directiontion == 'LEFT':
        #The code is pretty similar to the UP and DOWN function however we change for current_piece to y as now we want the y axis tiles to move.
        for i in range(4):
            for y in range(4):
                blank_spaces = 0
                for current_piece in range(y):
                    if game_board[i][current_piece] == 0:
                        blank_spaces += 1
                if blank_spaces > 0:
                    game_board[i][y - blank_spaces] = game_board[i][y]
                    game_board[i][y] = 0
                if game_board[i][y - blank_spaces] == game_board[i][y - blank_spaces - 1] and not merged[i][y - blank_spaces - 1] \
                        and not merged[i][y - blank_spaces]:
                    game_board[i][y - blank_spaces - 1] *= 2
                    score += game_board[i][y - blank_spaces - 1]
                    game_board[i][y - blank_spaces] = 0
                    merged[i][y - blank_spaces - 1] = True

    elif directiontion == 'RIGHT':
        for i in range(4):
            for y in range(4):
                blank_spaces = 0
                for current_piece in range(y):
                    if game_board[i][3 - current_piece] == 0:
                        blank_spaces += 1
#Starting from the right and moving from the left to check for empty spaces
                if blank_spaces > 0:
                    #After checking the zero we add the blank spaces and since we are adding now it will be moving to the right
                    game_board[i][3 - y + blank_spaces] = game_board[i][3 - y]
                    game_board[i][3 - y] = 0
#the reason its a four cause now we want to check the entire board so it wont go off board
                if 4 - y + blank_spaces <= 3:
                    if game_board[i][4 - y + blank_spaces] == game_board[i][3 - y + blank_spaces] and not merged[i][4 - y + blank_spaces] \
                            and not merged[i][3 - y + blank_spaces]:
                        game_board[i][4 - y + blank_spaces] *= 2
                        score += game_board[i][4 - y + blank_spaces]
                        game_board[i][3 - y + blank_spaces] = 0
                        merged[i][4 - y + blank_spaces] = True
    #Processes how the game_board looks after each turn is made and displays it on the game game_board
    return game_board

#Refreneces 

#This helped me to create a background of the color and how to change it.
#https://www.geeksforgeeks.org/how-to-change-screen-background-color-in-pygame/
#This website showed me how to create a spacing betweenn tiles and how to create tiles, and plus chossing a font for the numbers to be in. 
#https://techvidvan.com/tutorials/python-2048-game-project-with-source-code/
#This helped me to create the pygame rectangle where the game is being played 
#https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/
  
# spawn in new pieces randomly when turns start 
def new_pieces(game_board):
    #if the count is 0 meaning there are empty spaces on the game board
    count = 0
    # function checks if the  game board is full and if it's not then it will continue with the onward code
    full = False
    #this function will check to see if there is some zero (available space) in some row inside the board.
    while any(0 in row for row in game_board) and count < 1:
        #If there is a zero within a row and column then the random function will produce a number in either row or column.
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if game_board[row][col] == 0:
            count += 1
            #Using this function will give us a 1 in 10 chance to give us a 4 on the grid in either row or column
            if random.randint(1, 10) == 10:
                game_board[row][col] = 4
            #In the other 3/4 it will give us a 2 as a new value.
            else:
                game_board[row][col] = 2
    if count < 1:
        full = True

    return game_board, full


# draw background for the game_board
def draw_game_board():
    #Make the game board shape rectangle with the py game function and then address the background from the list.
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)
    score_text = font.render(f'Score: {score}', True, 'black')
    screen.blit(score_text, (10, 410))
    pass


# draw tiles for game
def draw_pieces(game_board):
    #Using nested for loop make the rectangle pieces on the board
    for i in range(4):
        #This will go through each row of data and address the column of the data
        for y in range(4):
            #Assign a variable and store the value of i and j
            value = game_board[i][y]
            #Create an If statement for the number of the tile that is more than 8 because the higher the number of the tile the darker the background would be. For that reason on top, we would need lighter text.
            if value > 8:
                value_color = colors['light text']
            #It goes the same for the tiles that are less than 8 because their background is light, so we need darker text to be on top.
            else:
                value_color = colors['dark text']
            #This function demonstrates that the background would be black if the number is higher or equal to 2048.
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            #In order to have 20 spacing between every tile. We need 20 on the left, 20 on the right, and 20 in between each other. That concludes to be 5 spaces between 20, which means we have 300 spacing that will be filled with rectangles. 300 divided by 4 would be 75. 95 and 20 and the top left and right corners. The first squares need to be 20 by 20 and I and J are going to be equal to 0.
            pygame.draw.rect(screen, color, [y * 95 + 20, i * 95 + 20, 75, 75],
                             0, 5)
            #this function will help us check the value
            if value > 0:
                value_len = len(str(value))
                #Font on the rectangle tiles and their size. Also if the tile has more characters, then the font size would decrease by 5.
                font = pygame.font.Font('freesansbold.ttf',
                                        48 - (5 * value_len))
                #The more the game moves on we want the color of the tile to change accordingly to the number that we have picked before.
                value_text = font.render(str(value), True, value_color)

                text_rect = value_text.get_rect(center=(y * 95 + 57,
                                                        i * 95 + 57))
                #center point of the rectangle that would hold the value
                screen.blit(value_text, text_rect)
                #This function makes a thick black outline outside of the tiles
                pygame.draw.rect(screen, 'black',
                                 [y * 95 + 20, i * 95 + 20, 75, 75], 2, 5)



play = True
#If the user wants to continue playing
while play:
    #Colour the background of the game_board white
    screen.fill('white')
    #Call for the function that includes the score and board
    draw_game_board()
    #add the tiles 
    draw_pieces(game_board_values)
    #When new tiles comes in
    if spawn_new or init_count ==0:
        game_board_values, stop_playing = new_pieces(game_board_values)
        spawn_new = False
        init_count += 1
    #After the user has taken their turn
    if directiontion != '':
        game_board_values = take_turn(directiontion, game_board_values)
        #Reset the direction string to nothing after the user clicks a key so that code can restart the process or merging and moving the tiles
        directiontion = ''
        spawn_new = True
    #For each key assign the merging function to them
    for event in pygame.event.get():
        #If you press the red x button on the screen then it will break the while loop of the window and it will close
        if event.type == pygame.QUIT:
            #Break the while loop
            play = False
        #When the user presses the up arrow key then the merge and move the board up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                directiontion = 'UP'
            #When the user presses teh down arrow key then everything will move down
            elif event.key == pygame.K_DOWN:
                directiontion = 'DOWN'
            #When the user preses the left key everything will move left
            elif event.key == pygame.K_LEFT:
                directiontion = 'LEFT'
            #When the user presses the right arrow key then the board will move to the right
            elif event.key == pygame.K_RIGHT:
                directiontion = 'RIGHT'

#Put code onto the screen. In pygame this is used to display all of the code
    pygame.display.flip()
#To close the program
pygame.quit()


import os
import random
import pygame
 # from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 800

# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple game development practice")



# Get the change of direction , if there is no change , keep the current
# Also initialize the starting direction





# this probably does nothing now
img = pygame.image.load('images/player.png')
playerx = 370
playery = 480




#velicina bloka platforme, ili zidova unutar igre
tile_size = 30


class World():
    def __init__(self, data):
        self.tile_list = []
        row_count = 0
        col_count = 0
        block_img = pygame.image.load('images/spacewall.jpg')
        # for loop za popunjavanje bloka
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(block_img,  (5, 30))
                    img_oblik = img.get_rect()
                    # pozicija bloka
                    if col_count >= 26:
                        img_oblik.x = (col_count * 30) + 15
                    else:
                        img_oblik.x = col_count * tile_size
                    img_oblik.y = row_count * tile_size
                    tile = (img, img_oblik)
                    self.tile_list.append(tile)
                elif tile == 2:
                    img = pygame.transform.scale(block_img, (50, 30))
                    img_oblik = img.get_rect()
                    # pozicija bloka
                    img_oblik.x = col_count * tile_size
                    img_oblik.y = row_count * tile_size
                    tile = (img, img_oblik)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])


world_data =[
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

#player = Player(100, screen_height - 170)
world = World(world_data)
# load images
bg_img = pygame.image.load('images/bg.jpg')















                                            #Finding the previous move direction


class Food(pygame.sprite.Sprite):


    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([15, 15])
        self.image.fill((100, 100, 255))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.n = 0 #random numbers for spawning the food sprite
        self.m = 0
    def control(self,x):

        if x == 1:

            self.n = random.randint(5, 795)
            self.m = random.randint(5, 795)
    def update(self):


        if self.n and self.m != 0:
            self.rect.x = self.n
            self.rect.y = self.m
        else:
            self.rect.x = 150
            self.rect.y = 360
class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('images', 'player.png')).convert()
        playimg = pygame.transform.scale(img ,(15, 20))

        self.images.append(playimg)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.direction = 0
        self.start = 0
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.frame = 0  # count frames
        self.x_change = 0
        self.y_change = 0
        self.colided = 0

    def control(self, x, y, z):

        #Cancelling the breaks or backward movement
        # IF movey is already equal to -2 or if its equal to 2 , then y cannot be -2 or 2 again. Aka only it can be changed from
        #the x Axis and vice versa
        """
        control player movement
        """
        if z < 3 and z != 0:
            self.movey = 0    # canceling the movement in the other axis , so you dont move sideways
        elif self.movey == 0: # Do not update movement if the change is on the same axis.
            self.movey += y

        if z > 2 and z < 5:
            self.movex = 0
        elif self.movex == 0:
            self.movex += x
        print('%d', self.movex)



    def update(self):
        """
        Update sprite position
        """
        if self.movex < -steps or self.movex > steps:
            if self.movex < -steps:
                self.movex = -steps
            else:
                self.movex = steps
                print('dont go faster')

        if self.rect.x > self.rect.x + self.movex:
            self.direction = 2
        elif self.rect.x < self.rect.x + self.movex:
            self.direction = 1
        self.rect.x = self.rect.x + self.movex

        if self.movey < -steps or self.movey > steps:
            if self.movey < -steps:
                self.movey = -steps
            else:
                self.movey = steps
        if self.rect.y > self.rect.y + self.movey:
            self.direction = 3
        elif self.rect.y < self.rect.y + self.movey:
            self.direction = 4

        self.rect.y = self.rect.y + self.movey

        """ 
        IF the player goes outside of the play screen aka 800 pixels, then teleport him back to the 
               oposite end but keeping the position of the other axis
        """
        if self.rect.y > 800 or self.rect.y < 0:

            if self.rect.y > 800:
                self.rect.y = 0
            elif self.rect.y < 0:
                self.rect.y = 800

        if self.rect.x > 800 or self.rect.x < 0:

            if self.rect.x > 800:
                self.rect.x = 0
            elif self.rect.x < 0:
                self.rect.x = 800


player = Player()   # spawn player
food = Food()
player.rect.x = 100 # go to x
player.rect.y = 37  # go to y

all_sprite_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
player_list.add(player)
player_list.add(food)



clock = pygame.time.Clock()
snake_List = []
Lenght_of_snake = 1

score_number = '0'
snake_block = 15
# Creating a text object for when the game is ended
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Game Over', True, blue, (255, 255, 0))
textRect = text.get_rect()
textRect.center = (800 // 2, 800 // 2)

""" Creating a number indicator function for the score and putting it in the main start loop"""
def counter(c):
    score_number = c + 1 - 2
    score = font.render(str(score_number), True, blue, (255, 255, 0))
    scoreRect = score.get_rect()
    scoreRect.topright = (750, 50)
    screen.blit(score, scoreRect)



def convert(list):
    return tuple(list)
def colision(snek_list):

    ch1 = 0
    ch2 = 0
    for f in snek_list:

            cc = 0
            yy = 0
            xx = 0
            for i in convert(f):
                if cc == 0:
                    xx = i
                    cc = 1
                else:
                    yy = i
                for z in range(5):
                    if yy + z == player.rect.y or yy - z == player.rect.y:

                        ch1 = 1

                    if xx + z == player.rect.x or xx - z == player.rect.x:
                        ch2 = 1



            if ch1 + ch2 == 2:
                print("YEEEEEEESSSS")
                player.colided = 1
            else:
                ch1 = 0
                ch2 = 0

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0,0,0), [x[0], x[1], snake_block, snake_block])


control = 0
sep = 25
f = 0
check = 1
run = True
while run:


    pygame.display.update()
    world.draw()

    player_list.draw(screen)  # draw player


    pygame.display.flip()
    clock.tick(15)

    current_time = pygame.time.get_ticks()
    i = current_time









    screen.fill((255, 255, 0))


    steps = 18
    if player.colided == 0:
        player.update()
        counter(Lenght_of_snake)

    else:
        screen.blit(text, textRect)

    food.update()

    if pygame.sprite.collide_rect(food, player):
        check_time = pygame.time.get_ticks()
        Lenght_of_snake += 1
        food.control(1)
        player.start = 1






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0, 1)

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0, 2)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, -steps, 3)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps, 4)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(0, 0, 5)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(0, 0, 6)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, 0, 7)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, 0, 8)
            if event.key == ord('q'):

                pygame.quit()
                quit()
    pos_x = player.rect.x
    pos_y = player.rect.y
    snake_Head = []
    if player.direction == 2:
        snake_Head.append(pos_x + steps)
        snake_Head.append(pos_y)
        control = 1
    if player.direction == 1:
        snake_Head.append(pos_x - steps)
        snake_Head.append(pos_y)
        control = 1
    if player.direction == 3:

        snake_Head.append(pos_x)
        snake_Head.append(pos_y + steps)
        control = 1
    if player.direction == 4:

        snake_Head.append(pos_x)
        snake_Head.append(pos_y - steps)
        control = 1
    if control == 1:
        snake_List.append(snake_Head)
        if len(snake_List) > Lenght_of_snake:
            del snake_List[0]
        our_snake(snake_block, snake_List)


    colision(snake_List)







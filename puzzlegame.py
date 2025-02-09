import pygame
import random

# adding constants
width,height=500,500
grid_size=3 # 3x3
tile_size=width//grid_size

# loading image
image_path="/home/nix/Downloads/angela.jpg" # simply put yor interested pic or linnk of it..!!
original_img=pygame.image.load(image_path)
original_img=pygame.transform.scale(original_img, (width,height))

# initialize pygame
pygame.init()
screen=pygame.display.set_mode(( width, height + 50)) # 50 means adding extra space for buttons 
pygame.display.set_caption("Picture puzzle game")

# tiles creation
tiles=[]
positions=[]

# loop for tiles and positions
for row in range(grid_size):
    for col in range(grid_size):
        x,y=col*tile_size,row*tile_size # column * tile size and row * tile size
        tile=original_img.subsurface(( x, y, tile_size, tile_size))
        tiles.append(tile)
        positions.append((x,y))

# to remove the last tile to create an empty space ....
empty_pos=positions[-1]
tiles.pop()
positions.pop()


# shuffling the tiles
random.shuffle(positions)


# button colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font=pygame.font.Font(None,30)

def draw_buttn(text,x,y,color,action=None):
    button_rect=pygame.Rect(x ,y ,100,40)
    pygame.draw.rect(screen,color,button_rect)
    label=font.render(text,True,BLACK)
    screen.blit(label,(x+10,y+10))
    return button_rect

def swap_tiles(index):
    global positions,empty_pos

    # giving or get the position of the tiles x and y
    tile_x,tile_y=positions[index]
    empty_x,empty_y=empty_pos

    # checking if the clicked tile is next to the empty space
    if (abs(tile_x - empty_x) == tile_size and tile_y == empty_y) or (abs(tile_y - empty_y) == tile_size and tile_x == empty_x):
        # swapping positions
        positions[index],empty_pos=empty_pos,positions[index]

def check_win():
    return positions+[empty_pos]==[(col * tile_size, row * tile_size) for row in range(grid_size) for col in range(grid_size)]

running=True
hint_mode=False

while running:
    screen.fill(WHITE)

    # trying to show hit image
    if hint_mode:
        screen.blit(original_img,(0,0))
    else:
        for i,pos in enumerate(positions):
            screen.blit(tiles[i],pos)
    
    # drawing button
    hint_button=draw_buttn("Hint",100 ,height+5,RED)
    reset_button=draw_buttn("Reset",300,height+5,GREEN)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos


            # check hint buttn
            if hint_button.collidepoint(x,y):
                hint_mode=not hint_mode
            
            # check the reset button
            elif reset_button.collidepoint(x,y):
                random.shuffle(positions)
                hint_mode=False

            # checking the tile click
            elif y<height:
                for i,pos in enumerate(positions):
                    tile_x,tile_y=pos
                    if tile_x < x < tile_x + tile_size and tile_y < y < tile_y + tile_size:
                        swap_tiles(i)
                        if check_win():
                            # print("Congratulations! You can fap easily!")
                            print("आपको बधाई, अब आप आसानी से मुथ को मार सकते हैं!")
                            running = False
                        break
pygame.quit()


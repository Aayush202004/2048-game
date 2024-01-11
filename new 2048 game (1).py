import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 4
TILE_SIZE = 100
GRID_MARGIN = 10
SCREEN_WIDTH = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * GRID_MARGIN
SCREEN_HEIGHT = GRID_SIZE * TILE_SIZE + (GRID_SIZE + 1) * GRID_MARGIN
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
FONT = pygame.font.Font(None, FONT_SIZE)

# Colors for tiles
TILE_COLORS = {
    0: (204, 192, 179),
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
}

# Create the initial grid
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]


def add_new_tile():
    empty_tiles = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        grid[i][j] = 2 if random.random() < 0.9 else 4


def draw_grid(screen):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            tile_value = grid[i][j]
            tile_color = TILE_COLORS.get(tile_value, (255, 255, 255))
            tile_rect = pygame.Rect(
                j * (TILE_SIZE + GRID_MARGIN) + GRID_MARGIN,
                i * (TILE_SIZE + GRID_MARGIN) + GRID_MARGIN,
                TILE_SIZE,
                TILE_SIZE,
            )
            pygame.draw.rect(screen, tile_color, tile_rect)
            if tile_value != 0:
                text = FONT.render(str(tile_value), True, BLACK)
                text_rect = text.get_rect(center=tile_rect.center)
                screen.blit(text, text_rect)


def slide_tiles(row):
    new_row = [value for value in row if value != 0]  # Remove zeros
    new_row += [0] * (GRID_SIZE - len(new_row))  # Add zeros to the end
    return new_row


def merge_tiles(row):
    new_row = []
    i = 0
    while i < GRID_SIZE:
        if i + 1 < GRID_SIZE and row[i] == row[i + 1]:
            new_row.append(row[i] * 2)
            i += 2
        else:
            new_row.append(row[i])
            i += 1
    new_row += [0] * (GRID_SIZE - len(new_row))  # Add zeros to the end
    return new_row


def move_left():
    global grid
    new_grid = [slide_tiles(row) for row in grid]
    new_grid = [merge_tiles(row) for row in new_grid]
    if new_grid != grid:
        grid = new_grid
        add_new_tile()


def move_right():
    global grid
    reversed_grid = [row[::-1] for row in grid]
    new_grid = [slide_tiles(row) for row in reversed_grid]
    new_grid = [merge_tiles(row) for row in new_grid]
    new_grid = [row[::-1] for row in new_grid]
    if new_grid != grid:
        grid = new_grid
        add_new_tile()


def move_up():
    global grid
    transposed_grid = [list(row) for row in zip(*grid)]
    new_grid = [slide_tiles(row) for row in transposed_grid]
    new_grid = [merge_tiles(row) for row in new_grid]
    new_grid = [list(row) for row in zip(*new_grid)]
    if new_grid != grid:
        grid = new_grid
        add_new_tile()


def move_down():
    global grid
    new_grid = [list(row) for row in grid]
    for col in range(len(new_grid[0])):
        column = [new_grid[row][col] for row in range(len(new_grid))]
        column = slide_tiles(column[::-1])[::-1]  # Slide and reverse the column
        column = merge_tiles(column[::-1])[::-1]  # Merge and reverse the column
        for row in range(len(new_grid)):
            new_grid[row][col] = column[row]

    if new_grid != grid:
        grid = new_grid
        add_new_tile()


# Pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2048 Game")
clock = pygame.time.Clock()


def main():
    global grid
    add_new_tile()
    add_new_tile()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left()
                elif event.key == pygame.K_RIGHT:
                    move_right()
                elif event.key == pygame.K_UP:
                    move_up()
                elif event.key == pygame.K_DOWN:
                    move_down()

        screen.fill(WHITE)
        draw_grid(screen)
        pygame.display.flip()
        clock.tick(60)


import tkinter as tk
GUI_WINDOW_WIDTH = 300
GUI_WINDOW_HEIGHT = 150



def setup_pygame():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2048 Game")
    global clock
    clock = pygame.time.Clock()


# Function to start the game
def start_game():
    setup_pygame()
    global grid
    add_new_tile()
    add_new_tile()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left()
                elif event.key == pygame.K_RIGHT:
                    move_right()
                elif event.key == pygame.K_UP:
                    move_up()
                elif event.key == pygame.K_DOWN:
                    move_down()
        screen.fill(WHITE)
        draw_grid(screen)
        pygame.display.flip()
        clock.tick(60)


# GUI setup
from tkinter import *
from PIL import ImageTk,Image
def create_gui():
    root = tk.Tk()
    root.title("2048 Game Launcher")
    root.geometry("750x750")

    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("baki (1).png"))
    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()

    root.minsize(750,750)
    bg = PhotoImage(file="lmaoded.png")
    label1 = Label(root, image=bg)
    label1.pack()
    space1=Label()
    space1.pack()





    def play_button_click():
        root.destroy()
        start_game()

    def exit_button_click():
        root.destroy()
        pygame.quit()

    play_button = tk.Button(root, text="Play 2048",font=("Times",15,"bold"),command=play_button_click ,bg="light goldenrod",fg="black",height=1,width=15)
    play_button.pack()
    space2 = Label()
    space2.pack()


    exit_button = Button(root, text="Exit",command=exit_button_click,
                         bg="light goldenrod", fg="black",height=1,width=15,font=("Times",15,"bold"))
    exit_button.pack()
    space3 = Label()
    space3.pack()



    def open_controls_window():
        controls_window = Toplevel()  # Create a new window
        controls_window.title("Controls Window")

        custom_font = ('Arial', 20)
        custom_font1 = ('Arial', 17)
        custom_font2 = ('Arial', 13)

        label = Label(controls_window, text="How To Play 2048 game:", font=custom_font)
        label.pack()

        label2 = Label(controls_window, text="Tile Movement:", font=custom_font1)
        label2.pack(anchor='w')

        label3 = Label(controls_window,
                       text="1)In 2048, you play on a 4×4 grid, and your goal is to combine matching tiles to reach the elusive 2048 tile.",
                       font=custom_font2)
        label3.pack(anchor='w')

        label4 = Label(controls_window,
                       text="2)Swipe left, right, up, or down to move all the tiles in that direction. Every time you swipe, a new tile (either a 2 or 4) appears on an empty spot.",
                       font=custom_font2)
        label4.pack(anchor='w')

        label5 = Label(controls_window, text="Combining Tiles:", font=custom_font1)
        label5.pack(anchor='w')

        label6 = Label(controls_window,
                       text="1.Tiles with the same value can be combined by moving them into each other.",
                       font=custom_font2)
        label6.pack(anchor='w')

        label7 = Label(controls_window,
                       text="2.When two tiles of the same value collide, they merge into one tile with a value equal to their sum.",
                       font=custom_font2)
        label7.pack(anchor='w')

        label8 = Label(controls_window, text="Cornering High Values:", font=custom_font1)
        label8.pack(anchor='w')

        label9 = Label(controls_window,
                       text="1-Focus on building up high-value tiles in one corner to create a chain reaction for combining tiles.",
                       font=custom_font2)
        label9.pack(anchor='w')

        label10 = Label(controls_window,
                        text="2-Keep your highest tile in the corner to minimize the chances of breaking your sequence.",
                        font=custom_font2)
        label10.pack(anchor='w')

        label11 = Label(controls_window, text="Edge Management:", font=custom_font1)
        label11.pack(anchor='w')

        label12 = Label(controls_window,
                        text="1)Keep your high-value tiles along the edges to maximize space and prevent blocking.",
                        font=custom_font2)
        label12.pack(anchor='w')

        label13 = Label(controls_window,
                        text="2)Use the edges strategically to guide the flow of tiles and create more opportunities for combining.",
                        font=custom_font2)
        label13.pack(anchor='w')

        label14 = Label(controls_window, text="Prioritize Swiping Direction:", font=custom_font1)
        label14.pack(anchor='w')

        label15 = Label(controls_window,
                        text="1.Stick to one or two primary directions to avoid dispersing tiles and losing control.",
                        font=custom_font2)
        label15.pack(anchor='w')

        label16 = Label(controls_window,
                        text="2.Consistency in your swiping strategy helps in building patterns and sequences.",
                        font=custom_font2)
        label16.pack(anchor='w')

        image_label = tk.Label(controls_window, image=img1)
        image_label.pack()

    image_path = "red.png"  # Replace this with the path to your image
    img1 = Image.open(image_path)
    img1 = img1.resize((320, 320))  # Resize the image as needed
    img1 = ImageTk.PhotoImage(img1)




    def main_window():

        howtoplay_button = Button(root, text="Controls", command=open_controls_window,bg="light goldenrod",fg="black",height=1,width=15,font=("Times",15,"bold"))
        howtoplay_button.pack()


    main_window()


    root.geometry(f"{GUI_WINDOW_WIDTH}x{GUI_WINDOW_HEIGHT}")

    root.mainloop()



if __name__ == "__main__":
    create_gui()
if __name__ == "__main__":
    main()